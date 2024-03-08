# Install Packages
library("zoo")
library("solaR")
library("dplyr")

## A FUNCTION THAT EXTRACTS THE HOURLY SURFACE IRRADIANCE VALUES AND TEMPERATURE VALUES FROM A CSV FILE FOR A GIVEN YEAR AND RETURNS THEM IN A DATA FRAME
hourly_irradiance_from_csv <- function(dataset_filename, year) {

  #read in the data from the csv file
  data <- read.csv(dataset_filename)

  #filter for specific year
  yearly_data <- data %>% filter(grepl(year, time))

  #extract time and irradiance columns
  yearly_irradiance_data <- yearly_data[c('irradiance_surface', 'temperature')]

  return(yearly_irradiance_data)
}

## A FUNCTION THAT TAKES THE YEARLY IRRADIANCE DATA AND PREPARES IT SUCH THAT solaR CAN PROCESS THEM
prepare_data_for_solaR <- function(yearly_irradiance_data, year) {

  #rename columns according to solaR documentation
  colnames(yearly_irradiance_data)[colnames(yearly_irradiance_data) == 'irradiance_surface'] <- 'G0'
  colnames(yearly_irradiance_data)[colnames(yearly_irradiance_data) == 'temperature'] <- 'Ta'

  #prepare string based on year
  date_string <- paste(year,"-01-01 00:00", sep = "")

  #create an hourly time series over an entire year
  time_index <- seq(from = as.POSIXct(date_string), by = "hour", length.out = 8760, tz = "CET")

  #convert to zoo format
  prepared_data <- zoo(yearly_irradiance_data, time_index)


  return(prepared_data)
}

#TODO EXTRACT ANUAL TIME SERIES OF GENERATION
total_supply <- function(prepared_data, azimuthal_angle) {
}


# Parameters
azimuthal_angle <- 0
year <- 2019


hourly_irradiance <- hourly_irradiance_from_csv("ninja_weather_country_CH_merra-2_population_weighted.csv", year)

prepared_data <- prepare_data_for_solaR(yearly_irradiance_data = hourly_irradiance, year)


hourly_generation <- prodGCPV(47,
         "fixed",
         "bdI",
         dataRad =  prepared_data,
         "hour",
         TRUE,
         alfa = azimuthal_angle)

#TODO FIGURE OUT WHY NA AND WHY NO PRODUCTION IN AFTERNOON
hourly_generation_data <- as.data.frameI(hourly_generation)

head(hourly_generation_data, 250)

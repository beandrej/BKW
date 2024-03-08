# Install Packages
library("solaR")
library("dplyr")

## A FUNCTION THAT EXTRACTS THE HOURLY SURFACE IRRADIANCE VALUES FROM A CSV FILE FOR A GIVEN YEAR AND RETURNS THEM IN A DATA FRAME
hourly_irradiance_from_csv <- function(dataset_filename, year) {

  #read in the data from the csv file
  data <- read.csv(dataset_filename)

  #filter for specific year
  yearly_data <- data %>% filter(grepl(year, time))

  #extract time and irradiance columns
  yearly_irradiance_data <- yearly_data[c('time','irradiance_surface')]

  #create new data frame including the unit
  solar_data <- data.frame(
    Hours = yearly_irradiance_data[c('time')],
    Irradiance = yearly_irradiance_data[c('irradiance_surface')],
    Unit = "W/m^2"
  )
  return(solar_data)
}

total_supply <- 0

hourly_irradiance <- hourly_irradiance_from_csv("ninja_weather_country_CH_merra-2_population_weighted.csv", 2019)

print(head(hourly_irradiance, 150))
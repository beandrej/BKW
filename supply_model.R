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

## A FUNCTION THAT TAKES THE IRRADIANCE DATA AND PREPARES IT SUCH THAT solaR CAN PROCESS THEM
prepare_data_for_solaR <- function(yearly_irradiance_data, year, month_week) {

  month_string <- "-01"

  #rename columns according to solaR documentation
  colnames(yearly_irradiance_data)[colnames(yearly_irradiance_data) == 'irradiance_surface'] <- 'G0'
  colnames(yearly_irradiance_data)[colnames(yearly_irradiance_data) == 'temperature'] <- 'Ta'

  #find the amount of hours for the specified time range
  if (month_week[1] == 0) { #if range == full year
    if (year %% 4 == 0) { #check if leap year
      hours <- 8774
    } else {
      hours <- 8760
    }
  } else {
    if (month_week[1] < 10) {
    #specify the month string for one-digit months
      month_string <- paste("-0", month_week[1], sep = "")
    } else {
      month_string <- paste("-", month_week[1], sep = "") #two digit case (October, November, December)
    }

    if (month_week[2] == TRUE) { #if range == one week
      hours <- 168
    } else {

      if (month_week[1] == 1 || #31 day months
          month_week[1] == 3 ||
          month_week[1] == 5 ||
          month_week[1] == 7 ||
          month_week[1] == 8 ||
          month_week[1] == 10 ||
          month_week[1] == 12) {
        hours <- 31*24
      } else if (month_week[1] == 4 || #30 day months
                  month_week[1] == 6 ||
                  month_week[1] == 9 ||
                  month_week[1] == 11) {
        hours <- 30*24
      } else if (year %% 4 == 0) { #leap year February
        hours <- 29*24
      } else { #28 day February
        hours <- 28*24
      }
    }
  }


  #prepare string based on year and chosen month
  date_string <- paste(year, month_string, sep = "")
  date_string <- paste(date_string, "-01 00:00", sep = "")

  #create an hourly time series over an entire year
  time_index <- seq(from = as.POSIXct(date_string), by = "hour", length.out = hours, tz = "CET")

  #convert to zoo format
  prepared_data <- zoo(yearly_irradiance_data, time_index)


  return(prepared_data)
}

## A FUNCTION THAT READS A CVS FILE AND FINDS THE RANGE OF YEARS
## ASSUMES THE FILE COVERS A CONTINUOUS AMOUNT OF TIME, FULL YEARS, AND THAT THE FORMAT IS YYYY-MM-DD
find_range_of_years <- function (dataset_filename) {

  data <- read.csv(dataset_filename)

  first_year_entry <- data[1, "time"]
  first_year <- substr(first_year_entry, 1, 4)

  last_year_entry <- data[nrow(data) - 1, "time"]
  last_year <- substr(last_year_entry, 1, 4)

  return(list(first_year, last_year))
}

## A FUNCTION THAT ASKS THE USER WHICH YEAR FROM THE CVS FILE THEY WANT TO LOOK AT, ENSURING IT'S WITHIN THE FILE'S TIME RANGE
get_desired_year_from_user <- function(firstlast_year) {

  first_year <- firstlast_year[1]
  last_year <- firstlast_year[2]

  print_string <- paste("The provided CSV file covers the years", first_year)
  print_string <- paste(print_string, "to")
  print_string <- paste(print_string, last_year)
  print_string <- paste(print_string, ".", sep = "")
  print_string <- paste(print_string, "\n What year do you want to look at? \n")

  cat(print_string)
  desired_year <- readLines("stdin", n = 1)

  while (is.na(as.numeric(desired_year))) {
    cat("Please enter a numeric year in the format [YYYY] in the range. \n")
    desired_year <- readLines("stdin", n = 1)
    desired_year <- as.integer(desired_year)
  }

  desired_year <- as.integer(desired_year)

  while (desired_year < first_year || desired_year > last_year) {
    cat("That year is not in the set range. Try again. \n")
    desired_year <- readLines("stdin", n = 1)
    desired_year <- as.integer(desired_year)
  }

  return(desired_year)
}

## A FUNCTION THAT ASKS THE USER IF THEY WANT TO LOOK AT A WHOLE YEAR, A MONTH, OR A WEEK AND SAVES THE SPECIFIED MONTH IN A LIST
get_desired_time_range_from_user <- function () {

  month <- 0
  week <- FALSE

  cat("Would you like to check production over a week, a month or a year? \n w/m/y \n")
  desired_range <- readLines("stdin", n = 1)

  while (!(desired_range == "w" || desired_range == "m" || desired_range == "y")) {
    cat("Please enter \"w\" if you want to look at a single week, \"m\" if you want to look at a month, \"y\" if you want to look at the whole year. \n" )
    desired_range <- readLines("stdin", n = 1)
  }

  if (desired_range == "w" || desired_range == "m") {
    cat("Which month? Please provide a number from 1 to 12. \n")

    desired_month <- readLines("stdin", n = 1)

    while (is.na(as.numeric(desired_month))) {
      cat("Please enter a numeric between 1 and 12. \n")
      desired_month <- readLines("stdin", n = 1)
      desired_month <- as.integer(desired_month)
    }

    desired_month <- as.integer(desired_month)

    while (desired_month < 1 || desired_month > 12) {
      cat("That year is not in the set range. Try again. \n")
      desired_month <- readLines("stdin", n = 1)
      desired_month <- as.integer(desired_month)
    }

    if(desired_range == "w") {
      week <- TRUE
    }

    month <- desired_month
  }

  return(list(month, week))
}

#TODO EXTRACT TIME SERIES OF GENERATION
total_supply <- function(prepared_data, azimuthal_angle) {
}


# Parameters
azimuthal_angle <- 90

year <- get_desired_year_from_user(find_range_of_years("ninja_weather_country_CH_merra-2_population_weighted.csv"))

month_week <- get_desired_time_range_from_user()

print(month_week)

hourly_irradiance <- hourly_irradiance_from_csv("ninja_weather_country_CH_merra-2_population_weighted.csv", year)

prepared_data <- prepare_data_for_solaR(yearly_irradiance_data = hourly_irradiance, year, month_week)


hourly_generation <- prodGCPV(47,
         "fixed",
         "bdI",
         dataRad =  prepared_data,
         "hour",
         TRUE,
         alfa = azimuthal_angle)

#TODO FIGURE OUT WHY NA AND WHY NO PRODUCTION IN AFTERNOON
hourly_generation_data <- as.data.frameI(hourly_generation)

head(hourly_generation_data, 10)

print("…")

tail(hourly_generation_data, 10)

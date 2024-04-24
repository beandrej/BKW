################################################################################
# PV simulation - library
# FTA - 24.01.2023
################################################################################

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#--> libraries

library(solaR)
library(solarPos)
library(solrad)
library(tidyverse)
library(lubridate)
library(zoo)
library(lattice)
library(latticeExtra)



#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# Function for the simulation of a pv output
# Intraday simulated production

simprodpv_I<-function(weather,i,j,pv_params,sim.data) {
  
  G<-weather$irradiance_data
  Temp<-weather$ambient_temp-273.15
  Coord<-list(lon=weather$lon,lat=weather$lat)
  year<-as.numeric(weather$year)
  
  date<-seq(ISOdatetime(weather$year,1,1,0,0,0),ISOdatetime(weather$year,12,31,23,0,0),by="hours")
  
  dateloc<-local2Solar(date,lon=Coord$lon)
  
  dataI<-data.frame(G0=G,Ta=Temp,date=dateloc)

  dfI<-dfI2Meteo(file=dataI,lat=Coord$lat,format = '%Y-%m-%d %H:%M:%S',
                 time.col = 'date',source = 'NASA-MERRA2')


  gcpv<- prodGCPV(lat = Coord$lat,modeTrk=sim.data$modeTrk,modeRad='bdI',dataRad = dfI, sample="hour",keep.night =TRUE,
                  sunGeometry = 'michalsky',alfa=sim.data$alfa,beta=sim.data$beta,
                  betaLim=90,iS=sim.data$iS,alb=sim.data$alb,horizBright=sim.data$hB,HCPV=FALSE,
                  generator=pv_params$generator,module=pv_params$module,inverter=pv_params$inverter,effSys=pv_params$effSys)
  gcpv@prodI$Pac<-na.approx(gcpv@prodI$Pac)
  gcpv@prodI$Pdc<-na.approx(gcpv@prodI$Pdc)
  
  prodnorm<-gcpv@prodI$Pac/as.numeric(gcpv@generator$Pg)
  result<-list(profile=prodnorm,prod=gcpv)
  result
}




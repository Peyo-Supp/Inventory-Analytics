Data <- read.csv("data5.csv", header= TRUE)
head(Data)
drop <- c("X")
Data = Data[,!(names(Data) %in% drop)]
Data <- Data[, c("Date","Id","Quantity")]

head(Data)

library("forecast")
library("DBI")
library("RPostgreSQL")
library("lubridate")
#
target_value  <- function(target){

Id <- unique(Data["Id"][,])

for (i in Id) {
  train <- head(Data[target][Data["Id"]==i] , 500)
  train <- ts(train[1:(length(train))],frequency = 104)

  fc1 = auto.arima(train)
  pred1 = forecast( fc1)
  fit1_acry = accuracy(pred1)

  fc2 = stlf(train,)   # forecast 2
  pred2 = forecast( fc2 )
  fit2_acry = accuracy(pred2 )

  MAPE <- data.frame ( fit1_MAPE = fit1_acry[,'MAPE'],
                         fit2_MAPE = fit2_acry[,'MAPE']
  )

  best <-  which.min(MAPE)

  BestModel = get(paste('fc',best,sep=""))

  forecastoutput <- data.frame(forecast(BestModel, h=8 ))


  plot(forecastoutput$Point.Forecast ,type = "l" )
}

write.table(forecastoutput, file=paste0('output', i, format(Sys.time()), target,  '.csv'))



}

target <- 50
View(target_value("Quantity"))



load("./data/PUMSRawData.Rdata")
write.csv(rawPumsData, file = "./data/PUMSRawData.csv", row.names = FALSE)
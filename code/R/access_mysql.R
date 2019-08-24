install.packages("RMySQL")
library(RMySQL)
mydb = dbConnect(MySQL(), user='{User Account}', password='{User Password}', dbname='{Database Name}', host=’{SERVER_IP}2’)
dbListTables(mydb)
dbListFields(mydb, 'some_table')

rs = dbSendQuery(mydb, "{SQL_SELECT}")
data = fetch(rs, n=-1)
data
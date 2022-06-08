setwd("~/Desktop/")
# read file
data1 = read.csv('M1 framed 30.csv')
data2 = read.csv('M2 framed 30.csv')
data3 = read.csv('M3 framed 30.csv')
data4 = read.csv('M4 framed 30.csv')
#data5 = read.csv('CL_2 framed.csv')

# convert to list
myls1 = list(data1$Track.n)
myls2 = list(data2$Track.n)
myls3 = list(data3$Track.n)
myls4 = list(data4$Track.n)
#myls5 = list(data5$Track.n)

# count
df1 = as.data.frame(table(myls1[1][1]))
df2 = as.data.frame(table(myls2[1][1]))
df3 = as.data.frame(table(myls3[1][1]))
df4 = as.data.frame(table(myls4[1][1]))
#df5 = as.data.frame(table(myls5[1][1]))

# delete
del1 = subset(df1, df1$Freq < 12)
a = 0
for (i in 1:nrow(del1)) {
  a = as.integer(as.character(del1[i, 1]))
  if (is.na(a)){
    break
  }else{
    data1 = data1[!(data1$Track.n == a),]
  }
}

del2 = subset(df2, df2$Freq < 12)
a = 0
for (i in 1:nrow(del2)) {
  a = as.integer(as.character(del2[i, 1]))
  if (is.na(a)){
    break
  }else{
    data2 = data2[!(data2$Track.n == a),]
  }
}

del3 = subset(df3, df3$Freq < 12)
a = 0
for (i in 1:nrow(del3)) {
  a = as.integer(as.character(del3[i, 1]))
  if (is.na(a)){
    break
  }else{
    data3 = data3[!(data3$Track.n == a),]
  }
}

del4 = subset(df4, df4$Freq < 12)
a = 0
for (i in 1:nrow(del4)) {
  a = as.integer(as.character(del4[i, 1]))
  if (is.na(a)){
    break
  }else{
    data4 = data4[!(data4$Track.n == a),]
  }
}

#del5 = subset(df5, df5$Freq < 12)
#a = 0
#for (i in 1:nrow(del5)) {
#  a = as.integer(as.character(del5[i, 1]))
#  if (is.na(a)){
#    break
#  }else{
#    data5 = data5[!(data5$Track.n == a),]
#  }
#}

write.csv(df1,"M1 check.csv", row.names = FALSE)
write.csv(df2,"M2 check.csv", row.names = FALSE)
write.csv(df3,"M3 check.csv", row.names = FALSE)
write.csv(df4,"M4 check.csv", row.names = FALSE)
#write.csv(df5,"CL_2 check.csv", row.names = FALSE)
write.csv(data1,"M4_pos1 for frame.csv", row.names = FALSE)
write.csv(data2,"M4_pos4 for frame.csv", row.names = FALSE)
write.csv(data3,"M8_pos1 for frame.csv", row.names = FALSE)
write.csv(data4,"M8_pos4 for frame.csv", row.names = FALSE)
#write.csv(data5,"CL_2 for frame.csv", row.names = FALSE)

# next step: loop over to set frame


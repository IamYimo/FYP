# read file
data1 = read.csv('PL_new.csv')
data2 = read.csv('CL_new.csv')

# convert to list
myls1 = list(data1$Track.n)
myls2 = list(data2$Track.n)

# count
df1 = as.data.frame(table(myls1[1][1]))
df2 = as.data.frame(table(myls2[1][1]))


b1 = barplot(table(df1$Freq), ylim = c(0, 200), main = "PL Frame", 
             xlab = "Track with frame length of", ylab = "Frequency" )
text(x = b1, table(df1$Freq) + 10 ,table(df1$Freq) )
b2 = barplot(table(df2$Freq), ylim = c(0, 200), main = "CL Frame", 
             xlab = "Track with frame length of", ylab = "Frequency" )
text(x = b2, table(df2$Freq) + 10 ,table(df2$Freq) )
#barplot(table(df2_2$Freq), ylim = c(0, 65),main = "M2_2 Frame")
#barplot(table(df2$Freq), ylim = c(0, 80),main = "M7 Frame")
#barplot(table(df4$Freq), ylim = c(0, 65),main = "M4 Frame")

#write.csv(data,"Frame.csv", row.names = FALSE)

# delete
del1 = subset(df1, df1$Freq < 28)
a = 0
for (i in 1:nrow(del1)) {
  a = as.integer(as.character(del1[i, 1]))
  data1 = data1[!(data1$Track.n == a),]
}

del2 = subset(df2, df2$Freq < 28)
a = 0
for (i in 1:nrow(del2)) {
  a = as.integer(as.character(del2[i, 1]))
  data2 = data2[!(data2$Track.n == a),]
}

#del2_2 = subset(df2_2, df2_2$Freq < 33)
#a = 0
#for (i in 1:nrow(del2_2)) {
#  a = as.integer(del2_2[i, 1])
#  data2_2 = data2_2[!(data2_2$Track.n == a),]
#}

#del3 = subset(df3, df3$Freq < 30)
#a = 0
#for (i in 1:nrow(del3)) {
#  a = as.integer(as.character(del3[i, 1]))
#  data3 = data3[!(data3$Track.n == a),]
#}

#del4 = subset(df4, df4$Freq < 30)
#a = 0
#for (i in 1:nrow(del4)) {
#  a = as.integer(as.character(del4[i, 1]))
#  data4 = data4[!(data4$Track.n == a),]
#}

write.csv(data1,"~/Desktop/Intermediate manual CL for frame.csv", row.names = FALSE)
write.csv(data2,"~/Desktop/Intermediate automated CL for frame.csv", row.names = FALSE)
#write.csv(data2_2,"~/Desktop/Distance/Early CL (2_2).csv", row.names = FALSE)
#write.csv(data3,"~/Desktop/Early CL (3).csv", row.names = FALSE)
#write.csv(data4,"~/Desktop/Distance/Early CL (4).csv", row.names = FALSE)

# next step: loop over to set frame

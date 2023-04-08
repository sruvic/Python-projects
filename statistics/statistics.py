import statistics as stats
#mean

st_Age = [9,10,10,11,11,11,12,12,14,14,15]
st_AgeOdd = [9,10,10,11,11,11,12,12,12,14,14,15,13]

print ("The mean is ", stats.mean(st_Age))


#median
print ("The Median is when even ", stats.median(st_Age))

#Odd
print ("The Median is when Odd " , stats.median(st_AgeOdd))

#calc the mode

print ("The mode is ", stats.mode(st_Age))
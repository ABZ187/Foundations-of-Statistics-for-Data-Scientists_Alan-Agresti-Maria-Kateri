import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.formula.api as smf
import statsmodels.api as sm

# #random sample of 5 as list without replacement (nos will not be repeated insample)
# randomsample=random.sample(range(1,6),5) 
# print(randomsample,type(randomsample))

# #random sample of 5 as array with replacement (nos can be repeated insample)
# list1 = list(range(1,6))
# randomsample2 = np.random.choice(list1,5)
# print(randomsample2,type(randomsample2))

#read csv file
# carbon = pd.read_csv('http://stat4ds.rwth-aachen.de/data/Carbon.dat',sep='\s+')
# print(type(carbon)) #DataFrame type
# print(carbon.shape) 
# print(carbon.loc[[20]])  # data at index 20
# print(carbon.columns) # column names
# print(carbon.head())    #first 5 values in data frame
# print(carbon.tail())

# # count, mean, std, min, lower quartile (25th percentile),  median (50th percentile), upper quartile (75th percentile),  max
# print(carbon.describe())

# #mean
# print('mean',carbon['CO2'].mean())

# #std
# print('std',carbon['CO2'].std())

# #median
# print('median',carbon['CO2'].median())

# #plot histogram
# #bins=total no. of bars. density=True shows proportion such that integral of the plot is 1.
# #density=False uses counts for y-axis
# plt.hist(carbon['CO2'],density=True, bins=10,color="green",edgecolor="black") 
# plt.ylabel('proportion')
# plt.xlabel('C02')
# plt.title("Histogram of CO2 proportion")
# plt.show()

# #subplot is used to create multiple plots in a single image. Return figure and axes of each plot
# fig1,ax1 = plt.subplots()
# plt.xlabel("CO2")
# plt.boxplot(carbon["CO2"],vert=False) #boxplot
# plt.show()

# #side by side boxplot
# crime = pd.read_csv("http://stat4ds.rwth-aachen.de/data/Murder2.dat",sep="\s+")
# sns.boxplot(x="murder",y="nation", data=crime,orient='h')
# plt.show()                  #as sns is based on matplotlib 


# gs = pd.read_csv("http://stat4ds.rwth-aachen.de/data/Guns_Suicide.dat",sep="\s+")
# #no of non missing values
# print(gs.info()) 

# #correlation matrix
# print(gs.corr()) 

# #scatter plot
# gs.plot(kind="scatter",x="guns",y="suicide",color="green",figsize=(8,6))
# plt.xlabel("Guns")
# plt.ylabel("Suicide")
# plt.show()

# # gives 5 equally spaced numbers including the endpoints, spaces are 4. (end-start)/(no - 1) interval lenght 
# x=np.linspace(0,20,5)

# #returns coefficient and constants of polynomial. below eg. returns m and c from y=mx+c.
# coef= np.polyfit(gs["guns"],gs["suicide"],1)

# #turn list into polynomial. if list is of n no.s then polynomial of deg n-1 will generate 
# yn= np.poly1d(coef)

# #set figure size
# fig =plt.figure(figsize=(8,6))

# #returns output of the polynomial at individual values of coef
# print(yn(gs["guns"]))

# #2 plots on same graph. first is scatter plot of guns and suicide. second is line graph of guns and output of polynomial yn
# plt.plot(gs["guns"],gs["suicide"],'o',gs["guns"],yn(gs["guns"]))

# plt.xlabel("Guns",size=14)
# plt.ylabel("Suicide",size=14)
# plt.show()

# #fit a linear model to data. Ordinary Least Squares(OLS) function
# mod = smf.ols(formula='suicide ~ guns',data=gs).fit()

# #returns intercept and slope
# print(mod.params)

# #returns summary of model https://medium.com/swlh/interpreting-linear-regression-through-statsmodels-summary-4796d359035a
# print(mod.summary())

# pid = pd.read_csv("http://stat4ds.rwth-aachen.de/data/PartyID.dat",sep="\s+")

# #contigency table
# pid_table=pd.crosstab(pid['race'],pid['id'],margins=False)
# print(pid_table)

# from scipy.stats.contingency import margins
# #sum of rows and sum of columns
# mr,mc=margins(pid_table)

# #joint probability distribution
# asarray = np.array(pid_table)/sum(sum(np.array(pid_table)))
# probdist = pd.DataFrame(asarray,columns=["Democrat" , "Independent"  ,"Republican"],index=["race","white","other"])
# print(probdist)

# #row wise probability distribution
# asarray2 = np.array(pid_table)/mr
# print(pd.DataFrame(asarray2,columns=["Democrat" , "Independent"  ,"Republican"],index=["race","white","other"]))

# #alternative contigency table through statsmodel
# table = sm.stats.Table.from_data(pid)
# print(table)

# #mosaic plot
# from statsmodels.graphics.mosaicplot import mosaic
# fig ,_ = mosaic(pid,index=["race","id"])
# plt.show()


# mu, sigma = 100 ,16
# #random sample of size 30 following normal distribution with population mean mu, population std sigma
# y1 = np.random.normal(mu,sigma,30)
# print(y1.mean(),y1.std())
# plt.hist(y1,bins="auto",edgecolor="black")
# plt.show()  

# y2 = np.random.normal(mu,sigma,30)
# print(y2.mean(),y2.std())
# plt.hist(y2,bins="auto",edgecolor="black")
# plt.show()
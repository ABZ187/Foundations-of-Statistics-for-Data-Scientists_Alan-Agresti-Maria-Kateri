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
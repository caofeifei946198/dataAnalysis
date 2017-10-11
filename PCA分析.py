import pandas as pd
from pandas_datareader import data
import pandas_datareader.data as web
import numpy as np
np.random.seed(1000)
import scipy.stats as scs
import statsmodels.api as sm
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn.decomposition import KernelPCA#导入机器学习的ＰＣＡ包
symbols = ['ADS.DE', 'ALV.DE','BAS.DE','BAYN.DE','BEI.DE','BMW.DE','CBK.DE','CON.DE','DAI.DE',
           'DB1.DE','DBK.DE','DPW.DE','DTE.DE','EOAN.DE','FME.DE','FRE.DE','HEI.DE','HEN3.DE',
           'IFX.DE','LHA.DE','LIN.DE','LXS.DE','MRK.DE','MUV2.DE','RWE.DE','SAP.DE','SDF.DE',
           'SIE.DE','TKA.DE','VOW3.DE','^GDAXI',]#DAX30指数各个股票的代码以及德国３０指数代码
data = pd.DataFrame()
for sym in symbols:#获取数据
    data[sym] = web.DataReader(sym,data_source='google')['Close']
data = data.dropna()#丢弃缺失值
dax = pd.DataFrame(data.pop('^GDAXI'))#将指数数据单独拿出来，采用pop在获取的时候已经从原来的地方删除这一列数据了
scale_function = lambda x:(x-x.mean())/x.std()
pca = KernelPCA().fit(data.apply(scale_function))#这里用到了apply函数，做ＰＣＡ前我们要对数据做标准化
get_we = lambda x:x/x.sum()
print(get_we(pca.lambdas_))[:10]

pca = KernelPCA(n_components=1).fit(data.apply(scale_function))
dax['PCA_1'] = pca.transform(data)
dax.apply(scale_function).plot(figsize = (8,4))
pca = KernelPCA(n_components=5).fit(data.apply(scale_function))
weights = get_we(pca.lambdas_)
dax['PCA_5'] = np.dot(pca.transform(data),weights)

plt.figure(figsize=(8,4))
plt.scatter(dax['PCA_5'],dax['GDAXI'],color = 'r')
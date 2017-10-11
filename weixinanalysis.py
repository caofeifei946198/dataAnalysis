import itchat
import numpy
import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame

itchat.login()
#get friends information
friends = itchat.get_friends()
print(friends)
#build variable and save friends
def get_var(var):
    variable =[]
    for i in friends:
        value = i[var]
        variable.append(value)
    return variable

#use get_var to get information
NickName = get_var('NickName')
Province = get_var('Province')
print(NickName, Province)
data = {
    'NickName':NickName,
'Province':Province
}
frame = DataFrame(data)#save data
print(frame)
#data chuli
#data groupby
aggResult = frame.groupby(
    by=['Province']
)['NickName'].agg({'人数':numpy.size,})
print(aggResult)
#transform data type

aggResult['好友数'] = aggResult.人数.astype(int)
aggResult['地区'] = aggResult.index
#data standard
# new data = (raw data-min) /(max - min)
aggResult['scala'] = (
aggResult.好友数 - aggResult.好友数.min()
) / (aggResult.好友数.max() - aggResult.好友数.min())
print(aggResult['好友数'], aggResult['地区'], aggResult['scala'])
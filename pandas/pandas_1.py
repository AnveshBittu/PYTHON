import pandas as pd

# series

# data=[1,2,3,4,5,6,7,8]
# res=pd.Series(data)
# print(res)\


# data=['anvesh','chinna','gopi']
# res=pd.Series(data,index=['a','b','c'])
# print(res)


# res=pd.Series(
#     ['anvesh','chinna','gopi'],
#     index=['a','b','c']
# )
# print(res)


# dataframe

# data={
#     'names':['anvesh','chinna','gopi'],
#     'age':[22,33,44]
# }
# res=pd.DataFrame(data)
# print(res)


# data=pd.DataFrame(
#     [['anvesh',33,'guntur'],['bittu',55,'vinukonda'],['chinna',123,'bandar'],['gopi',1239,'tpk']],
#     columns=['names','age','location'],
#     index=['a','b','c','d']
# )
# # print(data)

# data['surename']=['y','y','c','h']
# print(data)


# data.insert(0,'surname',['y','y','c','h'])
# print(data)




# append

data=pd.DataFrame(
    [['anvesh',33,'guntur'],['bittu',55,'vinukonda'],['chinna',123,'bandar'],['gopi',1239,'tpk']],
    columns=['names','age','location'],
    index=['a','b','c','d']
)


# data_add={'names':'leo','age':99,'location':'my_heart'}
# ok=data._append(data_add,ignore_index=True)
# print(ok)

# res=data.head(2)
# print(res)

# res=data.tail(1)
# print(res)



#values

# import numpy as np

# res=pd.DataFrame({'abc':np.random.randint(1,9,size=(10)), 'def':np.random.randint(100,200,size=(10))})
# # print(res)
# res_1=res.abc.values
# print(res_1)
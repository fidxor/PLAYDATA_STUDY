import numpy as np
import pandas as pd 

'''
pivot
'''

df1 = pd.DataFrame({'cust_id': ['c1', 'c1', 'c1', 'c2', 'c2', 'c2', 'c3', 'c3', 'c3'],
                    'prod_cd': ['p1', 'p2', 'p3', 'p1', 'p2', 'p3', 'p1', 'p2', 'p3'],
                    'grade' : ['A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B'],
                    'pch_amt': [30, 10, 0, 40, 15, 30, 0, 0, 10]})

df_pivot = df1.pivot(index='cust_id', columns='prod_cd', values='pch_amt')
print(df_pivot)


'''
melt
'''

df2 = pd.DataFrame({'cust_ID' : ['C_001', 'C_001', 'C_002', 'C_002'],
                    'prd_CD' : ['P_001', 'P_002', 'P_001', 'P_002'],
                    'pch_cnt' : [1, 2, 3, 4], 'pch_amt' : [100, 200, 300, 400]})
print(df2.melt())


'''
cust_ID와 prd_CD 칼럼의 값
C_001, P_001, 의 
'''
df_melt = pd.melt(df2, id_vars=['cust_ID', 'prd_CD'])
# print(df_melt)


# melt의 variable 이름 , value 이름을 직접 지정해 줄수 있다.
df_melt_setName = pd.melt(df2, id_vars=['cust_ID', 'prd_CD'], var_name='pch_CD', value_name='pch_value')
# print(df_melt_setName)


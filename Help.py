# 
# # coding: utf-8
# 
# # In[5]:
# 
# 
# import pandas as pd
# df = pd.DataFrame()
# df['a','b','c','s'] = [["a",2,3,4],["a",5,6,7],["d",9,5,4]]
# print(df)
# 
# #problem  - need to have a new column follwing the logic below - 
# df['new_col']  = [1,2,3]
# print(df)
# 
# #the column values should be calculaed on column 'c' 
# # BUT modified when column 'a' has value equal 'a' and rest should be as they are
# #DO NOT USE FOR LOOP BECAUSE THE LOGIC NEEDS TO BE APPLIED ON MORE THAN 10,000,0000 ROWS. IT WONT WORK!
# 
# 
# # In[6]:
# 
# 
# #df


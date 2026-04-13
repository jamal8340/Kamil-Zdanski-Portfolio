import pandas as pd
import numpy as np
import json
import re

#ex0 e
with open('lab3_params.json', 'r') as f:
    params = json.load(f)

#ex1
df1=pd.read_json('lab3_ex01_data1.json')
df2=pd.read_json('lab3_ex01_data2.json')
df3=pd.read_json('lab3_ex01_data3.json')
bigdataframe=pd.concat([df1, df2, df3],ignore_index=True)
bigdataframe.to_json('lab3_ex01_concatenated.json', orient='records')
concat_columns = params["concat_columns"]
bigdataframe["description"] = bigdataframe[concat_columns].astype(str).agg(" ".join, axis=1)
bigdataframe.to_json('lab3_ex01_descriptions.json', orient='records')

#ex2
more_data=pd.read_json('lab3_ex02_more_data.json')
join_columns=params['join_column']

join1 = bigdataframe.merge(more_data, how='left', on=join_columns)
join1.to_json('lab3_ex02_join1.json', orient='records')

join2 = bigdataframe.merge(more_data, how='right', on=join_columns)
join2.to_json('lab3_ex02_join2.json', orient='records')

join3 = bigdataframe.merge(more_data, how='outer', on=join_columns)
join3.to_json('lab3_ex02_join3.json', orient='records')

join4 = bigdataframe.merge(more_data, how='inner', on=join_columns)
join4.to_json('lab3_ex02_join4.json', orient='records')

#ex3

int_columns = params.get('int_columns',[])

for idx, row in join4.iterrows():

    description=row["description"]
    file_name_desc=description.lower().replace(' ', '_')

    data = row.drop("description").to_dict()
    file_name = f"lab3_ex03_{file_name_desc}.json"

    with open(file_name, "w") as f:
        json.dump(data, f)




    data_int = data.copy()
    
    for col in int_columns:
        if col in data_int and pd.notna(data_int[col]):
            data_int[col] = int(data_int[col])
    
    for k, v in data_int.items():
        if pd.isna(v):
            data_int[k] = None
    
    file_name_int = f"lab3_ex03_int_{file_name_desc}.json"
    with open(file_name_int, "w") as f:
        json.dump(data_int, f)

#ex4
paramsdf = pd.DataFrame([params])

aggregations = paramsdf["aggregations"].at[0]
params_ex4={}

for key, value in aggregations:
        params_ex4[key] = value
pomdf=pd.DataFrame()
pomdf=join4.copy()
dfex4=pomdf.agg(params_ex4)
json_ex4={}
for col, f in aggregations:
    key= f"{f}_{col}"
    value=dfex4[col]
    json_ex4[key]=value

with open("lab3_ex04_aggregations.json", "w") as f:
    json.dump(json_ex4, f,indent=4)

#ex5

params_ex5=paramsdf["grouping_column"].at[0]
grouped_ex5=pomdf.groupby(params_ex5)
grouped_ex5=grouped_ex5.filter(lambda x: len(x)>1)
mean_ex5=grouped_ex5.groupby(params_ex5).mean(numeric_only=True)
mean_ex5.to_csv("lab3_ex05_groups.csv",header=True,index=True)

params2_ex5=paramsdf["extra_category"].at[0]
df_ex5=pomdf.copy()
df_ex5[params_ex5]=df_ex5[params_ex5].astype("category")
df_ex5[params_ex5]=df_ex5[params_ex5].cat.add_categories([params2_ex5])
mean2_ex5=df_ex5.groupby(params_ex5).mean(numeric_only=True)
mean2_ex5=mean2_ex5.fillna(0)
mean2_ex5.to_csv("lab3_ex05_groups_categories.csv",index=True,header=True)

#koniec

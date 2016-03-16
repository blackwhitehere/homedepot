import pandas as pd

df_train = pd.read_csv('/home/stan/Documents/dev/homedepot/input/train.csv', encoding="ISO-8859-1")
df_test = pd.read_csv('/home/stan/Documents/dev/homedepot/input/test.csv', encoding="ISO-8859-1")
df_pro_desc = pd.read_csv('/home/stan/Documents/dev/homedepot/input/product_descriptions.csv')
df_attr = pd.read_csv('/home/stan/Documents/dev/homedepot/input/attributes.csv')
df_attr["name_value"] = df_attr['name'].astype(str) + ' ' + df_attr['value'].astype(str)


def concat(df):
    rtn = ""
    for i in range(df.shape[0]):
        rtn += str(df['name_value'].iloc[i]) + ' '
    return rtn


df_attr = df_attr.groupby('product_uid').apply(concat)
df_attr = pd.DataFrame({'product_uid': df_attr.index, 'name_value': df_attr.values})

num_train = df_train.shape[0]
df_all = df_train


def trans(df_all):
    df_all = pd.merge(df_all, df_pro_desc, how='left', on='product_uid')
    df_all = pd.merge(df_all, df_attr, how='left', on='product_uid')

    df_all['product_description'] = df_all['product_description'].astype(str) + ' ' + df_all['name_value'].astype(str)
    del df_all['name_value']
    df_all['product_title'] = df_all['product_uid'].astype(str) + ' ' + df_all['product_title'].astype(str)
    del df_all['product_uid']
    df_all.rename(columns={'search_term': 'query', 'relevance': 'median_relevance'}, inplace=True)
    df_all['relevance_variance'] = 0

    return df_all
import os
trans(df_train).to_csv(os.getcwd()+'/raw_data/train.csv')
trans(df_test).to_csv(os.getcwd()+'/raw_data/test.csv')

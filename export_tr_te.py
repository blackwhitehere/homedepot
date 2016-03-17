import pandas as pd
import os

path = os.getcwd()


def toutf8(x):
    return x.decode('iso-8859-1').encode('utf-8')


df_train = pd.read_csv(path + '/input/train.csv', encoding="ISO-8859-1")[0:50]
df_test = pd.read_csv(path + '/input/test.csv', encoding="ISO-8859-1")[0:50]
df_pro_desc = pd.read_csv(path + '/input/product_descriptions.csv')[0:50] #iso or unicode?
df_attr = pd.read_csv(path + '/input/attributes.csv')[0:50]
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

    # def chtype(x):
    #     if type(x) == 'numpy.int64' or type(x) == 'numpy.float64':
    #         return x.encode('iso-8859-1')
    #     # else:
    #         return x
    #
    # for c in df_all.columns:
    #     df_all[c] = df_all[c].map(lambda x: chtype(x))
    #     df_all[c] = df_all[c].map(lambda x: x.decode('ISO-8859-1').encode('utf-8'))

    return df_all


trans(df_train).to_csv(os.getcwd() + '/raw_data/train.csv')
trans(df_test).to_csv(os.getcwd() + '/raw_data/test.csv')

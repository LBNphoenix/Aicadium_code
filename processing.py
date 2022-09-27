import pandas as pd
 
def feature_bin(df):
    
    df_eco_other = df.select_dtypes(exclude = ['category'])
    df_eco_cat = df.select_dtypes(include = ['category'])

    df_eco_other['Weekend'] = df_eco_other['Weekend'].astype('category').cat.codes.astype('int64')
    df_eco_other['Month'] = df_eco_other['Month'].astype('category').cat.codes.astype('int64')
    df_eco_other['VisitorType'] = df_eco_other['VisitorType'].astype('category').cat.codes.astype('int64')
    
    for col in df_eco_cat.columns:
        df_eco_cat[col] = df_eco_cat[col].cat.codes.astype('int64')
    df_ip_tree = pd.concat([df_eco_cat, df_eco_other],axis = 1)
    return df_ip_tree
def data_exploration(df, list_primary_keys, excelname): 
    columns = df.columns.to_list()
    columns = [col for col in columns if col not in list_primary_keys]

    writer = pd.ExcelWriter(desc_path+excelname+'.xlsx', engine='xlsxwriter')

    # controllo inizialmente le chiavi 

    data=dict()
    data['Description'] = ["# Null key "+key for key in list_primary_keys]
    data['Values'] = [df[key].isnull().sum() for key in list_primary_keys]
    keys_desc = pd.DataFrame(data=data)     
    keys_desc.to_excel(writer, sheet_name="primary_keys", index=False)   

    for col in columns: 
        type = df[col].dtype
        if type == 'O': 
            columns_desc = pd.DataFrame(data=df[col].value_counts(dropna=False)).reset_index().rename({'index':'Variable Value ', col:'Count'}, axis=1)
        elif type == '<M8[ns]': 
            data=dict()
            data['Description'] = ['min', 'max']
            data['Values'] = [df[col].min(), df[col].max()]
            columns_desc = pd.DataFrame(data=data)            
        else:
            columns_desc = pd.DataFrame(data=df[col].describe([x*0.1 for x in range(10)])).reset_index().rename({'index':'Description', col:'Values'}, axis=1)
            
        general_desc = dict()
        general_desc['Description'] = list()
        general_desc['Values'] = list()
        general_desc['Description'].extend(['DB Lenght', '# Null Values','% Null Values'])
        general_desc['Values'].extend([len(df), df[col].isnull().sum(), df[col].isnull().sum() / len(df)])

        general_desc = pd.DataFrame(data=general_desc)

        general_desc.to_excel(writer, sheet_name=col, startrow=0, index=False)
        columns_desc.to_excel(writer, sheet_name=col, startrow=len(general_desc)+3, index=False)

    writer.save()

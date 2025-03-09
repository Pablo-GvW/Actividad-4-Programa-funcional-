

##A##
def cargar_dataset(archivo):
#Cargar las librerias dentro de la función
    import pandas as pd
    import os
    extension = os.path.splitext(archivo)[1].lower()
    #Cargar el archivo según su extensión
    if extension == '.csv':
        df = pd.read_csv(archivo)
        return(df)
    elif extension == '.xlsx':
        df = pd.read_excel(archivo)
        return(df)
    elif extension == '.json':
        df = pd.read_json(archivo)
        return(df)
    elif extension == '.html':
        df = pd.read_html(archivo)
        return(df)
    else:
        raise ValueError(f"Formato de archivo no soportado: {extension}")


##B##
def sustitucion_ffill(df, columnas):
    import pandas as pd
    for x in columnas:  
        data_type = df[x].dtype  
        if (data_type == "object") | (data_type == "category")|(data_type == "int64") | (data_type == "float64"):  
            df[x] = df[x].fillna(method="ffill")  
    return df 
##C##
def sustitucion_bfill(df, columnas):
    import pandas as pd
    for x in columnas:  
        data_type = df[x].dtype  
        if (data_type == "object") | (data_type == "category")|(data_type == "int64") | (data_type == "float64"):  
            df[x] = df[x].fillna(method="bfill")  
    return df 
##D##
def sustitucion_string(df, columnas):
    import pandas as pd
    for x in columnas:  
        data_type = df[x].dtype  
        if (data_type == "object") | (data_type == "category"):  
            df[x] = df[x].fillna("f")
    return df

##E##
def sustitucion_mean(df, columnas):
    import pandas as pd
    # Seleccionar las columnas numéricas (int, float)
    for x in columnas:  
        data_type = df[x].dtype  
        if (data_type == "int64") | (data_type == "float64"):  
            mean_value = df[x].mean()    
            df[x] = df[x].fillna(round(mean_value, 1)) 
    return df 

    
##F##
def sustitucion_median(df, columnas):
    import pandas as pd
    for x in columnas:  
        data_type = df[x].dtype  
        if (data_type == "int64") | (data_type == "float64"):  
            mediana_value = df[x].median()    
            df[x] = df[x].fillna(round(mediana_value, 1)) 
    return df 
##G##
def sustitucion_constante(df, columnas):
    import pandas as pd
    for x in columnas:  
        data_type = df[x].dtype  
        if (data_type == "int64") | (data_type == "float64"):  
            df[x] = df[x].fillna(5)
    return df 
##H##
def valores_nulos(df): 
    valores_nulos_por_columna = df.isnull().sum()
    valores_nulos_dataframe = df.isnull().sum().sum()
    return("Nulos por columna", valores_nulos_por_columna,
           "Nulos por dataframe", valores_nulos_dataframe)

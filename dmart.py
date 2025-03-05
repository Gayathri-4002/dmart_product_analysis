import pandas as pd
import sqlalchemy as sal
import os 

#selecting the file location
datasetFilePath=os.path.dirname(__file__)+"/dataset/DMart.csv"

#loading the file
def loadcsvfiletodataframe():
   # print('my Dataset path :',datasetFilePath)
    
    #load data to dataframe    
    dataframe=pd.read_csv(datasetFilePath) 
    #print(dataframe)

    #removing unwanted columns
    cleaneddataframe=dataframe.drop(columns=['BreadCrumbs'])
    #print(cleaneddataframe)

    cleaneddataframe=cleaneddataframe.drop(columns=['Description'])
    #print(cleaneddataframe)

    #lower case the capital letters
    cleaneddataframe.columns=cleaneddataframe.columns.str.lower()
    #print(cleaneddataframe)

    #replace space with _
    cleaneddataframe.columns=cleaneddataframe.columns.str.replace(' ','_')
    #print(cleaneddataframe)

    #split the unit from quantity field (created 2 fields using str operation )(indexing)
    cleaneddataframe['qty']=cleaneddataframe['quantity'].str.split(' ').str[0]
    #print(cleaneddataframe)

    cleaneddataframe['unit']=cleaneddataframe['quantity'].str.split(' ').str[1]
    #print(cleaneddataframe)

    #drop the quantity field
    cleaneddataframe=cleaneddataframe.drop(columns=['quantity'])
    #print(cleaneddataframe)

    #find the discount percentage and add to the dataframe as a new column
    cleaneddataframe['discount_percentage']=(cleaneddataframe['price']-cleaneddataframe['discountedprice'])/cleaneddataframe['price']*100
    cleaneddataframe['discount_percentage']=cleaneddataframe['discount_percentage'].round(2)
    print(cleaneddataframe)

    #fixing null values
    cleaneddataframe["brand"].fillna('unknown',inplace=True)
    #print(cleaneddataframe)

    cleaneddataframe['qty'].fillna(0,inplace=True)
    #print(cleaneddataframe)

    cleaneddataframe['unit'].fillna('unknown',inplace=True)
    #print(cleaneddataframe)

    cleaneddataframe['price'].fillna('bfill',inplace=True)
    #print(cleaneddataframe)
    
    cleaneddataframe['discount_percentage'].fillna(0,inplace=True)
    #print(cleaneddataframe)

    cleaneddataframe['discountedprice'].fillna(0,inplace=True)
    #print(cleaneddataframe)

    #drop all rows where name is null
    cleaneddataframe.dropna(subset=['name'],inplace=True)
    #print(cleaneddataframe)

    #create a connection to mysql
    engine=sal.create_engine("mysql+pymysql://root:Gayathri_123@localhost/dmart") 
    conn=engine.connect()

    #load data to MySQL
    cleaneddataframe.to_sql('products',con=conn,index=False,if_exists='replace')

loadcsvfiletodataframe()
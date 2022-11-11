import pandas as pd
from os.path import exists
from datetime import date



def write(newData):
    # Getting date of data upload
    today = date.today()
    newData['Fecha'] = today

    # Update dict
    del newData['sending_data']
    
    data = pd.DataFrame([newData])
    data['Fecha'] = pd.to_datetime(data['Fecha'], dayfirst=True)
    data['Mes']= data['Fecha'].dt.month

    # writing data
    if (exists('database/data.csv')):
        data.to_csv('database/data.csv', mode='a', index=False, header=False)
    else:
        data.to_csv('database/data.csv',index=False)
    
def read(month):
    months = {	
		'Janauary':1,
		'February':2,
		'March':3,
		'April':4,
		'May':5,
		'June':6,
		'July':7,
		'August':8,
		'September':9,
		'October':10,
		'November':11,
		'December':12		}

    # reading data
    data = pd.read_csv('database/data.csv', thousands=',')
    data = data[data.Mes == months[month]]


    
    return data

    


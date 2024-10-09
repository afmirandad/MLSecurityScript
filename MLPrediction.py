import pandas as pd
import matplotlib.pyplot as plt
from pymongo import MongoClient
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from Capture import CapturaDatos

class PrepareData:

    def __init__(self):
        self.listReturned = CapturaDatos()
        self.listData = []

    def prepareJson(self):
        self.listReturned.Captura()
        self.listData = self.listReturned.limpieza()

    def pandasDataPrepared(self):
        df = pd.DataFrame(self.listData,columns=['Year','Quarter','Provider','Income','amountSMS'])
        df['Year'] = pd.to_datetime(df['Year'])
        df['Quarter'] = df['Quarter'].astype('category').cat.codes
        df['Provider'] = df['Provider'].astype('category').cat.codes
        print(df)
        x = df[['Year','Quarter','Provider','amountSMS']]
        y = df['Income']


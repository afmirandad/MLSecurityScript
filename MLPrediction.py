import pandas as pd
import random
import matplotlib.pyplot as plt
from pymongo import MongoClient
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from wheel.macosx_libfile import calculate_macosx_platform_tag

from Capture import CapturaDatos
from MongoClass import MongoClass

class PrepareData:

    def __init__(self):
        self.listReturned = CapturaDatos()
        self.listData = []

    def prepareJson(self):
        self.listReturned.Captura()
        self.listData = self.listReturned.limpieza()

    def storeDataPrepared(self):
        capture = MongoClass()
        print(capture.storeDataMany(self.listData))

    def monthChoise(self,quarter):
        months = {
            1: ['January', 'February', 'March'],
            2: ['April', 'May', 'June'],
            3: ['July', 'August', 'September'],
            4: ['October', 'November', 'December']
        }
        return random.choice(months.get(quarter))

    def pandasDataPrepared(self):
        df = pd.DataFrame(self.listData,columns=['Year','Quarter','Provider','Income','amountSMS'])
        df['Quarter'] = df['Quarter'].astype(int)
        df['Month'] = df['Quarter'].apply(self.monthChoise)
        print(df)


prueba = PrepareData()
prueba.prepareJson()
prueba.pandasDataPrepared()


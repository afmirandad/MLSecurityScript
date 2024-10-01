import requests
import json
from pymongo import MongoClient


class CapturaDatos:
    def __init__(self):
        self.dataJson = []

    def Captura(self):
        resultado_busqueda = requests.get(f"https://www.datos.gov.co/resource/m5pi-7cau.json")
        self.dataJson = resultado_busqueda.json()


    def limpieza(self):
        for ind in range(len(self.dataJson)):
            jsonClean = {
                "Year": "",
                "Quarter": "",
                "Provider": "",
                "Income": ""
            }
            if self.dataJson[ind]['proveedor'] == "ALMACENES EXITO INVERSIONES S.A.S.":
                jsonClean['Provider'] = "MOVIL EXITO"
            elif self.dataJson[ind]['proveedor'] == "AVANTEL S.A.S":
                jsonClean['Provider'] = "WOM"
            elif self.dataJson[ind]['proveedor'] == "VIRGIN MOBILE COLOMBIA S.A.S.":
                jsonClean['Provider'] = "VIRGIN MOBILE"
            elif self.dataJson[ind]['proveedor'] == "SUMA MOVIL S.A.S.":
                jsonClean['Provider'] = "SUMA MOVIL"
            elif self.dataJson[ind]['proveedor'] == "COLOMBIA MOVIL  S.A ESP":
                jsonClean['Provider'] = "CLARO"
            elif self.dataJson[ind]['proveedor'] == "LOGISTICA FLASH COLOMBIA S.A.S":
                jsonClean['Provider'] = "FLASH"
            elif self.dataJson[ind]['proveedor'] == "COMUNICACION CELULAR S A COMCEL S A":
                jsonClean['Provider'] = "CLARO"
            elif self.dataJson[ind]['proveedor'] == "EMPRESA DE TELECOMUNICACIONES DE BOGOTA S.A. ESP":
                jsonClean['Provider'] = "ETB"
            elif self.dataJson[ind]['proveedor'] == "SETROC MOBILE GROUP SAS":
                jsonClean['Provider'] = "SETROC"
            elif self.dataJson[ind]['proveedor'] == "PARTNERS TELECOM COLOMBIA SAS":
                jsonClean['Provider'] = "PARTNERS"
            elif self.dataJson[ind]['proveedor'] == "LIWA SAS ESP":
                jsonClean['Provider'] = "LIWA"
            elif self.dataJson[ind]['proveedor'] == "LOV TELECOMUNICACIONES SAS":
                jsonClean['Provider'] = "LOV"
            elif self.dataJson[ind]['proveedor'] == "UFF MOVIL SAS":
                jsonClean['Provider'] = "UFF"
            elif self.dataJson[ind]['proveedor'] == "COLOMBIA TELECOMUNICACIONES S.A. E.S.P.":
                jsonClean['Provider'] = "MOVISTAR"
            jsonClean['Year'] = self.dataJson[ind]['anno']
            jsonClean['Quarter'] = self.dataJson[ind]['trimestre']
            jsonClean['Income'] = self.dataJson[ind]['ingresos_por_mensajes']
            print(jsonClean)

    #def guardar_en_db(self, datos):
    #self.collection.insert_one(datos)
    #print(f"Datos guardados en MongoDB: {datos}")


prueba = CapturaDatos()
prueba.Captura()
prueba.limpieza()
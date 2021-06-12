# coding: UTF-8

import requests                 # install requests 
import manageData               # データベースをいじるクラス


class LoadData:
    def __init__(self, fileName):
        print (f"DB file is {fileName}")
        self.fileName = fileName
    
    def selectData(self, hourData, minuteData):
            manageDB = manageData.ManageData(self.fileName)
            return manageDB.selectAllData(hourData, minuteData)
            
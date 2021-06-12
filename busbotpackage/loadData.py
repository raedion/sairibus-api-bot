# coding: UTF-8

import requests                 # install requests 
import manageData               # データベースをいじるクラス


class LoadData:
    def __init__(self, fileName):
        self.fileName = fileName
    
    def selectData(self, hourData, minuteData):
            manageDB = manageData.ManageData(self.fileName)
            loadData = manageDB.selectAllData(hourData, minuteData)
            return "本日の再履バスは終了しました！" if loadData == "" else loadData
            
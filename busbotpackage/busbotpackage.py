# coding: UTF-8

from enum import Enum
import manageData
import analyzeHTML

fileName = 'timetable/20210611.db'
# fileName = 'timetable/20210531.db'

class Station(Enum):
    TOYONAKA = 0
    MINO = 1
    SUITA = 2

# DBはtimetableフォルダ直下のファイル. 作成日時を名前に採用. 

# 時間を指定してその時間に対応するデータを取得
def loadTime(hourData, minuteData):
    # DateData.toString()
    a = manageData.ManageData(fileName, "timetable")
    # a.createDataTable()
    # a.addData(6,10)
    a.selectData(0,0)

def selectData():
    print("")

def getResult():
    analyzer = analyzeHTML.AnalyzeHTML()
    analyzer.getElement()

getResult()
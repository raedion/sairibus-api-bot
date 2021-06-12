# coding: UTF-8

from enum import Enum
import analyzeHTML

fileName = 'timetable/20210611.db'
# fileName = 'timetable/20210531.db'

class Station(Enum):
    TOYONAKA = 0
    MINO = 1
    CONVENTION = 2
    JINKA = 3
    TECH = 4

# DBはtimetableフォルダ直下のファイル. 作成日時を名前に採用. 

# 時間を指定してその時間に対応するデータを取得
def loadTime(hourData, minuteData):
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
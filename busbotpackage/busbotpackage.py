# coding: UTF-8

import analyzeHTML
import loadData
import datetime                                         # 現在時刻を取得するために利用
import re

fileName = 'timetable/20210611.db'
# fileName = 'timetable/20210531.db'

# DBはtimetableフォルダ直下のファイル. 作成日時を名前に採用. 

# 時間を指定してその時間に対応するデータを取得
def loadTime(msg = None):
    hourData = 0
    minuteData = 0
    if msg is None:
        dt_now = datetime.datetime.now()
        hourData = dt_now.hour
        minuteData = dt_now.minute
    else:
        val = re.match(r'([0-9]{2}):([0-9]{2})', msg)
        if val is None:
            dt_now = datetime.datetime.now()
            hourData = dt_now.hour
            minuteData = dt_now.minute     
        else:
            hourData = int(val[1])
            minuteData = int(val[2])
    loader = loadData.LoadData(fileName)
    returnVal = f"時刻[{hourData:02}:{minuteData:02}]の直近に発車するバスの時間は以下の通りです\n"
    returnVal = returnVal + loader.selectData(hourData, minuteData)
    return returnVal

def renewData():
    analyzer = analyzeHTML.AnalyzeHTML(fileName)
    analyzer.getElement()

def main():
    print(renewData())

if __name__ == '__main__':
    main()
# coding: UTF-8

import analyzeHTML
import loadData
import datetime                                         # 現在時刻を取得するために利用

fileName = 'timetable/20210611.db'
# fileName = 'timetable/20210531.db'

# DBはtimetableフォルダ直下のファイル. 作成日時を名前に採用. 

# 時間を指定してその時間に対応するデータを取得
def loadTime():
    loader = loadData.LoadData(fileName)
    dt_now = datetime.datetime.now()
    returnVal = f"時刻[{dt_now.hour:02}:{dt_now.minute:02}]の直近に発車するバスの時間は以下の通りです\n"
    returnVal = returnVal + loader.selectData(dt_now.hour, dt_now.minute)
    return returnVal

def renewData():
    analyzer = analyzeHTML.AnalyzeHTML(fileName)
    analyzer.getElement()

def main():
    print(loadTime())

if __name__ == '__main__':
    main()
# coding: UTF-8

import analyzeHTML

fileName = 'timetable/20210611.db'
# fileName = 'timetable/20210531.db'

# DBはtimetableフォルダ直下のファイル. 作成日時を名前に採用. 

# 時間を指定してその時間に対応するデータを取得
def loadTime(hourData, minuteData):
    a = manageData.ManageData(fileName, "timetable")
    # a.createDataTable()
    # a.addData(6,10)
    a.selectData(0,0)

def selectData():
    print("")

def main():
    # analyzer = analyzeHTML.AnalyzeHTML(fileName)
    # analyzer.getElement()
    

if __name__ == '__main__':
    main()
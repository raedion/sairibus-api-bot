# coding: UTF-8

import sqlite3
import os

class ManageData:
    fileName = ""
    tableName = "timetable"
    def __init__(self):
        self.fileName = ""
    def __init__(self, fileName):
        self.fileName = fileName
    def __init__(self, fileName, tableName):
        self.fileName = fileName
        self.tableName = tableName

    def toString():
        print (f"{hourData}:{minuteData}")
    
    # データベースを新規作成するメソッド
    def createDataTable(self):
        if not os.path.exists(self.fileName):
            print ("There is no DB file")
            f = open(self.fileName, 'w')
            f.write('')
            f.close()
        conn = sqlite3.connect(self.fileName)
        c = conn.cursor()
        c.execute(f"CREATE TABLE {self.tableName} (id integer primary key autoincrement, start integer, end integer, departure_h integer, departure_m integer)")
        conn.commit()
        conn.close()

    # データを新しく追加するメソッド
    def addData(self, hourData, minuteData):
        conn = sqlite3.connect(self.fileName)
        c = conn.cursor()
        c.execute(f"INSERT INTO {self.tableName} (start, end, departure_h, departure_m) VALUES (0, 2, {hourData} ,{minuteData})")
        c.execute(f"INSERT INTO {self.tableName} (start, end, departure_h, departure_m) VALUES (0, 2, {hourData + 1} ,{minuteData})")
        conn.commit()
        conn.close()
    
    def addDatas(self):
        conn = sqlite3.connect(self.fileName)
        c = conn.cursor()
        c.execute(f"INSERT INTO {self.tableName} (start, end, departure_h, departure_m) VALUES (0, 2, {hourData} ,{minuteData})")
        c.execute(f"INSERT INTO {self.tableName} (start, end, departure_h, departure_m) VALUES (0, 2, {hourData + 1} ,{minuteData})")
        conn.commit()
        conn.close()


    # データを選択するメソッド
    def selectData(self, hourData, minuteData):
        conn = sqlite3.connect(self.fileName)
        c = conn.cursor()
        for result in c.execute(f"select * from {self.tableName} where departure_h >= {hourData} and departure_m >= {minuteData}"):
            print(result)
        conn.commit()
        conn.close()
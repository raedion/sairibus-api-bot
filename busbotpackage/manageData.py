# coding: UTF-8

import sqlite3
import os
from enum import Enum

class ManageData:
    class Station(Enum):
        TOYONAKA = 0
        MINO = 1
        CONVENTION = 2
        JINKA = 3
        TECH = 4
    fileName = ""
    tableName = "timetable"
    def __init__(self):
        self.fileName = ""
    def __init__(self, fileName):
        self.fileName = fileName

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
        c.execute(f"CREATE TABLE t2s (ID integer primary key autoincrement, TOYONAKA_h integer, TOYONAKA_m integer, MINO_h integer, MINO_m integer, CONVENTION_h integer, CONVENTION_m integer, TECH_h integer, TECH_m integer)")
        c.execute(f"CREATE TABLE s2t (ID integer primary key autoincrement, TECH_h integer, TECH_m integer, CONVENTION_h integer, JINKA_h integer, JINKA_m integer, MINO_h integer, MINO_m integer, TOYONAKA_h integer, TOYONAKA_m integer)")
        conn.commit()
        conn.close()


    # データを新しく追加するメソッド
    def addData(self, data, tableName):
        L = []
        V = []
        for e in data:
            L.append(self.Station(e[0]).name + "_h")
            L.append(self.Station(e[0]).name + "_m")
            V.append(str(e[1][0]))
            V.append(str(e[1][1]))
        if len(L) == 0:
            return
        # print (f"INSERT INTO t2s ({', '.join(L)}) VALUES ({', '.join(V)})")
        conn = sqlite3.connect(self.fileName)
        c = conn.cursor()
        c.execute(f"INSERT INTO {tableName} ({', '.join(L)}) VALUES ({', '.join(V)})")
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
# coding: UTF-8

import sqlite3
import os
from enum import Enum

class ManageData:
    # https://docs.python.org/ja/3/library/enum.html
    class Station(Enum):
        TOYONAKA = 0
        MINO = 1
        CONVENTION = 2
        JINKA = 3
        TECH = 4
        def __str__(self):
            if self.value == 0:
                return "豊中"
            elif self.value == 1:
                return "箕面"
            elif self.value == 2:
                return "コンベンション前"
            elif self.value == 3:
                return "人間科学部前"
            elif self.value == 4:
                return "工学部前"

    fileName = ""
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

    # データを選択するメソッド
    def selectData(self, hourData, minuteData, start, end):
        tableName = "t2s" if start.value < end.value else "s2t"
        try:

            conn = sqlite3.connect(self.fileName)
            c = conn.cursor()
            for result in c.execute(self.createSelectQuery(
                hourData, minuteData, tableName, start.name, end.name)):
                print (f"- {str(start)}({result[0]:02}:{result[1]:02}) -> {str(end)}({result[2]:02}:{result[3]:02})")
                break
            conn.commit()
            conn.close()
        except sqlite3.OperationalError as e:   # 何らかの原因でデータベースにアクセスできない時
            print(e)                            # ログに出力

    def selectAllData(self, hourData, minuteData):
        self.selectData(hourData, minuteData, self.Station.TOYONAKA, self.Station.MINO)
        self.selectData(hourData, minuteData, self.Station.TOYONAKA, self.Station.CONVENTION)
        self.selectData(hourData, minuteData, self.Station.TOYONAKA, self.Station.TECH)
        self.selectData(hourData, minuteData, self.Station.MINO, self.Station.TOYONAKA)
        self.selectData(hourData, minuteData, self.Station.MINO, self.Station.CONVENTION)
        self.selectData(hourData, minuteData, self.Station.MINO, self.Station.TECH)
        self.selectData(hourData, minuteData, self.Station.TECH, self.Station.MINO)
        self.selectData(hourData, minuteData, self.Station.TECH, self.Station.TOYONAKA)

    def createSelectQuery(self, hourData, minuteData, tableName, start, end):
        return f"SELECT ifnull({start}_h, -1), ifnull({start}_m, -1), ifnull({end}_h, -1), ifnull({end}_m, -1) FROM {tableName} WHERE ({start}_h == {hourData} and {start}_m >= {minuteData}) or ({start}_h > {hourData})"
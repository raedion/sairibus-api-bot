# coding: UTF-8

# https://codezine.jp/article/detail/12230
# https://naruport.com/blog/2019/12/9/bs4-class/#class_%E3%82%92%E6%8C%87%E5%AE%9A%E3%81%97%E3%81%A6%E8%A6%81%E7%B4%A0%E3%82%92%E5%8F%96%E5%BE%97%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95

from bs4 import BeautifulSoup   # install beautifulsoup4
import requests                 # install requests 
import re
import manageData

class AnalyzeHTML:
    siteName = "https://www.osaka-u.ac.jp/ja/access/bus.html"
    fileName = ""
    def __init__(self, fileName):
        print (f"DB file is {fileName}")
        self.fileName = fileName
    
    def addDataToDB(self, dataContent, positionArr, tableName):
        pattern = re.compile(r'－|([0-9]{1,2})：([0-9]{1,2})')        # パターンマッチで内部の文字列が時間情報か確認
        for tr_element in dataContent.find_all("tr"):         # タップルを読み込み
            for td_element in tr_element.find_all("td"):
                matchedResult = pattern.match(td_element.text)
                if type(matchedResult) is re.Match:     
                    msg = matchedResult.group()
                    if matchedResult.group() != "－":
                        result = self.convData(matchedResult.groups())


    # 時間情報を数値データに変更する
    def convData(self, str):
        return [int(str[0]), int(str[1])]

    # データベースを新規作成するメソッド
    def getElement(self):
        html = requests.get(self.siteName)                      # サイトを指定  
        soup = BeautifulSoup(html.content, "html.parser")       # 構文解析 
        dataTables = soup.find_all(class_="dataTable")          # テーブルを取得

        self.addDataToDB(dataTables[0], [0,1,2,4], "t2s")                         # テーブルに処理実行(豊中 -> 吹田)
        self.addDataToDB(dataTables[1], [4,3,1,0], "s2t")                         # テーブルに処理実行(吹田 -> 豊中)
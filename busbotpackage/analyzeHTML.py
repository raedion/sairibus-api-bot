# coding: UTF-8

# https://codezine.jp/article/detail/12230
# https://naruport.com/blog/2019/12/9/bs4-class/#class_%E3%82%92%E6%8C%87%E5%AE%9A%E3%81%97%E3%81%A6%E8%A6%81%E7%B4%A0%E3%82%92%E5%8F%96%E5%BE%97%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95

from bs4 import BeautifulSoup   # install beautifulsoup4
import requests                 # install requests 
import re

class AnalyzeHTML:
    siteName = "https://www.osaka-u.ac.jp/ja/access/bus.html"
    def __init__(self):
        print ("analyze call")
    
    # def toString():
        # print (f"{hourData}:{minuteData}")
    
    # データベースを新規作成するメソッド
    def getElement(self):
        pattern = re.compile("－|[0-9]{1,2}：[0-9]{1,2}")        # パターンマッチで内部の文字列が時間情報か確認
        html = requests.get(self.siteName)                      # サイトを指定  
        soup = BeautifulSoup(html.content, "html.parser")       # 構文解析 
        dataTables = soup.find_all(class_="dataTable")          # テーブルを取得
        for dataTable in dataTables:                            # 各テーブル内に処理実行(第一ループ: 豊中 -> 吹田, 第二ループ: 吹田 -> 豊中)
            for tr_element in dataTable.find_all("tr"):         # タップルを読み込み
                print ("----------------")
                for td_element in tr_element.find_all("td"):
                    a = pattern.match(td_element.text)
                    if type(a) is re.Match:     
                        print(a.group())
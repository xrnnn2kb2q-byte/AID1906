"""
練習： 將單詞本存入數據庫
1.創建數據庫 dict    (utf8)
2.創建數據表 words   將單詞和單詞解釋分別存入不同的字典
3.將單詞存入words單詞表 超過19500 即可
"""
import pymysql
import re

db = pymysql.connect(host= 'localhost',
                     port= 3306,
                     password="asd3140293",
                     database="dict",
                     charset='utf8')
cur = db.cursor()
sql = "insert into words(word,mean) values(%s,%s)"

with open("dict.txt","r") as f:
    for line in f:
        tup = re.findall(r"(\S+)\s+(.*)",line)[0]
        try:
            cur.execute(sql,tup)
            db.commit()
        except:
            db.rollback()

cur.close()
db.close()
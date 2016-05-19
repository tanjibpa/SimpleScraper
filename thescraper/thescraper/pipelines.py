import os
import sqlite3
from django.utils.dateparse import parse_datetime

conn = None
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class ThescraperPipeline(object):
    def __init__(self):
        self.setupDBCon()

    def setupDBCon(self):
        self.conn = sqlite3.connect(os.path.join(BASE_DIR, 'scraper/db.sqlite3'))
        self.cur = self.conn.cursor()

    def checkDB(self, data_fullname):
        self.cur.execute("""SELECT * FROM scrapeapp_redditlinks WHERE data_fullname = (?)""", (data_fullname,))
        item_exist = self.cur.fetchone()
        if item_exist:
            return True
        else:
            False

    def storeInDB(self, item):
        if not self.checkDB(item['data_fullname']):
            self.cur.execute("""INSERT INTO scrapeapp_redditlinks(title_text, link, pub_date, data_fullname) VALUES(?, ?, ?, ?)""",
                             (item['title_text'], item['link'], parse_datetime(item['pub_date']), item['data_fullname']))
            print '-----------------------'
            print 'Data stored in database'
            print '.......................'
            self.conn.commit()

    def closeDB(self):
        self.conn.close()

    def __del__(self):
        self.closeDB()

    def process_item(self, item, spider):
        self.storeInDB(item)
        return item

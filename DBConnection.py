import mysql.connector
from datetime import datetime


class DBConnection:
    def __init__(self):
        self.con = mysql.connector.connect(user='test', password='test',
                                           host='127.0.0.1', database='quiz')

    def check_user(self, username):
        cursor = self.con.cursor()
        query = "SELECT * FROM users WHERE username=%s"
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        cursor.close()
        return result

    def save_score(self, userid, score):
        today = datetime.now()
        print(today)
        cursor = self.con.cursor()
        query = "INSERT INTO scores (users_id, date_recorded, score) VALUES (%s, %s, %s)"
        cursor.execute(query, (userid, str(today), score))
        cursor.close()
        self.con.commit()


if __name__ == '__main__':
    db = DBConnection()
    print(db.check_user('aaa'))  # True
    print(db.check_user('zzz'))  # False

    db.save_score(1, 10)


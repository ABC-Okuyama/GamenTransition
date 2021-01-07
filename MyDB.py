import psycopg2

# psycopg2
# Postgresql用のPythonのDB用ドライバ実装、psycopg2を使うと以下のような見た目のコードになる
# Basic module usage — Psycopg 2.6 documentation

class MyDB:

    # Postgres用接続文字列　(ユーザ名、パスワード)
    userName = 'koh'
    passWord = 'password'

    # Constructor
    # 接続文字列を使って、DBに接続 (user=xx dbname=xx password=xx) の形式
    def __init__(self, dbName):
        self.conn = psycopg2.connect(" user=" + MyDB.userName + " dbname=" + dbName + " password=" + MyDB.passWord)


    # SQL文の実行 (パラメータなし)
    def query(self, sqlStatement):
        # excexute sql
        self.cur = self.conn.cursor()
        self.cur.execute(sqlStatement)
        results = self.cur.fetchall()
        self.cur.close()
        return results # 結果を返す


    # DBのクローズ
    def close(self):
        self.conn.close()


    # 著者テーブルに追加
    def insertAuthor(self, author):
        self.cur = self.conn.cursor()
        self.cur.execute("insert into author_table (author_name) values (%s);", (author,))
        self.conn.commit() # commit忘れずに


    # ジャンルテーブルに追加
    def insertGenre(self, code, genre):
        self.cur = self.conn.cursor()
        self.cur.execute("insert into genre_table (g_code,g_name) values (%s,%s);", (code,genre))
        self.conn.commit() # commit忘れずに


    # 書籍テーブルに追加
    def insertBook(self, book, g_code, a_id ):
        self.cur = self.conn.cursor()
        self.cur.execute("insert into book_table ( b_name, g_code, a_id ) values (%s,%s,%s);", (book, g_code, a_id))
        self.conn.commit() # commit忘れずに


    # 著者テーブルを更新 (a_idを指定して、そのa_idの著者名を変更する)
    def updateAuthor(self, a_id, author):
        self.cur = self.conn.cursor()
        self.cur.execute("update author_table set author_name = %s where a_id = %s;", (author,a_id))
        self.conn.commit() # commit忘れずに


    # ジャンルテーブルを更新 (g_codeを指定して、そのg_codeの行を削除する)
    def deleteGenre(self, g_code):
        self.cur = self.conn.cursor()
        self.cur.execute("delete from genre_table where g_code = %s;", (g_code,))
        self.conn.commit() # commit忘れずに


# SQLに対するヒント
#
# >>> cur.execute(
# ...     "INSERT INTO some_table (an_int, a_date, a_string)
# ...         VALUES (%s, %s, %s);”,
# ...     (10, datetime.date(2005, 11, 18), "O'Reilly"))
# ・cur（カーソル）はJavaとかC++でいうところのstatementとかpreparedstatementにあたるやつ
# ・注目はVALUES (%s, %s, %s)、なんとフォーマット記述子である

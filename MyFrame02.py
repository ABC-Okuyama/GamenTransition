from MyDB import MyDB
import tkinter as tk
from tkinter import ttk


class MyFrama02(ttk.Frame):

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        # Load Data from Database
        self.results = self.load_Data()

        # Buttonを作る
        back_button = ttk.Button(self, text="メニューに戻る")
        # 任意の名前の仮想イベントを作成しておく
        back_button["command"] = lambda: self.event_generate("<<Page_Back>>")

        # 下地のframe: frBoxを作る
        self.frBox = tk.Frame(self)

        # 下地のfrBoxにTreeViewをセットアップする
        self.setup_treeView()

        # frBoxを配置
        self.frBox.pack()

        # Buttonを配置 (bottomに)
        back_button.pack(side="bottom")


    # TreeViewのセットアップ
    def setup_treeView(self):

        # TreeView (ListBox)
        self.tree = ttk.Treeview(self.frBox)
        # 列を作成（4列）
        self.tree["columns"] = ('ID', 'title', 'genre', 'author')
        # ヘッダーの設定    tree.column(2,width=100)
        self.tree["show"] = "headings"
        self.tree.heading('ID', text="ID")
        self.tree.heading('title', text="タイトル")
        self.tree.heading('genre', text="ジャンル")
        self.tree.heading('author', text="作者")
        # 各列の幅設定
        self.tree.column('ID', width=50)
        self.tree.column('title', width=100)
        self.tree.column('genre', width=100)
        self.tree.column('author',width=100)

        # Scrollbarを作る
        self.scrollbar = ttk.Scrollbar(
            self.frBox,
            orient=tk.VERTICAL,
            command=self.tree.yview)
        self.tree['yscrollcommand'] = self.scrollbar.set

        # 表にデータを入れる
        for i in range(len(self.results)):
            rec = self.results[i]
            self.tree.insert("", "end", values=(rec[0], rec[1], rec[2], rec[3]))

        # TreeView
        # 項目を選択したら、on_tree_select()が呼ばれるようにする
        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

        # TreeViewとScrollView配置
        self.tree.pack(side=tk.LEFT, fill=tk.Y)
        self.scrollbar.pack(side=tk.LEFT, fill=tk.Y)


    # TreeView 項目選択された時の処理
    def on_tree_select(self, event):
        print("selected items:")
        for item in self.tree.selection():
            print(self.tree.item(item)['values'])  # for Debug


    # データベースからデータをロード
    def load_Data(self):
        # Connect DataBase ('MyLibrary')
        myDB = MyDB('MyLibrary')

        # DB Query Execute
        results = myDB.query('SELECT b_id, b_name, genre_table.g_name, author_table.author_name ' \
                             'FROM book_table, genre_table, author_table ' \
                             'where book_table.g_code = genre_table.g_code and ' \
                             'book_table.a_id = author_table.a_id;')
        # Close DataBase
        myDB.close()

        return results      # 検索結果を返す
from MyDB import MyDB
import tkinter as tk
from tkinter import ttk


class MyFrame03(ttk.Frame):

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

        # Frameを配置
        self.frBox.pack()
        # Buttonを配置
        back_button.pack(side="bottom")


    # TreeViewのセットアップ
    def setup_treeView(self):

        # TreeView (ListBox)
        self.tree = ttk.Treeview(self.frBox)
        # 列を作成（4列）
        self.tree["columns"] = ('ID', 'author')
        # ヘッダーの設定    tree.column(2,width=100)
        self.tree["show"] = "headings"
        self.tree.heading('ID', text="ID")
        self.tree.heading('author', text="作者")
        # 各列の幅設定
        self.tree.column('ID', width=50)
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
            self.tree.insert("", "end", values=(rec[0], rec[1]))

        # TreeView
        # 項目を選択したら、on_tree_select()が呼ばれるようにする
        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

        # TreeViewとScrollView配置
        self.tree.pack(side="left", fill="y")
        self.scrollbar.pack(side="left", fill="y")


    # TreeView 項目選択された時の処理
    def on_tree_select(self,event):
        print("selected items:")
        for item in self.tree.selection():
            print(self.tree.item(item)['values'])  # for Debug


    # データベースからデータをロード
    def load_Data(self):
        # Connect DataBase ('MyLibrary')
        myDB = MyDB('MyLibrary')

        # DB Query Execute
        results = myDB.query('SELECT a_id, author_name ' \
                             'FROM author_table order by 1;')
        # Close DataBase
        myDB.close()

        return results  # 検索結果を返す

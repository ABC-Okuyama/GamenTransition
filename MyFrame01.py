
import tkinter as tk
from tkinter import ttk


class MyFrama01(ttk.Frame):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        # グリッドを使ってレイアウト
        self.grid_rowconfigure(0, weight=1)

        # ボタンを3つ作る
        book_button = ttk.Button(self, text="書籍一覧",  width=20)
        author_button = ttk.Button(self, text="作者一覧", width=20)
        exit_button = ttk.Button(self, text="アプリ終了", width=20)

        # 任意の名前の仮想イベントを作成しておく
        book_button["command"] = lambda: self.event_generate("<<Page_Home>>")
        author_button["command"] = lambda: self.event_generate("<<Page_Back>>")
        exit_button["command"] = lambda: self.event_generate("<<Page_Exit>>")

        # Labelを作成して 0行目、0列目 (3列分の大きさ)
        tk.Label(self, text="メニューのページ", font=("", 30)).grid(row=0, column=0, columnspan=3)
        # ボタンを配置 1行目、0列目、1列目、2列目
        author_button.grid(row=1, column=0)
        book_button.grid(row=1, column=1)
        exit_button.grid(row=1, column=2)
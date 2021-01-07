# Original
# https://repl.it/@MiKLTea/tkStackedFrame#sample.py
# Arranged by K.O.

import tkinter as tk
from tkinter import ttk

# Frameを管理するクラス
class LayeredFrame(ttk.Frame):

    # Constructor
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        self._pages = {}        # ページに名前を付けて覚えておくぞ
        self._current = None    # 最初は何にもなし
        self.grid_rowconfigure(0, weight=1)     # Grid 横 (1)
        self.grid_columnconfigure(0, weight=1)  # Grid 縦 (1)


    # 現在のページを返す
    @property
    def currentPage(self):
        return self._pages.get(self._current, None)


    # 現在のページ名を返す
    @property
    def currentPageName(self):
        return self._current


    # ページの追加 ページ, ページ名
    def addPage(self, page, name):
        assert not name in self._pages
        self._pages[name] = page
        self._current = name
        page.grid(row=0, column=0, sticky=tk.NSEW)


    # ページの削除  ページ名
    def removePage(self, name):
        if name in self._pages:
            del self._pages[name]
        if name == self._current:
            self._current = None


    # ページの変更  ページ名を指定する
    # 以下参照
    # Tkinterによる複数の画面（フレーム）をボタン操作で切り替えて表示させる（画面遷移）方法
    # https://office54.net/python/tkinter/screen-change-tkraise
    def changePage(self, name):
        page = self._pages.get(name, None)
        if page:
            self._current = name
            # 一番前面に表示する
            page.tkraise()
            # ページが変更されたことを通知する仮想イベント
            self.event_generate("<<StackedFrame_PageChanged>>")


    # ページ名を指定してページに遷移する(関数を実行する)
    def toPage(self, name):
        # イベントと結びつけるためのコールバックを実行して返す
        return lambda event=None: self.changePage(name)

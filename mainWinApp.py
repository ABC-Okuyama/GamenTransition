import tkinter as tk
from LayeredFrame import LayeredFrame
from MyFrame01 import MyFrama01
from MyFrame02 import MyFrama02
from MyFrame03 import MyFrame03

# アプリケーションクラスだよ
class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        # Windowの大きさを指定
        self.master.geometry("600x400")
        self.create_windows()


    # Window の設定
    def create_windows(self):
        # master=rootの上に frameを構築する
        # frame に対して複数のページを登録する
        layered_frame = LayeredFrame(self.master)

        # frameのレイアウトを設定
        # 以下 参照のこと
        # https://www.shido.info/py/tkinter2.html
        layered_frame.pack(fill=tk.BOTH, expand=True)

        # root.main_loopの中で
        # frame.changePage()を呼び出すようにする
        # 最初に page1 の表示をするように
        self.master.after_idle(layered_frame.changePage, "page1")

        # frameに onPageChanged をくっつける
        # 仮想イベント<<StackedFrame_PageChanged>>が発生したら、onPageChaneged()が呼ばれる
        layered_frame.bind("<<StackedFrame_PageChanged>>", self.onPageChanged)

        # page1 はMyFrame01クラスのインスタンスを作り、追加
        page1 = MyFrama01(layered_frame)
        # 第1引数:仮想イベントと 第2引数:処理  を結びつける(bindする)
        page1.bind("<<Page_Back>>", layered_frame.toPage("page3"))
        page1.bind("<<Page_Home>>", layered_frame.toPage("page2"))
        page1.bind("<<Page_Exit>>", lambda _: self.master.quit())  # アプリ終了

        # frameに page1を 追加
        layered_frame.addPage(page1, "page1")

        # page2 は MyFrame02クラスのインスタンスを作る
        page2 = MyFrama02(layered_frame)
        page2.bind("<<Page_Back>>", layered_frame.toPage("page1"))

        # frameに page2を 追加
        layered_frame.addPage(page2, "page2")

        # page3 は MyFrame03クラスのインスタンスを作る
        page3 = MyFrame03(layered_frame)
        page3.bind("<<Page_Back>>", layered_frame.toPage("page1"))

        # frameに page3を 追加
        layered_frame.addPage(page3, "page3")


    # pageが変わったら呼ばれる
    def onPageChanged(self, event):
        if isinstance(event.widget, LayeredFrame):
            name = event.widget.currentPageName
            print("PageChanged", name)      # for Debug
            self.master.title(name)


    def callBack(self):
        pass        # 使わないかも pass


# main() だよ
def main():
    root = tk.Tk()
    app = Application(master=root)  # Inherit
    app.mainloop()


# Startup EntryPoint
if __name__ == "__main__":
    main()

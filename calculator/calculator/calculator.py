from main import tk
from stack import STACK
from queue import QUEUE

ButtonSize = 50
DisplayWidth  = ButtonSize * 4
DisplayHeight = ButtonSize * 6

"""
渡された文字が計算記号かの確認
"""
def CalculationSymbol_Check(text):
    if text == "＋":
        return True
    elif text == "－":
        return True
    elif text == "×":
        return True
    elif text == "÷":
        return True
    else:
        return False

"""
スタックから値をキューに格納
"""
def CollectNumber(stock, queue):
    # すべての文字を読み込んだ後の処理
    tmp = ""
    # 計算記号が来るまで，数値を取り出す
    while True:
        if CalculationSymbol_Check(stock.check(-1)):
            break
        if stock.check(-1) == None:
            break
        else:
            tmp += stock.pop()
    queue.enqueue(tmp[::-1])

"""
演算子の優先順位を返す
"""
def rank(text):
    if text == "＋" or text == "－":
        return 2
    elif text == "×" or text == "÷":
        return 1
    # 数値の場合
    else:
        return 0

"""
中置記法を逆ポーランド記法に変換
"""
def Convert_RPN(text):
    q = QUEUE()
    s = STACK()
    
    # 先頭から順に文字を確認
    for i in range (0, len(text)):
        # 計算記号の場合
        if CalculationSymbol_Check(text[i]):
            while rank(text[i]) >= rank(s.check(-1)) and s.check(-1) != None:
                # 数値の場合，読み取った値をキューに格納
                if rank(s.check(-1)) == 0:
                    CollectNumber(s, q)
                # 計算記号の場合，そのままキューに格納
                else:
                    q.enqueue(s.pop())
        # 読み取った文字を格納
        s.push(text[i])
    # 最後に読み取った値をキューに格納
    CollectNumber(s, q)

    # スタックに残った計算記号をキューに格納
    while s.check(-1) != None:
        q.enqueue(s.pop())
    return q

"""
与えられた逆ポーランド記法の式を計算する
"""
def calculation(queue):
    s = STACK()

    while queue.check(0) != None:
        # 数値の場合
        if rank(queue.check(0)) == 0:
            s.push(queue.dequeue())
        # 演算子の場合
        else:
            CS = queue.dequeue()
            if CS == "＋":
                value1 = float(s.pop())
                value2 = float(s.pop())
                s.push(str(value2 + value1))
            if CS == "－":
                value1 = float(s.pop())
                value2 = float(s.pop())
                s.push(str(value2 - value1))
            if CS == "×":
                value1 = float(s.pop())
                value2 = float(s.pop())
                s.push(str(value2 * value1))
            if CS == "÷":
                value1 = float(s.pop())
                value2 = float(s.pop())
                s.push(str(value2 / value1))
    return s.pop()

"""
電卓クラス
"""
class CALCULATOR(tk.Frame):
    # コンストラクタ
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        # フォントの設定
        master.option_add("*font", ["MS Pゴシック", 22])
        # ウィンドウサイズを固定
        master.resizable(width = False, height = False)
        # ウィンドウの設定
        master.minsize(DisplayWidth, DisplayHeight)
        master.title("電卓")
        # 表示テキスト
        self.DisplayText = "0"
        # ディスプレイ・ボタンの設定
        self.createCanvas()
        self.createButton()

    # ボタンの設定
    def createButton(self):
        # ボタンの配置
        tk.Button(self.master, text = "AC", command = self.AllClear,                compound = tk.CENTER, bg = "gray"  , fg = "black").place(x =   0, y =  50, width = ButtonSize,     height = ButtonSize)
        tk.Button(self.master, text = "＝", command = self.calc,                    compound = tk.CENTER, bg = "orange", fg = "white").place(x = 150, y = 250, width = ButtonSize,     height = ButtonSize)
        tk.Button(self.master, text = "＋", command = lambda:self.ButtonClick("＋"), compound = tk.CENTER, bg = "orange", fg = "white").place(x = 150, y = 200, width = ButtonSize,     height = ButtonSize)
        tk.Button(self.master, text = "－", command = lambda:self.ButtonClick("－"), compound = tk.CENTER, bg = "orange", fg = "white").place(x = 150, y = 150, width = ButtonSize,     height = ButtonSize)
        tk.Button(self.master, text = "×", command = lambda:self.ButtonClick("×"), compound = tk.CENTER, bg = "orange", fg = "white").place(x = 150, y = 100, width = ButtonSize,     height = ButtonSize)
        tk.Button(self.master, text = "÷", command = lambda:self.ButtonClick("÷"), compound = tk.CENTER, bg = "orange", fg = "white").place(x = 150, y =  50, width = ButtonSize,     height = ButtonSize)
        tk.Button(self.master, text = "０", command = lambda:self.ButtonClick(0),    compound = tk.CENTER, bg = "gray"  , fg = "white").place(x =   0, y = 250, width = ButtonSize * 2, height = ButtonSize)
        tk.Button(self.master, text = "１", command = lambda:self.ButtonClick(1),    compound = tk.CENTER, bg = "gray"  , fg = "white").place(x =   0, y = 200, width = ButtonSize,     height = ButtonSize)
        tk.Button(self.master, text = "２", command = lambda:self.ButtonClick(2),    compound = tk.CENTER, bg = "gray"  , fg = "white").place(x =  50, y = 200, width = ButtonSize,     height = ButtonSize)
        tk.Button(self.master, text = "３", command = lambda:self.ButtonClick(3),    compound = tk.CENTER, bg = "gray"  , fg = "white").place(x = 100, y = 200, width = ButtonSize,     height = ButtonSize)
        tk.Button(self.master, text = "４", command = lambda:self.ButtonClick(4),    compound = tk.CENTER, bg = "gray"  , fg = "white").place(x =   0, y = 150, width = ButtonSize,     height = ButtonSize)
        tk.Button(self.master, text = "５", command = lambda:self.ButtonClick(5),    compound = tk.CENTER, bg = "gray"  , fg = "white").place(x =  50, y = 150, width = ButtonSize,     height = ButtonSize)
        tk.Button(self.master, text = "６", command = lambda:self.ButtonClick(6),    compound = tk.CENTER, bg = "gray"  , fg = "white").place(x = 100, y = 150, width = ButtonSize,     height = ButtonSize)
        tk.Button(self.master, text = "７", command = lambda:self.ButtonClick(7),    compound = tk.CENTER, bg = "gray"  , fg = "white").place(x =   0, y = 100, width = ButtonSize,     height = ButtonSize)
        tk.Button(self.master, text = "８", command = lambda:self.ButtonClick(8),    compound = tk.CENTER, bg = "gray"  , fg = "white").place(x =  50, y = 100, width = ButtonSize,     height = ButtonSize)
        tk.Button(self.master, text = "９", command = lambda:self.ButtonClick(9),    compound = tk.CENTER, bg = "gray"  , fg = "white").place(x = 100, y = 100, width = ButtonSize,     height = ButtonSize)
        tk.Button(self.master, text = "",   command = lambda:self.ButtonClick(""),   compound = tk.CENTER, bg = "gray"  , fg = "white").place(x = 100, y = 250, width = ButtonSize,     height = ButtonSize)
        tk.Button(self.master, text = "",   command = lambda:self.ButtonClick(""),   compound = tk.CENTER, bg = "gray"  , fg = "white").place(x =  50, y =  50, width = ButtonSize,     height = ButtonSize)
        tk.Button(self.master, text = "",   command = lambda:self.ButtonClick(""),   compound = tk.CENTER, bg = "gray"  , fg = "white").place(x = 100, y =  50, width = ButtonSize,     height = ButtonSize)

    # ボタンを押した際の処理
    def ButtonClick(self, text):
        """
        正しい数式を入力されているか判断する処理
        """
        # 最初に入力された数字が 0 の場合
        if text == 0 and self.DisplayText == "0":
            return
        # 計算記号の次に入力された数字が 0 の場合
        if text == 0 and CalculationSymbol_Check(self.DisplayText[-1]):
            return
        # 計算記号の次に計算記号が入力された場合
        if CalculationSymbol_Check(text) and CalculationSymbol_Check(self.DisplayText[-1]):
            # 計算記号を新たに入力されたものに更新
            self.DisplayText = self.DisplayText[:-1] + text
            self.DisplayLabel["text"] = self.DisplayText
            return
        """
        正しい順序で入力されている場合の処理
        """
        # 数値が入力された場合の処理
        if type(text) == int:
            # ディスプレイ部が 0 なら修正
            if self.DisplayText == "0" and type(text) == int:
                self.DisplayText = ""
            # 表示部分の更新
            self.DisplayText += str(text)
            self.DisplayLabel["text"] = self.DisplayText
        # 計算記号が入力された場合の処理
        elif self.DisplayText != "" and type(text) == str:
            # 表示部分の更新
            self.DisplayText += str(text)
            self.DisplayLabel["text"] = self.DisplayText

    # AC（All Clear）ボタンを押された際の処理
    def AllClear(self):
        self.DisplayText = "0"
        self.DisplayLabel["text"] = self.DisplayText

    # ＝ボタンを押された際の処理
    def calc(self):
        RPN = Convert_RPN(self.DisplayText)
        # 計算
        self.DisplayText = calculation(RPN)
        # 表示部分の更新
        self.DisplayLabel["text"] = self.DisplayText

    # ディスプレイ部分の設定
    def createCanvas(self):
        self.canvas = tk.Canvas(self.master, width = DisplayWidth + 10, height = DisplayHeight + 10, bg = "black")
        self.canvas.place(x = -5, y = -5)
        self.DisplayLabel = tk.Label(text = "0", anchor = "e", bg = "black", fg = "white")
        self.DisplayLabel.place(x = 0, y = 0, width = DisplayWidth, height = ButtonSize)
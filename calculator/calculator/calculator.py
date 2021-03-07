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
        if stock.check(-1) == "(":
            break
        if CalculationSymbol_Check(stock.check(-1)):
            break
        if stock.check(-1) == None:
            break
        else:
            tmp += stock.pop()
    if tmp != "":
        queue.enqueue(tmp[::-1])

"""
演算子の優先順位を返す
"""
def rank(text):
    if text == "(" or text == ")":
        return 3
    elif text == "＋" or text == "－":
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
        # ( の場合，スタックに追加するのみ
        if text[i] == "(":
            pass
        # 各文字のランクを評価し，優先度が高いなら実行
        elif rank(text[i]) != 0:
            while rank(text[i]) >= rank(s.check(-1)) and s.check(-1) != None:
                # 括弧の場合
                if rank(s.check(-1)) == 3:
                    s.pop()
                # 計算記号の場合，そのままキューに格納
                if rank(s.check(-1)) == 1 or rank(s.check(-1)) == 2:
                    q.enqueue(s.pop())
                # 数値の場合，読み取った値をキューに格納
                else:
                    CollectNumber(s, q)
        # 読み取った文字を格納【")"は不要であるため，例外で設定】
        if text[i] != ")":
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
    # 小数点第5位で四捨五入
    return str(round(float(s.pop()), 5))

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
        # 値入力の状態
        self.ValueInput_flag = False
        # 小数点ボタンの有効(True)・無効(False)
        self.DecimalPoint_flag = True
        # ()のボタンの状態【 ( : Ture, ) : False】
        self.Parenthesis_flag = True
        # ディスプレイ・ボタンの設定
        self.createCanvas()
        self.createButton()

    # ボタンの設定
    def createButton(self):
        # ボタンの配置
        tk.Button(self.master, text = "＝", command = self.calc,                     compound = tk.CENTER, bg = "orange",  fg = "white").place(x = 150, y = 250, width = ButtonSize,     height = ButtonSize)
        tk.Button(self.master, text = "＋", command = lambda:self.ButtonClick("＋"), compound = tk.CENTER, bg = "orange",  fg = "white").place(x = 150, y = 200, width = ButtonSize,     height = ButtonSize)
        tk.Button(self.master, text = "－", command = lambda:self.ButtonClick("－"), compound = tk.CENTER, bg = "orange",  fg = "white").place(x = 150, y = 150, width = ButtonSize,     height = ButtonSize)
        tk.Button(self.master, text = "×", command = lambda:self.ButtonClick("×"), compound = tk.CENTER, bg = "orange",  fg = "white").place(x = 150, y = 100, width = ButtonSize,     height = ButtonSize)
        tk.Button(self.master, text = "÷", command = lambda:self.ButtonClick("÷"), compound = tk.CENTER, bg = "orange",  fg = "white").place(x = 150, y =  50, width = ButtonSize,     height = ButtonSize)
        tk.Button(self.master, text = "０", command = lambda:self.ButtonClick(0),    compound = tk.CENTER, bg = "dimgrey", fg = "white").place(x =   0, y = 250, width = ButtonSize * 2, height = ButtonSize)
        tk.Button(self.master, text = "１", command = lambda:self.ButtonClick(1),    compound = tk.CENTER, bg = "dimgrey", fg = "white").place(x =   0, y = 200, width = ButtonSize,     height = ButtonSize)
        tk.Button(self.master, text = "２", command = lambda:self.ButtonClick(2),    compound = tk.CENTER, bg = "dimgrey", fg = "white").place(x =  50, y = 200, width = ButtonSize,     height = ButtonSize)
        tk.Button(self.master, text = "３", command = lambda:self.ButtonClick(3),    compound = tk.CENTER, bg = "dimgrey", fg = "white").place(x = 100, y = 200, width = ButtonSize,     height = ButtonSize)
        tk.Button(self.master, text = "４", command = lambda:self.ButtonClick(4),    compound = tk.CENTER, bg = "dimgrey", fg = "white").place(x =   0, y = 150, width = ButtonSize,     height = ButtonSize)
        tk.Button(self.master, text = "５", command = lambda:self.ButtonClick(5),    compound = tk.CENTER, bg = "dimgrey", fg = "white").place(x =  50, y = 150, width = ButtonSize,     height = ButtonSize)
        tk.Button(self.master, text = "６", command = lambda:self.ButtonClick(6),    compound = tk.CENTER, bg = "dimgrey", fg = "white").place(x = 100, y = 150, width = ButtonSize,     height = ButtonSize)
        tk.Button(self.master, text = "７", command = lambda:self.ButtonClick(7),    compound = tk.CENTER, bg = "dimgrey", fg = "white").place(x =   0, y = 100, width = ButtonSize,     height = ButtonSize)
        tk.Button(self.master, text = "８", command = lambda:self.ButtonClick(8),    compound = tk.CENTER, bg = "dimgrey", fg = "white").place(x =  50, y = 100, width = ButtonSize,     height = ButtonSize)
        tk.Button(self.master, text = "９", command = lambda:self.ButtonClick(9),    compound = tk.CENTER, bg = "dimgrey", fg = "white").place(x = 100, y = 100, width = ButtonSize,     height = ButtonSize)
        tk.Button(self.master, text = "．", command = lambda:self.ButtonClick("."),  compound = tk.CENTER, bg = "dimgrey", fg = "white").place(x = 100, y = 250, width = ButtonSize,     height = ButtonSize)
        tk.Button(self.master, text = "AC", command = self.AllClear,                 compound = tk.CENTER, bg = "silver",  fg = "black").place(x =   0, y =  50, width = ButtonSize,     height = ButtonSize)
        tk.Button(self.master, text = "()", command = lambda:self.ButtonClick("()"), compound = tk.CENTER, bg = "silver" , fg = "black").place(x =  50, y =  50, width = ButtonSize,     height = ButtonSize)
        tk.Button(self.master, text = "",   command = lambda:self.ButtonClick(""),   compound = tk.CENTER, bg = "silver" , fg = "black").place(x = 100, y =  50, width = ButtonSize,     height = ButtonSize)

    # ボタンを押した際の処理
    def ButtonClick(self, text):
        """
        正しい数式を入力されているか判断する処理
        """
        # 0 の次に入力された数字が 0 の場合
        if text == 0 and self.DisplayText[-1] == "0" and self.ValueInput_flag == False:
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
            if self.DisplayText[-1] == "0" and type(text) == int and self.ValueInput_flag == False:
                self.DisplayText = self.DisplayText[:-1]
            # 表示部分の更新
            self.DisplayText += str(text)
            self.DisplayLabel["text"] = self.DisplayText
            self.ValueInput_flag = True

        # 小数点が入力された場合の処理
        elif text == ".":
            # 小数点ボタンが有効の場合
            if self.DecimalPoint_flag:
                # 整数値が入力されていない場合は，0 を設定
                if CalculationSymbol_Check(self.DisplayText[-1]):
                    self.DisplayText += "0"
                # 表示部分の更新
                self.DisplayText += str(text)
                self.DisplayLabel["text"] = self.DisplayText
                # 値入力の有効化
                self.ValueInput_flag = True
                # 小数点ボタンの無効化
                self.DecimalPoint_flag = False

        # （ , ）が入力された場合の処理
        elif text == "()":
            # ( の場合の処理
            if self.Parenthesis_flag:
                # 計算記号の後に入力されなければ，反映しない
                if CalculationSymbol_Check(self.DisplayText[-1]):
                    # 表示部分の更新
                    self.DisplayText += "("
                    self.DisplayLabel["text"] = self.DisplayText
                    # ()ボタンのモード切り替え
                    self.Parenthesis_flag = False
            # ) の場合の処理
            else:
                # 数値の後に入力されなければ，反映しない
                if not(CalculationSymbol_Check(self.DisplayText[-1])):
                    # 表示部分の更新
                    self.DisplayText += ")"
                    self.DisplayLabel["text"] = self.DisplayText
                    # ()ボタンのモード切り替え
                    self.Parenthesis_flag = True

        # 計算記号が入力された場合の処理
        elif self.DisplayText != "" and CalculationSymbol_Check(text):
            # 表示部分の更新
            self.DisplayText += str(text)
            self.DisplayLabel["text"] = self.DisplayText
            # 値入力の無効化
            self.ValueInput_flag = False
            # 小数点の入力を有効化
            self.DecimalPoint_flag = True

    # AC（All Clear）ボタンを押された際の処理
    def AllClear(self):
        self.DisplayText = "0"
        self.DisplayLabel["text"] = self.DisplayText
        # 各ボタンの初期化
        self.DecimalPoint_flag = True
        self.Parenthesis_flag = True
        # 値入力の無効化
        self.ValueInput_flag = False

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
"""
スタッククラス
"""
class STACK:
    # コンストラクタ
    def __init__(self):
        self.__stack = []

    # プッシュ
    def push(self, item):
        self.__stack.append(item)

    # ポップ
    def pop(self):
        if len(self.__stack) == 0:
            return None
        return self.__stack.pop()

    # 指定インデックスの値を確認
    def check(self, index):
        if len(self.__stack) == 0:
            return None
        return self.__stack[index]

    # スタック全体の表示
    def display(self):
        print(self.__stack)
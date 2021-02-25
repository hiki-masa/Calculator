"""
キュークラス
"""
class QUEUE:
    # コンストラクタ
    def __init__(self):
        self.__queue = []

    # エンキュー
    def enqueue(self, item):
        self.__queue.append(item)

    # デキュー
    def dequeue(self):
        if len(self.__queue) == 0:
            return None
        item = self.__queue[0]
        del self.__queue[0]
        return item

    # 指定インデックスの値を確認
    def check(self, index):
        if len(self.__queue) == 0:
            return None
        return self.__queue[index]

    # キュー全体の表示
    def display(self):
        print(self.__queue)

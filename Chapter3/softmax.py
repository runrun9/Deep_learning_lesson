# ソフトマックス関数による出力層の設計

import numpy as np

def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c)       # オーバーフロー回避
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y                    # 各入力の指数 / 全入力の指数

a = np.array([0.3,2.9,4.0])     # 出力層の入力値
y = softmax(a)
print(y)
print(np.sum(y))                # 正規化により合計は1

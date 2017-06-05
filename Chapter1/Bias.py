import numpy as np


def AND(x1, x2):
    x = np.array([x1, x2])      # 入力
    w = np.array([0.5, 0.5])    # 重み
    b = -0.7                    # バイアス
    if np.sum(x*w) + b > 0:
        return 1
    else:
        return 0


print(AND(0, 0))
print(AND(0, 1))
print(AND(1, 0))
print(AND(1, 1))

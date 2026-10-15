import numpy as np
import matplotlib.pyplot as plt

# 生成x坐标：0到2π，一共100个点
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

# 绘图
plt.plot(x, y, color="blue")
plt.title("Sine Curve Demo")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.grid(True)
plt.show()

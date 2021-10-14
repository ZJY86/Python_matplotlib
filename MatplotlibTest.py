from matplotlib import pyplot as plt
import numpy as np
import math
import pylab

# 简单的绘图程序
def t1():
    x = np.arange(0, math.pi*2, 0.05)
    y = np.sin(x)
    plt.plot(x, y)
    plt.xlabel("angle")
    plt.ylabel("sine")
    plt.title('sine wave')
    plt.show()

# pylag接口
def t2():
    x = np.linspace(-3, 3, 30)
    y = x**2
    # 'r.'是控制符号
    pylab.plot(x, y, 'r.')
    pylab.plot(x, np.sin(x), 'r.')
    pylab.show()

# 接触figure对象:面向对象思想
def t3():
    # 创建图形对象
    fig = plt.figure(frameon=True)

    x = np.arange(0, math.pi*2, 0.05)
    y = np.sin(x)

    # 对图形对象进行操作,返回轴域对象
    # 数组里的四个参数对应轴域的位置与大小,都在0-1之间
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    ax.plot(x, y)
    ax.set_title('sine wine')
    ax.set_xlabel('angle')
    ax.set_ylabel('sine')
    plt.show()

# axes类(轴域对象) 一个figure可以有多个axes对象，但是一个axes对象只能绑定到一个figure对象上
# 用legend()方法进行实例绘图
def t4():
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y1 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    y2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    fig = plt.figure()

    # add_axes()方法返回一个axes类对象，绑定调用方法的figure对象
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

    # 用legend()方法绘图,plot表示创建图形实例
    ax.plot(x, y1, 'b--')
    ax.plot(x, y2, 'r.')
    # labels按顺序给图实例命名 loc参数表示绘图位置
    ax.legend(labels=('y1', 'y2'), loc='lower right')
    plt.show()

# 子图 subplot()
def t5():
    # subplot(row, column, index)用于把画布分为几行几列，并选择具体的子图
    # 如果subplot的参数不一致，则会进行覆盖
    # 如果不想进行子图覆盖，则用figure对象的add_subplot(),同样返回axes对象
    fig = plt.figure()

    ax1 = fig.add_subplot(1, 2, 1)
    ax2 = fig.add_subplot(2, 3, 3, facecolor='y')
    ax1.plot([1, 2, 3], [1, 2, 3])
    ax2.plot([1, 2, 3], [3, 2, 1])
    plt.show()
    # 还可以通过add_axes方法直接在一个图像中插入另一个图像
    # x = np.arange(0, math.pi * 2, 0.05)
    # fig = plt.figure()
    # axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])  # main axes
    # axes2 = fig.add_axes([0.55, 0.55, 0.3, 0.3])  # inset axes
    # y = np.sin(x)
    # axes1.plot(x, y, 'b')
    # axes2.plot(x, np.cos(x), 'r')
    # axes1.set_title('sine')
    # axes2.set_title("cosine")
    # plt.show()

# subplots()方法
def t6():
    pass

if __name__ == '__main__':
    t6()

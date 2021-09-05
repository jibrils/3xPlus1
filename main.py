import math
import time
import matplotlib.pyplot as plt

xList = []
stepsList = []
x = int(input("Enter your starting number: "))
speed = float(input("Enter the speed of animation in secs per plot: "))
step = 0

while True:

    step = step + 1
    stepsList.append(step)
    xList.append(x)

    if x % 2 == 0 :
        x = x / 2

    elif x == 1 :
        print("done")
        break
    else:
        x = 3 * x + 1

    plt.title('3x + 1')
    plt.xlabel('Steps')
    plt.ylabel('Value of x')

    plt.plot(stepsList, xList)
    plt.pause(speed)
    plt.cla()

plt.plot(stepsList, xList)
plt.show()
print(xList)
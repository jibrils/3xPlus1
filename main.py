import math
import time
import matplotlib.pyplot as plt

xList = []
stepsList = []
x = int(input("Enter your starting number: "))
step = 0

while True:

    step = step + 1
    stepsList.append(step)
    xList.append(x)

    if x % 2 == 0 :
        x = x / 2
        print(str(x) + " at step number:  " + str(step))
    elif x == 1 :
        print("done")
        break
    else:
        x = 3 * x + 1
        print(str(x) + " at step number:  " + str(step))

print(stepsList)
print(xList)

plt.plot(stepsList, xList)
plt.title('3x + 1')
plt.xlabel('Steps')
plt.ylabel('Value of x')
plt.show()
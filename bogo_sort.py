import matplotlib.pyplot as plt
import random
import time

data = [2,1]
sorted = data.copy()
sorted.sort()
print(data)
plt.plot(data)
plt.show()

while not data == sorted:
    random.shuffle(data)
    print(data)
    plt.clf()
    plt.bar(range(1,len(data)+1), data)
    plt.show()
    time.sleep(0.001)
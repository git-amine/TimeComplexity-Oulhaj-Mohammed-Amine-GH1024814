import matplotlib.pyplot as plt


def exponential_algo(n):
    if n == 0:
        print("call 0")
        return 0
    else:
        print("call", n)
        exponential_algo(n-1)
        exponential_algo(n-1)

exponential_algo(3)

steps=[]
def exponential(n):
    return 2**n

for i in range(1,20):
    steps.append(exponential(i))

plt.plot(steps)
plt.show()


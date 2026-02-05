print('USE of DDA Algorithm')

import matplotlib.pyplot as plt

def DDA(x1,y1,x2,y2):
    dx = x2-x1
    dy = y2-y1
    if (abs(dx) >= abs(dy)):
        steps = abs(dx)
    else:
        steps = abs(dy)
    
    x = x1
    y = y1
    xs = []
    ys = []

    for i in range(steps+1):
        x += dx/steps
        y += dy/steps
        xs.append(round(x))
        ys.append(round(y))

    return xs, ys

x1 = int(input('Enter x1: '))
y1 = int(input('Enter y1: '))       
x2 = int(input('Enter x2: '))
y2 = int(input('Enter y2: '))



xs, ys = DDA(x1,y1,x2,y2)




plt.plot(xs, ys, marker='o', color='black')
plt.title('DDA Line Drawing Algorithm')
plt.xlabel('X-axis')    
plt.ylabel('Y-axis')
plt.grid()
plt.show()

            
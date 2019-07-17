import matplotlib.pyplot as plt
import numpy as np


#创建数据
x = np.arange(0,1,0.05)
y = np.sin(2*np.pi*x)
y2 = np.cos(2*np.pi*x)
plt.plot(x,y,color='red',label='sin(x)')    #更改图表的颜色在plt.plot中修
plt.plot(x,y2,color='yellow',label='cos(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('my first plot')
plt.legend(loc='best')
# fig,ax = plt.subplots(2,2)
# ax[0,1].plot(x,y)
# ax[1,1].plot(x,y2)
plt.show()

# 保存
plt.savefig('myplot.png')

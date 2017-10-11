import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3,3, 50)
y1 = 0.1*x + 1
#y2 = x**2
plt.figure()
plt.plot(x,y1, linewidth=10)
#plt.xlim(-1,2)
plt.ylim(-2,2)#设置坐标周
#plt.xlabel("I am x")
#plt.ylabel("I am y")#设置坐标周名称

#gca = "get current axis"，改变坐标周的位置
ax = plt.gca()
ax.spines['right'].set_color("none")
ax.spines['top'].set_color("none")
ax.spines['top'].set_color("none")
ax.xaxis.set_ticks_position("bottom")
ax.yaxis.set_ticks_position("left")
ax.spines["bottom"].set_position(("data",0))
ax.spines["left"].set_position(("data",0))
#l1,=plt.plot(x,y2, label="up")
#l2,=plt.plot(x,y1,color="red",linewidth=5,linestyle="--",
 #    label="down")
#plt.legend(handles=[l1,l2],loc="best")#添加图例
#添加注解
# x0 =1
# y0 = 2*x0+1
# plt.scatter(x0,y0, s = 50,color = "b")
# plt.plot([x0,x0],[y0,0],'k--',lw=2.5)
# plt.annotate(r"$2x+1=%s$" % y0,xy=(x0,y0),xycoords='data',xytext=(+30,-30),
# textcoords="offset points",fontsize=16)#arrowstyle=dict("->",
# #connectionstyle="arc3,rad=0.2"))
# plt.text(-3.7,3, r'$This\ is\ the\ some\ text.\ \mu\ \sigma_i\ \alpha_t$',
#          fontdict={"size":16,"color":"red"})#设置文本注释
# for label in ax.get_xticklabels+ax.get_yticklabels():
#     label.set_fontsize(12)
#     label.set_bbox(dict(facecolor="white",edgecolor="none",
#                    alpha=0.7))设置坐标透明度
n = 1024
X = np.random.normal(0,1,n)
Y = np.random.normal(0,1,n)
T = np.arctan2(Y,X)#颜色指
plt.scatter(X,Y,s=75,c=T,alpha=0.5)
plt.xlim((-1.5,1.5))
plt.ylim(())
plt.show()
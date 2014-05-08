#! encoding: UTF-8
import matplotlib.pyplot as pl
x=[-2.0,-1.0,0.0,1.0,2.0]
y=[-4.96,-4.8,-4,0,20]
x1=[-3,3]
y1=[0,0]
x2=[0,0]
y2=[-6,30]
pl.title('Grafica 1')
pl.xlabel('Eje x')
pl.ylabel('Eje y')
pl.plot (x,y, marker='o',linestyle=':',color='r', label='Funcion (5^x)-5')
pl.plot (x1,y1,color='k')
pl.plot (x2,y2,color='k')
pl.legend(loc=4)
pl.xlim(-3.0, 3.0)
pl.ylim(-6.0, 30.0)
pl.xticks(x)
pl.savefig("grafcap2.eps", dpi=100)
pl.show()
#! encoding: UTF-8
import matplotlib.pyplot as pl
x=[0,1,2,3]
y=[0.0,0.000028133,0.000024080,0.000031948]
pl.title('Grafica del tiempo de ejecucion')
pl.xlabel('Eje x')
pl.ylabel('Eje y')
pl.plot (x,y, marker='*',linestyle='--',color='c', label='Funcion tiempo')
pl.legend(loc=4)
pl.xlim(-0.1,3.1)
pl.ylim(-0.000001,0.00004)
pl.xticks(x)
pl.savefig("graftime.eps", dpi=100)
pl.show()
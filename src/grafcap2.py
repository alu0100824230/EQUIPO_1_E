#! encoding: UTF-8
import matplotlib.pylab as pl
x=[-2.-1,0,1,2]
y=[-4.96,-4.8,-4,0,20]
pl.title('Funcion (5^x)-5')
pl.xlabel('Eje x')
pl.ylabel('Eje y')
pl.plot (x,y, marker='o',linestyle=':',color='r', label='funcion 1')
pl.legend(loc=4)
pl.savefig("grafica.eps", dpi=100)
pl.show()
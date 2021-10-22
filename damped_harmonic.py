from RungeKutta import RungeKutta4

def fun(t,x,v):
    t += 1
    k =  7
    m = 2.8
    b = 0.6
    return -((v*b)/m)-(k*x)

rk=RungeKutta4(fun,0,0,3)

rk.show_iter  = True
rk.show_KandL = True
rk.percent =True

rk.solve(0,50,0.1)

rk.plot('t','x')
rk.plot('t','v')
rk.plot('x','v')

rk.show()


import matplotlib.pyplot as plt

sum    = lambda a,b             : a+(b/2) 
med    = lambda v1,v2,v3,v4     : (v1+(2*v2)+(2*v3)+v4)/6 
eval   = lambda fun,x,h,y,k,z,l : fun(sum(x,h),sum(y,k),sum(z,l))

time = ["Time","time","TIME",'T','t']
pos  = ["Position","position","POSITION",'X','x']
vel  = ["Velocity ","velocity ","VELOCITY ",'V','v']

def check(a,axs,val1,val2):
    if val1 in time and val2 in pos:
        axs.plot(a[0],a[1])
    if val2 in vel and val1 in time:
        axs.plot(a[0],a[2])
    if val1 in pos and val2 in vel:
        axs.plot(a[1],a[2]) 
    if val2 in pos and val1 in vel:
        axs.plot(a[2],a[1])  

class RungeKutta4:

    def __init__(self,fun,x_initial,y_initial,z_initial):

        self.fun        = fun
        self.x          = x_initial
        self.y          = y_initial
        self.z          = z_initial
        self.show_iter  = False
        self.show_KandL = False
        self.a          = []
        self.percent    = False
    
    def solve(self,start,stop,step):

        k1,k2,k3,k4=0,0,0,0
        l1,l2,l3,l4=0,0,0,0

        x = []
        y = []
        t = []

        h=start

        x0,y0,z0 = self.x,self.y,self.z
        fun      = self.fun
        

        while h<=stop:

            t.append(h)

            k1  = step*z0                                         
            l1  = step*fun(x0,y0,z0)

            k2  = step*sum(z0,l1)                  
            l2  = step*eval(fun,x0,step,y0,k1,z0,l1)  

            k3  = step*sum(z0,l2)                  
            l3  = step*eval(fun,x0,step,y0,k2,z0,l2) 

            k4  = step*(z0+l3)  
            l4  = step*fun(x0+step,y0+k3,z0+l3)

            y0  += med(k1,k2,k3,k4)
            z0  += med(l1,l2,l3,l4)

            if self.percent:
                print(" %.4f completed" % (h*100/stop),end='\r')
            
            

            if self.show_KandL:
                print('\n'+'#'*4+' At t = %.5f ' % (h)+'#'*4+'\n')
                print("\n k1 = %.8f\n l1 = %.8f\n\n k2 = %.8f\n l2 = %.8f\n\n k3 = %.8f\n l3 = %.8f\n\n k4 = %.8f\n l4 = %.8f\n" % (k1,l1,k2,l2,k3,l3,k4,l4))

            if self.show_iter:
                print(" Y(%.2f) = %.4f" % (h,y0))
                print(" Z(%.2f) = %.4f" % (h,z0))

            x.append(y0)
            y.append(z0)

            h += step
        
        self.a=[t,x,y]

        return t,x,y

    def plot(self,val1,val2):
        a=self.a
        fig,axs = plt.subplots()
        check(a,axs,val1,val2)
        axs.set_xlabel(val1+' =>')
        axs.set_ylabel(val2+' =>')
        fig.suptitle(val1+' vs '+val2)
    
        
    def show(self):
        plt.show()







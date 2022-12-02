import math
import my_lib as mb
import matplotlib.pyplot as plt

#INUPT---------------
filename = 'input.txt'
with open(filename) as data:
    arr = mb.read_data(data)
mb.floater(arr) #floats the data which was read as strings before

# END OF INPUT ----------------------------


#OUTPUT---------------------------#
res_file = open('output.txt','w')
Res = []

#Question - 1:

Res.append('Question-1--------------------------- \n')
def f(x):
    return math.log(x/2)-math.sin(5*x/2)

Res.append('\n #iterations Vs Root by Bisection \n')
mb.root_bisection(f,1.5,2.5,0.000001,Res)
Res.append('\n #iterations Vs Root by Regula-Falsi \n')
mb.root_regula_falsi(f,1.5,2.5,0.000001,Res)


#Question-2:
Res.append('\n Question-2------------------------ \n')

def g(x):
    return - x - math.cos(x)
def Dg(x):
    return -1 + math.sin(x)

Res.append('\n #iterations Vs Root by Bisection \n')
mb.root_bisection(g,1.5,2.5,0.000001,Res)
Res.append('\n #iterations Vs Root by Regula-Falsi \n')
mb.root_regula_falsi(g,1.5,2.5,0.000001,Res)
Res.append('\n #iterations Vs Root by Newton-Raphson \n')
mb.root_newton_raphson(g,Dg,1,0.000001,Res)
# mb.root_newton_raphson(f, Df, init, e, out)

#Question 3:
Res.append('\n Question-3------------------------ \n')

poly = [1,0,-5,0,4]
roots = []
mb.root_lag(poly,roots,0.000001,2) #Generating Positive Solutions with postive guess
for i in range(len(roots)):
    Res.append(str(roots[i]) + ' ')
Res.append('\n')


poly = [1,0,-5,0,4]
roots = []
mb.root_lag(poly,roots,0.000001,-3) #Generating negative Solutions with negative guess

for i in range(len(roots)):
    Res.append(str(roots[i]) + ' ')





#Question 4:
Res.append('\n Question-4------------------------ \n')

x,y = arr[0][0],arr[1][0]

pars = mb.polfit(x, y, 3)
Res.append('The least square polynomial fit parameters are: \n '+ 'a0 = '+str(pars[0]) +  ' a1 = '+str(pars[1])+  ' a2 = '+str(pars[2])+  ' a3 = '+str(pars[3]))

#PLOT----------------------
def h(x):
    a = pars[0]
    b = pars[1]
    c = pars[2]
    d = pars[3]
    return (d*x**3) + (c*x**2) + (b*x) + a

fx = [0.001*x for x in range(0,1000)]
func = [h(ele) for ele in fx]
plt.plot(fx,func)
plt.plot(x,y,'+')
# plt.show()
#PLOT------------------------------------



Res.append('\n \n Additional Comments : It is observed that the Laguerre Method was giving only solutions upto the sign of the initial guess, \n thus two different guesses one positive and another negative had to be used to generate the entire solution. ')


for i in range(len(Res)):
    # for j in range(len(Res[i])):
    res_file.writelines(Res[i])
res_file.close()

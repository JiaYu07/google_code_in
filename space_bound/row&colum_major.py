import time
import matplotlib.pyplot as plt
import numpy as np

table=[ ]
trow=[]
tcol=[]
size=[]

def row(sz,table=[]):    
    for i in range(0,sz):
        for j in  range(0,sz):
            table[i][j]=i+j
     #print("row-style",'\n',time_elapsed1)


def column(sz,table=[]) :     
    for j in  range(0,sz):
        for i in  range(0,sz):
            table[i][j]=i+j
    #print("column-style",'\n',time_elapsed2)

def chart():
    plt.title("Row-Major vs Cloumn-Major")
    plt.xlabel("sizes")
    plt.ylabel("time")
    global size, trow, tcol
    plt.plot(size,trow,'s-',color="blue",label="row1")
    plt.plot(size,tcol,'o-',color="green",label="column1")
    plt.legend(loc = "best", fontsize=20)    
    plt.show()

def main():
    t=10
    while t>0 :
        i=0
        t-=1
        i=int(input())
        cnt=i*i
        global size
        size.append(i*i)
        table=np.arange(0,i*i).reshape(i,i)           
        st = time.clock()
        column(i,table)
        x = time.clock()-st
        global tcol
        tcol.append(x)
        
        st = time.clock()
        row(i,table)
        x=time.clock()-st
        global trow
        trow.append(x)
    '''
    ttrow=np.array( trow)
    ttcol=np.array( tcol)  
    print(ttrow)
    print(ttcol)
    '''


def numpy():
    table=np.arange(0,16).reshape(4,4)
    columx=np.ravel(table,order="F")
    rowy=np.ravel(table,order="C")
    print("row-major:",'\n',rowy)
    print("column-major:",'\n',columx)

numpy()
main()
chart()
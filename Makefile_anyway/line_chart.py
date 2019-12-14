import matplotlib.pyplot as plt
import numpy as np

get=open(r'data.txt')
str=get.readline()
str=str.split(' ')
score=[]
for i in range(len(str)-1):
 score.append(str[i])

get.close()

number=[]
for i in range(100):
  number.append(i)


plt.title("Student's Grade Distribution")
plt.xlabel("grade")
plt.ylabel("number")

plt.plot(number,score,color="blue",linestyle="--")
plt.show()
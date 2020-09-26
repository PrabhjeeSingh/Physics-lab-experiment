import numpy as ny

h=float(input("Enter height: "))
i=1
c={}
m=[]
time=[]
#calculating g
while (i<11):
      t = float(input("Enter time: "))
      g= (2*h)/t**2
      
      s=round(g,3)
      c[i]=s
      m.append(s)
      time.append(t)
      i=i+1



#calculating delta g
dm=[]
delta={}
for n,v in c.items():
      uncertain = (v-9.81)/9.81
      uni=round(uncertain,3)
      delta[n]=uni
      dm.append(uni)

time_mean = ny.mean(time)
time_standard = ny.std(time)

mean = ny.mean(m)
standard = ny.std(m)

delta_mean = ny.mean(dm)
delta_standard = ny.std(dm)

print("g values")
print(c)
print("\n\n")
print("delta values")
print(delta)
print("\n time_mean={} , time_standard={}".format(time_mean,time_standard))
print("\n mean={} , standard={}".format(mean,standard))
print("\n delta_mean={} , delta_standard={}".format(delta_mean,delta_standard))

      


      

import csv
import os
from math import *

input_lyr=[ 0.0 for i in range(8) ]
weight=[]
iter_input=0
dist_a=0.0
dist_b=0.0
dist_c=0.0
a=0 #iter buat distance
winner=0.0
lrate=0.01#lrate
tau=0.3
content = [[]]
pilihan="Saya Ganteng"
rbf_weight=[[]]
input_lyr2=[ 0.0 for i in range(8) ]
gauss_a=0.0
gauss_b=0.0
gauss_c=0.0
v=[]
kelas1=0
kelas2=0
tes=[]
min=[100.0 for i in range (7)]
max=[-100.0 for i in range (7)]
tengah=[0.0 for i in range (3)]
out=[[0.0 for i in range (2)] for j in range (210)]


#load weight_log dari input ke hidden
with open('weight_log.txt', 'r+') as csvfile:
	read = csv.reader(csvfile, delimiter='\t')
	for row in read:
		rbf_weight=list(read)
		for x in range(len(rbf_weight)):
			for y in range(len(rbf_weight[x])):
				rbf_weight[x][y] = float(rbf_weight[x][y])
				print str(rbf_weight[x][y])+'\t'
			print '\n\n'



#load weight_log dari hidden ke output
with open('weight_log2.txt', 'r+') as csvfile:
	read = csv.reader(csvfile, delimiter='\t')
	for row in read:
		v=list(read)
		for x in range(len(v)):
			for y in range(len(v[x])):
				v[x][y] = float(v[x][y])
				print str(v[x][y])+'\t'
			print '\n'
		

#cari min max dari data set aslinya untuk normalisasi
with open('dataasli.txt', 'r+') as csvfile:
	read = csv.reader(csvfile, delimiter='\t')
	for row in read:
		content=list(read)
		for x in range(len(content)):
			for y in range(len(content[x])):
				content[x][y] = float(content[x][y])

for x in range(len(content)):
	for y in range(len(content[x])-1):
		if content[x][y] > max[y]:
			max[y]=content[x][y]

		if content[x][y] < min[y]:
			min[y]=content[x][y]

print "MIN"
for x in range(len(min)):
	print min[x]
print '\n'

print "MAX"
for x in range(len(max)):
	print max[x]
print '\n'


#load test case sekaligus normalisasi di array tes
with open('tes.txt', 'r+') as csvfile:
	read = csv.reader(csvfile, delimiter='\t')
	for row in read:
		tes=list(read)
		for x in range(len(tes)):
			for y in range(len(tes[x])-1):
				tes[x][y] = float(tes[x][y])
				tes[x][y]=(tes[x][y]-min[y])/(max[y]-min[y])
				print tes[x][y]
			print '\n'
			tes[x][7]=int(tes[x][7])

out=[[0.0 for i in range (2)] for j in range (len(tes))]
#feed foward untuk menentukan kelas dari data tes
for x in range (len(tes)):
	tengah=[0.0 for i in range (3)]
	for i in range (3):
		for y in range(len(tes[x])-1):
			#tengah[i]=tengah[i]+(tes[x][y]-rbf_weight[i][y])**2
			tengah[i]=tengah[i]+tes[x][y]*rbf_weight[i][y]
		#aktivasi sigmoid
		#tengah[i]=sqrt(tengah[i])
		tengah[i]=1.0/(1.0+exp(-tengah[i]))
	
	out[x][0]=tengah[0]*v[0][0]+tengah[1]*v[0][1]+tengah[2]*v[0][2]
	out[x][1]=tengah[0]*v[1][0]+tengah[1]*v[1][1]+tengah[2]*v[1][2]
	#os.system("pause")
kelas=[0 for i in range(len(tes))]
benar=0
file = open("hasil.txt", "w+")
for x in range (len(tes)):
	print "Data ke-"+str(x)
	for y in range (2):
		print out[x][y]
	print '\n'
	for y in range (2):
		if out[x][y]<0.5:
			out[x][y]=0
		else:
			out[x][y]=1
		print out[x][y]

	print '\n'			
	if out[x][0]==0:
		if out[x][1]==0:
			kelas[x]=0
		elif out [x][1]==1:
			kelas[x]=1
	elif out[x][0]==1:
		if out[x][1]==0:
			kelas[x]=2
		elif out[x][1]==1:
			kelas[x]=3
	#print tengah[x]
	for y in range (8):
                file.write(str(tes[x][y])+'\t')
        file.write(str(out[x])+'\t')
        file.write(str(kelas[x])+'\n')
	if kelas[x]==tes[x][7]:
		benar=benar+1

file.close()
hasil=0.0
hasil=benar/float(len(tes))
hasil=hasil*100
print str(hasil)+"% Benar"
os.system("pause")

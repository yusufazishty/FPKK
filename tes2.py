import csv
from math import *

input_lyr=[ 0.0 for i in range(8) ]
weight=[]
iter_input=0
dist_a=0.0
dist_b=0.0
dist_c=0.0
a=0 #iter buat distance 
winner=0.0
lrate=0.1#lrate
tau=0.3
content = [[]]
pilihan="Saya Ganteng"
rbf_weight=[[]]
input_lyr2=[ 0.0 for i in range(8) ]
gauss_a=0.0
gauss_b=0.0
gauss_c=0.0
v=[[0.1,0.2],[0.3,0.4],[0.5,0.6]]
kelas1=0
kelas2=0
tes=[]
min=[0.0 for i in range (7)]
max=[0.0 for i in range (7)]
tengah=[0.0 for i in range (3)]

#load weight_log dari input ke hidden
with open('weight_log.txt', 'r+') as csvfile:
	read = csv.reader(csvfile, delimiter='	')
 	for row in read:
		rbf_weight=list(read)
		for x in range(len(rbf_weight)):
			for y in range(len(rbf_weight[x])):
				rbf_weight[x][y] = float(rbf_weight[x][y])
				
			
	
#load weight_log dari hidden ke output
with open('weight_log2.txt', 'r+') as csvfile:
	read = csv.reader(csvfile, delimiter='	')
 	for row in read:
		v=list(read)
		for x in range(len(v)):
			for y in range(len(v[x])):
				v[x][y] = float(v[x][y])


#cari min max dari data set aslinya untuk normalisasi
with open('normaldata.csv', 'r+') as csvfile:
     read = csv.reader(csvfile, delimiter='	')
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

#load test case sekaligus normalisasi di array tes
with open('tes.txt', 'r+') as csvfile:
	read = csv.reader(csvfile, delimiter='	')
 	for row in read:
		tes=list(read)
		for x in range(len(tes)):
			for y in range(len(tes[x])-1):
				tes[x][y] = float(tes[x][y])
				tes[x][y]=(tes[x][y]-min[y])/(max[y]-min[y])
				print tes[x][y]

#straight foward untuk menentukan kelas dari data tes
for x in range (4):
	for y in range(len(tes[x])-1):
		tengah[x]=tengah[x]+tes[x][y]*rbf_weight[x][y]
	#sigmoid dulu gan :)
		#print tes [x][y]
	#print tengah[x]
		
		


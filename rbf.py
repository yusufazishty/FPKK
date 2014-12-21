import csv
import os
from math import *
winner=0.0
lrate=0.00075 #0001#lrate
tau=0.3
content = [[]]
pilihan="Saya Ganteng"
rbf_weight=[[]]
input_lyr2=[ 0.0 for i in range(8) ]
gauss_a=0.0
gauss_b=0.0
gauss_c=0.0
v=[[0.1,0.2,0.3],[0.4,0.5,0.6]]
kelas1=0
kelas2=0
poin=0

with open('lrate.txt', 'r+') as csvfile:
	read = csv.reader(csvfile, delimiter='\t')
	for row in read:
		content=list(read)
		for x in range(len(content)):
			for y in range(len(content[x])-1):
				content[x][y] = float(content[x][y])
lrate=content[0][0]
tau=float(content[0][1])
content=[[]]
with open('normaldata.csv', 'r+') as csvfile:
	read = csv.reader(csvfile, delimiter='\t')
	for row in read:
		content=list(read)
		for x in range(len(content)):
			for y in range(len(content[x])-1):
				content[x][y] = float(content[x][y])
			content[x][7]=int(content[x][7])

with open('weight_log.txt', 'r+') as csvfile:
        read = csv.reader(csvfile, delimiter='\t')
        for row in read:
                rbf_weight=list(read)
                for x in range(len(rbf_weight)):
                        for y in range(len(rbf_weight[x])):
                                rbf_weight[x][y] = float(rbf_weight[x][y])

if os.path.isfile('weight_log2.txt'):
	with open('weight_log2.txt', 'r+') as csvfile:
		read = csv.reader(csvfile, delimiter='\t')
		for row in read:
			v=list(read)
			for x in range(len(v)):
				for y in range(len(v[x])):
					v[x][y] = float(v[x][y])

epoch=10
for t in range(epoch):
        for x in range(len(content)):        
                #input data
                for y in range(len(content[x])):
                        input_lyr2[y]=content[x][y]
                dist_a=0.0
                dist_b=0.0
                dist_c=0.0
                '''
                print 'iterasi ke '+str(x)
                for b in range(3):
                        print v[0][b]
                print '\n'
                for b in range(3):
                        print v[1][b]
                print '\n'
                '''
                for y in range(len(content[x])-1):
                        dist_a += (input_lyr2[y] - rbf_weight[0][y]) ** 2
                        dist_b += (input_lyr2[y] - rbf_weight[1][y]) ** 2
                        dist_c += (input_lyr2[y] - rbf_weight[2][y]) ** 2
                dist_a=sqrt(dist_a)
                dist_b=sqrt(dist_b)
                dist_c=sqrt(dist_c)
                #tau=(dist_a+dist_b+dist_c)/3
                #print dist_a
                #print dist_b
                #print dist_c
                #cari gaussian
                gauss_a=exp(-((dist_a)**2)/2*(tau**2))
                gauss_b=exp(-((dist_b)**2)/2*(tau**2))
                gauss_c=exp(-((dist_c)**2)/2*(tau**2))
                #print gauss_a
                #print gauss_b
                #print gauss_c
                z1=(gauss_a*v[0][0])+(gauss_b*v[0][1])+(gauss_c*v[0][2])
                z2=(gauss_a*v[1][0])+(gauss_b*v[1][1])+(gauss_c*v[1][2])
                if content[x][7]==1:
                        kelas1=0
                        kelas2=1
                        print "kelas 1"
                elif content[x][7]==2:
                        kelas1=1
                        kelas2=0
                        print "kelas 2"
                elif content[x][7]==3:
                        kelas1=1
                        kelas2=1
                        print "kelas 3"
                v[0][0]=v[0][0]+(lrate*(kelas1-z1)*gauss_a)
                v[0][1]=v[0][1]+(lrate*(kelas1-z1)*gauss_b)
                v[0][2]=v[0][2]+(lrate*(kelas1-z1)*gauss_c)
                v[1][0]=v[1][0]+(lrate*(kelas2-z2)*gauss_a)
                v[1][1]=v[1][1]+(lrate*(kelas2-z2)*gauss_b)
                v[1][2]=v[1][2]+(lrate*(kelas2-z2)*gauss_c)
		
#os.system("pause")
file = open("weight_log2.txt", "w+")
file.write('\r\n')
file.write(str(v[0][0])+'\t'+str(v[0][1])+'\t'+str(v[0][2])+'\n'+str(v[1][0])+'\t'+str(v[1][1])+'\t'+str(v[1][2]))
file.close()	

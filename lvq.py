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
lrate=0.00075#lrate
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


with open('lrate.txt', 'r+') as csvfile:
	read = csv.reader(csvfile, delimiter='\t')
	for row in read:
		content=list(read)
		for x in range(len(content)):
			for y in range(len(content[x])-1):
				content[x][y] = float(content[x][y])
lrate=content[0][0]
content=[[]]
#menyimpan semua data set di dalam array
with open('normaldata.csv', 'r+') as csvfile:
	read = csv.reader(csvfile, delimiter='\t')
	for row in read:
		content=list(read)
		for x in range(len(content)):
			for y in range(len(content[x])-1):
				content[x][y] = float(content[x][y])
			content[x][7]=int(content[x][7])

#inputkan baris 1 sebagai input pertama kali
for x in range(1):
	for y in range(len(content[x])):
		input_lyr[y]=content[x][y]

#mulai lvq
#salin dulu bobot nya dari data set yang ada
weight=list(content)
if os.path.isfile('weight_log.txt'):
	with open('weight_log.txt', 'r+') as csvfile:
		read = csv.reader(csvfile, delimiter='\t')
		for row in read:
			weight=list(read)
			for x in range(len(weight)):
				for y in range(len(weight[x])):
					weight[x][y] = float(weight[x][y])

for x in range(len(content)):
	#print weight node 1 dan 2
	print 'iterasi ke '+str(x)
	#mulai lvq
	#1 hitung euqlidian distance
	dist_a=0.0
	dist_b=0.0
	dist_c=0.0
	for y in range(len(content[x])):
		input_lyr[y]=content[x][y]
	
	for y in range(len(content[x])-1):
		dist_a += (input_lyr[y] - weight[0][y]) ** 2
		dist_b += (input_lyr[y] - weight[1][y]) ** 2
		dist_c += (input_lyr[y] - weight[2][y]) ** 2
	dist_a=sqrt(dist_a)
	dist_b=sqrt(dist_b)
	dist_c=sqrt(dist_c)
	print "Distance A "+str(dist_a)
	print "Distance B "+str(dist_b)
	print "Distance C "+str(dist_c)
	print '\n'
	#2 tentukan winner
	winner=min(dist_a,dist_b,dist_c)
	#update bobot
	if winner==dist_a:
		for b in range(7):
			weight[0][b] = weight[0][b] + lrate * (input_lyr[b]-weight[0][b])
	elif winner==dist_b:
		for b in range(7):
			weight[1][b] = weight[1][b] + lrate * (input_lyr[b]-weight[1][b])
	elif winner==dist_c:
		for b in range(7):
			weight[2][b] = weight[2][b] + lrate * (input_lyr[b]-weight[2][b])
	for b in range(7):
		print weight[0][b]
	print '\n'
	for b in range(7):
		print weight[1][b]
	print '\n'
	for b in range(7):
		print weight[2][b]
	print '\n'
#def save(): untuk menyimpan outrput LVQ ke file digunakan sebagai start weight pada RBFNN
file = open("weight_log.txt", "w+")
file.write('\n')
file.write(str(weight[0][0])+'\t'+str(weight[0][1])+'\t'+str(weight[0][2])+'\t'+str(weight[0][3])+'\t'+str(weight[0][4])+'\t'+str(weight[0][5])+'\t'+str(weight[0][6]))
file.write('\n')
file.write(str(weight[1][0])+'\t'+str(weight[1][1])+'\t'+str(weight[1][2])+'\t'+str(weight[1][3])+'\t'+str(weight[1][4])+'\t'+str(weight[1][5])+'\t'+str(weight[1][6]))
file.write('\n')
file.write(str(weight[2][0])+'\t'+str(weight[2][1])+'\t'+str(weight[2][2])+'\t'+str(weight[2][3])+'\t'+str(weight[2][4])+'\t'+str(weight[2][5])+'\t'+str(weight[2][6]))
file.close()

'''
#Start RBFNN
pilihan="n"
while pilihan=="n":
	pilihan=raw_input("This is end of LVQ method, wanna start RBFNN? (y/n)")
	if pilihan=="y":
#masukkan weight awal RBFNN dari output weight nya LVQ
		with open('weight_log.txt', 'r+') as csvfile:
			read = csv.reader(csvfile, delimiter='\t')
			for row in read:
				rbf_weight=list(read)
				for x in range(len(rbf_weight)):
					for y in range(len(rbf_weight[x])):
						rbf_weight[x][y] = float(rbf_weight[x][y])

for x in range(len(rbf_weight)):
	for y in range(len(rbf_weight[x])):
		print str(rbf_weight[x][y])
	print '\n'

#inputkan baris 1 sebagai input pertama kali
#Mulai RBFNN
for x in range(len(content)):
	for y in range(len(content[x])):
		input_lyr2[y]=content[x][y]
	dist_a=0.0
	dist_b=0.0
	dist_c=0.0
	#print weight node 1 dan 2
	print 'iterasi ke '+str(x)
	for b in range(2):
		print v[0][b]
	print '\n'
	for b in range(2):
		print v[1][b]
	print '\n'
	for b in range(2):
		print v[2][b]
	print '\n'
	#mulai RBFNN
	#1 hitung euqlidian distance
	for y in range(len(content[x])-1):
		dist_a += (input_lyr2[y] - rbf_weight[0][y]) ** 2
		dist_b += (input_lyr2[y] - rbf_weight[1][y]) ** 2
		dist_c += (input_lyr2[y] - rbf_weight[2][y]) ** 2
	dist_a=sqrt(dist_a)
	dist_b=sqrt(dist_b)
	dist_c=sqrt(dist_c)
	#cari gaussian
	gauss_a=exp(-((dist_a)**2)/2*(tau**2))
	gauss_b=exp(-((dist_b)**2)/2*(tau**2))
	gauss_c=exp(-((dist_c)**2)/2*(tau**2))
	#cari output z
	z1=(gauss_a*v[0][0])+(gauss_b*v[1][0])+(gauss_c*v[2][0])
	z2=(gauss_a*v[0][1])+(gauss_b*v[1][1])+(gauss_c*v[2][1])
	#update weight
	#v_baru=v_lama+(l_rate*(kelas-output)*y)

	#update weight
	if content[x][7]==1:
		kelas1=0
		kelas2=1
	elif content[x][7]==2:
		kelas1=1
		kelas2=0
	elif content[x][7]==3:
		kelas1=1
		kelas2=1

	v[0][0]=v[0][0]+(lrate*(kelas1-z1)*gauss_a)
	v[1][0]=v[1][0]+(lrate*(kelas1-z1)*gauss_b)
	v[2][0]=v[2][0]+(lrate*(kelas1-z1)*gauss_c)
	v[0][1]=v[0][1]+(lrate*(kelas2-z2)*gauss_a)
	v[1][1]=v[1][1]+(lrate*(kelas2-z2)*gauss_b)
	v[2][1]=v[2][1]+(lrate*(kelas2-z2)*gauss_c)

file = open("weight_log2.txt", "w+")
file.write('\r\n')
file.write(str(v[0][0])+'\t'+str(v[1][0])+'\t'+str(v[2][0])+'\n'+str(v[0][1])+'\t'+str(v[1][1])+'\t'+str(v[2][1]))
file.close()

print "weight_log >> output lvq, bobot w untuk ke hidden layer"
with open('weight_log.txt', 'r+') as csvfile:
	read = csv.reader(csvfile, delimiter='\t')
	for row in read:
		rbf_weight=list(read)
		for x in range(len(rbf_weight)):
			for y in range(len(rbf_weight[x])):
				rbf_weight[x][y] = float(rbf_weight[x][y])
				print rbf_weight[x][y]
		print "\n"

print "weight_log2 >> bobot v untuk ke output layer"
with open('weight_log2.txt', 'r+') as csvfile:
	read = csv.reader(csvfile, delimiter='\t')
	for row in read:
		v=list(read)
		for x in range(len(v)):
			for y in range(len(v[x])):
				v[x][y] = float(v[x][y])
				print v[x][y]
		print "\n"






		#pembulatan
		if z1<0.5:
				z1=0
		else:
				z1=1
		if z2<0.5:
				z2=0
		else:
				z2=1

		v_baru=v_lama+(l_rate*(kelas-output)*y)
		if z1 < 0.5 and z2 >=0.5 :
				kelas="1"
		elif z1 >=0.5 and z2 <0.5:
				kelas="2"
		elif z1 >=0.5 and z2 >=0.5:
				kelas="3"
		else:
				kelas="bukan biji"
'''

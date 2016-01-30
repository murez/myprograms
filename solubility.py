
M=(raw_input("Please enter the mental like Fe+2,Fe+3,Mg,H,NH4 etc. : "))
S=(raw_input("Please enter the source like SO4,Cl,NO3,OH etc. :"))
if M=='H':
	m=0
elif M=='NH4':
	m=1
elif M=='K':
	m=1
elif M=='Na':
	m=1
elif M=='Ba':
	m=2
elif M=='Ca':
	m=3
elif M=='Mg':
	m=4
elif M=='Al':
	m=5
elif M=='Zn':
	m=7
elif M=='Fe+2':
	m=7
elif M=='Fe+3':
	m=7
elif M=='Cu':
	m=7
elif M=='Ag':
	m=9

if S=='OH':
	s=3
elif S=='NO3':
	s=20
elif S=='Cl':
	s=8
elif S=='SO4':
	s=9
elif S=='CO3':
	s=1.5

if m==2:
	if s==8:
		print 'Ba SO4 not solubility'
elif m==4:
	if s==1.5:
		print'Mg CO3 little solubility'
elif m==5:
	if s==1.5:
		print'no this kind of material'
elif m-s<0:
	print M+S+'solubility'
elif m-s==0:
	print M+S+'little solubility'
elif m-s>0:
	print M+S+'no solubility'
else :
	print'Try again'
#made by ZhangSiyuan

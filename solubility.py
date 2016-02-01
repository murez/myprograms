
M=(raw_input("Please enter the mental like Fe+2,Fe+3,Mg,H,NH4 etc. : "))
S=(raw_input("Please enter the source like SO4,Cl,NO3,OH etc. :"))
if M=='H':
        m=0
        k=1
elif M=='NH4':
        m=1
        k=1
elif M=='K':
        m=1
        k=1
elif M=='Na':
        m=1
        k=1
elif M=='Ba':
        m=2
        k=2
elif M=='Ca':
        m=3
        k=2
elif M=='Mg':
        m=4
        k=2
elif M=='Al':
        m=5
        k=3
elif M=='Zn':
        m=7
        k=2
elif M=='Fe+2':
        m=7
        M='(+2)Fe'
        k=2
elif M=='Fe+3':
        m=7
        M='(+3)Fe'
        k=3
elif M=='Cu':
        m=7
        k=2
elif M=='Ag':
        m=9
        k=1

if S=='OH':
        s=3
        p=1
elif S=='NO3':
        s=20
        p=1
elif S=='Cl':
        s=8
        p=1
elif S=='SO4':
        s=9
        p=2
elif S=='CO3':
        s=1.5
        p=2

if k==1:
        if p==1:
                a=''
                b=''
        if p==2:
                a='2'
                b=''
elif k==2:
        if p==1:
                a=''
                b='2'
        if p==2:
                a=''
                b=''
elif k==3:
        if p==1:
                a=''
                b='3'
        if p==2:
                a='2'
                b='3'

if M=='NH4':
        if p==2:
                M='(NH4)'
elif S=='OH':
        if k==2:
                S='(OH)'
        elif k==3:
                S='(OH)'
elif S=='NO3':
        if k==2:
                S='(NO3)'
        elif k==3:
                S='(NO3)'
elif S=='SO4':
        if k==3:
                S='(SO4)'
elif S=='CO3':
        if k==3:
                S='(CO3)'
        
if m==2:
        if s==8:
                print'BaSO4    not solubility'
elif m==4:
        if s==1.5:
                print'MgCO3    little solubility'
elif m==5:
        if s==1.5:
                print'Al2(CO3)3    no this kind of material'
elif m==9:
        if s==3:
                print'AgOH    no this kind of material'
elif m-s<0:
        print M+a+S+b+'   solubility'
elif m-s==0:
        print M+a+S+b+'   little solubility'
elif m-s>0:
        print M+a+S+b+'   no solubility'
else :
        print'Try again'
#made by ZhangSiyuan

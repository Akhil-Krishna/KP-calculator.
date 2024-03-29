from tkinter import *
from math import *
win=Tk()
c1=0
win.title('KP-calculator')
win.geometry('360x500')
win.resizable(0,0)

value=StringVar()

lab=Label(win,text='LABEL',anchor='se',bd=23,relief='sunken',textvariable=value,font=('bold',21),bg='powder blue',fg='black',height=2)

oper=['+','×','÷','-','//','^']
dis=''
def one_c():	
	global dis,v
	if dis=='0':
		dis=''
	try:
		if v==1:
			v=0
			dis=''
	except:
		pass
	dis+='1'
	value.set(dis)
def two_c():
	
	global dis,v
	if dis=='0':
		dis=''
	try:
		if v==1:
			v=0
			dis=''
	except:
		pass
	dis+='2'
	value.set(dis)
def three_c():
	global dis,v
	if dis=='0':
		dis=''
	try:
		if v==1:
			v=0
			dis=''
	except:
		pass
	dis+='3'
	value.set(dis)	
def four_c():
	global dis,v
	if dis=='0':
		dis=''
	try:
		if v==1:
			v=0
			dis=''
	except:
		pass
	dis+='4'
	value.set(dis)
def five_c():
	global dis,v
	if dis=='0':
		dis=''
	try:
		if v==1:
			v=0
			dis=''
	except:
		pass
	dis+='5'
	value.set(dis)
def six_c():
	global dis,v
	if dis=='0':
		dis=''
	try:
		if v==1:
			v=0
			dis=''
	except:
		pass
	dis+='6'
	value.set(dis)
def seven_c():
	global dis,v
	if dis=='0':
		dis=''
	try:
		if v==1:
			v=0
			dis=''
	except:
		pass
	dis+='7'
	value.set(dis)
def eight_c():
	global dis,v
	if dis=='0':
		dis=''
	try:
		if v==1:
			v=0
			dis=''
	except:
		pass
	dis+='8'
	value.set(dis)
def nine_c():
	global dis,v
	if dis=='0':
		dis=''
	try:
		if v==1:
			v=0
			dis=''
	except:
		pass
	dis+='9'
	value.set(dis)
def zero_c():
	global dis,v
	if dis=='0':
		dis=''
	try:
		if v==1:
			v=0
			dis=''
	except:
		pass
	dis+='0'
	value.set(dis)
def plus_c():
	global dis,v
	v=0
	dis+='+'
	value.set(dis)
def minus_c():
	global dis,v
	v=0
	dis+='-'
	value.set(dis)
def mul_c():
	global dis,v
	v=0
	dis+='×'
	value.set(dis)
def div_c():
	global dis,v
	v=0
	dis+='÷'
	value.set(dis)
def floor_c():
	global dis,v
	v=0
	dis+='//'
	value.set(dis)
def dot_c():
	global dis,v
	v=0
	dis+='.'
	value.set(dis)
def pi_c():
	global dis,v,c1
	if dis=='0':
		dis=''
	try:
		if v==1:
			v=0
			dis=''
		if c1==0:
			dis=''
	except:
		pass
	dis+=str(pi)[:13]
	value.set(dis)
def exp_c():
	global dis,v
	v=0
	dis+='^'
	value.set(dis)
def c_c():
	global dis
	dis=''
	value.set(dis)	
#def per_c():
	#global dis
#	dis+='%'
	#value.set(dis)
def sin_c():
	global dis,v
	try:
		if v==1:
			v=0
			dis=''
	except:
		pass
	dis+='sin'
	value.set(dis)
def cos_c():
	global dis,v
	try:
		if v==1:
			v=0
			dis=''
	except:
		pass
	dis+='cos'
	value.set(dis)
def tan_c():
	global dis,v
	try:
		if v==1:
			v=0
			dis=''
	except:
		pass
	dis+='tan'
	value.set(dis)
def root_c():
	global dis,v
	v=0
	dis+='√'
	value.set(dis)		
def dele_c():
	global dis
	dis=dis[:len(dis)-1]
	value.set(dis)	
	
def equal_c():
	global dis,v,c1
	c1=1
	v=1
	re=0
	try:
		if '+' in dis:
			l=dis.split('+')
			s=0
			for i in l:
				s+=eval(i)
			dis=str(s)
			if '.' in dis:
				ad=dis.split('.')
				if ad[1]=='0':
					dis=str(ad[0])
			if len(dis)>14 and '.' not in dis:
				d=dis[0]+'.'+dis[1:6]+'×10^'+str(len(dis)-1)
				value.set(d)
			elif len(dis)>14:
				
				dis1=dis.split('.')
				if len(dis1[0])>12:
					
					d1=dis[0]+'.'+dis1[0][1:6]+'×10^'+str(len(dis1[0])-1)
					value.set(d1)
				else:
					d1=dis1[0]+'.'+dis1[1][:10]
					value.set(d1)
			
				value.set(d1)
			else:
				value.set(dis)
		
		if '-' in dis:
			l=dis.split('-')
			s=eval(l[0])
			l.pop(0)
			for i in l:
				s-=eval(i)
			dis=str(s)
			if '.' in dis:
				ad=dis.split('.')
				if ad[1]=='0':
					dis=str(ad[0])
			if len(dis)>14:
				if '.' not in dis:
				
					
					dismin=f'{dis[0]}.{dis[1:6]}×10^{len(dis)-1}'
					value.set(dismin)
				else:
					
					dra=dis.split('.')
					if len(dra[0])>12:
						dismit=f'{dra[0][0]}.{dra[0][1:6]}×10^{len(dra[0])-1}'
						value.set(dismit)
					else:
						disamit=f'{dra[0]}.{dra[1][:8]}'
						value.set(disamit)
				
			else:		
				value.set(dis)

		if '×' in dis:
			l=dis.split('×')
			s=eval(l[0])
			l.pop(0)
			for i in l:
				s*=eval(i)
			dis=str(s)
			if '.' in dis:
				ad=dis.split('.')
					
				if ad[1]=='0':
					dis=str(ad[0])
			if len(dis)>14 and '.' not in dis:
				dismult=dis[0]+'.'+dis[1:6]+'×10^'+str(len(dis)-1)
				value.set(dismult)
			elif len(dis)>14 and '.' in dis:
				s4=dis.split('.')
				if len(s4[0])>6:
					dismult1=s4[0][0]+'.'+str(s4[0][1:6])+'×10^'+str(len(s4[0])-1)
				else:
					sm5=dis.split('e')
					if len(sm5)==1:
						dismult1=dis[:14]
						value.set(dis)
					else:
						dismult1=sm5[0][:7]+'×10^'+str(sm5[1][1:])
				value.set(dismult1)
			else:
				if 'e' in dis:
					dm=dis.split('e')
					if '+' in dm[1]:
						dm2=f'{dm[0]}×10^{dm[1][1:]}'
						value.set(dm2)
					else:
						dm2=f'{dm[0]}×10^{dm[1]}'
						value.set(dm2)
				else:
					
					
					value.set(dis)



					
	
		if '^' in dis:
			l=dis.split('^')
			s=eval(l[0])
			l.pop(0)
			for i in l:
				s**=eval(i)
			dis=str(s)
			if '.' in dis:
				ad=dis.split('.')
				if ad[1]=='0':
					dis=str(ad[0])
			if len(dis)>14 and '.' not in dis:
				dis1=dis[0]+'.'+dis[1:6]+'×10^'+str(len(dis)-1)
				value.set(dis1)
			elif len(dis)>14 and '.' in dis:
				s4=dis.split('.')
				if len(s4[0])>6:
					dis3=s4[0][0]+'.'+str(s4[0][1:6])+'×10^'+str(len(s4[0])-1)
				else:
					s5=dis.split('e')
					
					dis3=s5[0][:7]+'×10^'+str(s5[1][1:])
				value.set(dis3)
		
		if '//' in dis:
			l=dis.split('//')
			if l[1]=='0':
				value.set('Math Error')
				dis=''
				
			else:
				s=eval(l[0])
				l.pop(0)
				for i in l:
					s//=eval(i)
				dis=str(s)
				if len(dis)>15:
					df=dis[0]+'.'+dis[1:7]+'×10^'+str(len(dis)-1)
					value.set(df)
				else:
					value.set(dis)
		
		if '÷' in dis:
			l=dis.split('÷')
			if l[1]=='0':
			  dis='' 
			  value.set("Math ERROR")
			s=eval(l[0])
			l.pop(0)
			if l[0]=='0':
				value.set('Math ERROR')
				dis=''
			elif dis!="":
				for i in l:
					s/=eval(i)
				dis=str(s)
				if '.' in dis:		
					ad=dis.split('.')
				if ad[1]=='0':
					dis=str(ad[0])
			if len(dis)>14 and '.' not in dis:
				dismultdiv=dis[0]+'.'+dis[1:6]+'×10^'+str(len(dis)-1)
				value.set(dismultdiv)
			elif len(dis)>14 and '.' in dis:
				sd4=dis.split('.')
				if len(sd4)==1:
					sd4=dis.split('e')
				if len(sd4[0])>6:
					dismult1=sd4[0][0]+'.'+str(sd4[0][1:6])+'×10^'+str(len(sd4[0])-1)
				else:
					sm5=dis.split('e')
					if len(sm5)==1:
						dismult1=dis[:14]
						value.set(dis)
					else:
						dismult1=sm5[0][:7]+'×10^'+str(sm5[1][1:])
				value.set(dismult1)
			else:
				if 'e' in dis:
					dm=dis.split('e')
					if '+' in dm[1]:
						dm2=f'{dm[0]}×10^{dm[1][1:]}'
						value.set(dm2)
					else:
						dm2=f'{dm[0]}×10^{dm[1]}'
						value.set(dm2)
				elif dis!="":
					
					
					value.set(dis)
			
				
	
		if '%' in dis:
			l=dis.split('%')
			s=eval(l[0])
			l.pop(0)
			for i in l:
				s=s%eval(i)
			dis=str(s)
			value.set(dis)
		if 'sin' in dis:
			l=dis.split('sin')
			s=sin(eval(l[1])*pi/180)
		
			dis=str(s)
			if l[1]=='0':
				dis="0"
				value.set('0')
			elif l[1].isdigit():
				s=sin(eval(l[1])*pi/180)
				dis=str(s)[:14]
				value.set(dis)
				
			if l[1] not in ['0','1','2','3','4','5','6','7','8','9'] and eval(l[1][:-1])%2==0 and eval(l[1])%90==0:
				dis='0'
				value.set('0')
			else:
				if len(dis)>15:
					dis=dis[:15]
				if '.' in dis:
					l2=dis.split('.')
					if l2[1]=='0':
						dis=l2[0]
				value.set(dis)	
		
		if 'cos' in dis:
			l=dis.split('cos')
			s=cos(eval(l[1])*pi/180)
		
			dis=str(s)
			if l[1]=='0':
				dis='1'
				value.set('1')
			elif l[1].isdigit():
				s=cos(eval(l[1])*pi/180)
				dis=str(s)[:14]
				value.set(dis)
				
				
			if l[1] not in ['0','1','2','3','4','5','6','7','8','9'] and eval(l[1][:-1])%2!=0 and eval(l[1])%90==0:
				dis='0'
				value.set('0')
			else:
		
				if len(dis)>15:
					dis=dis[:15]
				if '.' in dis:
					l2=dis.split('.')
					if l2[1]=='0':
						dis=l2[0]
				value.set(dis)
		if 'tan' in dis:
			l=dis.split('tan')
			if l[1]=='0':
				dis='0'
				value.set('0')
			elif l[1].isdigit():
				s1=tan(eval(l[1])*(pi/180))
				
				dis=str(s1)[:14]
				value.set(dis)
				
			if l[1] not in ['0','1','2','3','4','5','6','7','8','9'] and eval(l[1][:-1])%2!=0 and eval(l[1])%90==0:
				value.set('Math ERROR')
			elif l[1] not in ['0','1','2','3','4','5','6','7','8','9'] and  eval(l[1][:-1])%2==0 and eval(l[1])%90==0:
				dis="0"
				value.set('0')
			else:
				s=tan(eval(l[1])*(pi/180))
		
				dis=str(s)
		
				if len(dis)>15:
					dis=dis[:15]
				if '.' in dis:
					l2=dis.split('.')
					if l2[1]=='0':
						dis=l2[0]
				if '.9999' in dis:
					distan=ceil(eval(dis))
					value.set(distan)	
				elif '.0000' in dis:
					distan2=floor(eval(dis))
					value.set(distan2)
				else:
					value.set(dis)
		if '√' in dis:
		
			l=dis.split('√')
			if l[0]=='':
				s=eval(l[1])**(0.5)
			elif l[0]!='0':
				s=eval(l[1])**(1/eval(l[0]))
			else:
				s="Math ERROR"
			if len(str(s))>13:
				s=str(s)[:13]

			
			dis=str(s)
			if len(dis)>10 and dis.isdigit():
				if '.9999' in dis:
					dis=eval(dis)
					dis=str(ceil(dis))
					dis=dis[:14]
				elif '.000' in dis:
					dis=str(floor(eval(dis)))[:13]
				
			value.set(dis)
	except:
		dis=''
		value.set('Syntax ERROR')

lab.pack(expand=True,fill='both')
r1=Frame(win,bg='black')
r1.pack(expand=True,fill='both')
r2=Frame(win,bg='yellow')
r2.pack(expand=True,fill='both')
r3=Frame(win,bg='cyan')
r3.pack(expand=True,fill='both')
r4=Frame(win,bg='blue')
r4.pack(expand=True,fill='both')
r5=Frame(win,bg='blue')
r5.pack(expand=True,fill='both')


o1=Button(r1,bd=5,text='1',font=('bold',20),command=one_c,bg='grey')
o1.pack(side='left',expand=True,fill='both')
o2=Button(r1,bd=5,text='2',font=('bold',20),command=two_c,bg="grey")
o2.pack(side='left',expand=True,fill='both')
o3=Button(r1,bd=5,text='3',font=('bold',20),command=three_c,bg='grey')
o3.pack(side='left',expand=True,fill='both')



o4=Button(r2,bd=5,text='4',font=('bold',20),command=four_c,bg='grey')
o4.pack(side='left',expand=True,fill='both')
o5=Button(r2,bd=5,text='5',font=("bold",20),command=five_c,bg='grey')
o5.pack(side='left',expand=True,fill='both')
o6=Button(r2,bd=5,text='6',font=('bold',20),command=six_c,bg='grey')
o6.pack(side='left',expand=True,fill='both')


o7=Button(r3,bd=5,text='7',font=('bold',22),bg='grey',command=seven_c)
o7.pack(side='left',expand=True,fill='both')
o8=Button(r3,bd=5,text='8',font=('bold',22),bg='grey',command=eight_c)
o8.pack(side='left',expand=True,fill='both')
o9=Button(r3,bg='grey',bd=5,text='9',font=('bold',21),command=nine_c)
o9.pack(side='left',expand=True,fill='both')


opi=Button(r4,bd=5,text='π',font=('bold',18),command=pi_c)
opi.pack(side='left',expand=True,fill='both')
o0=Button(r4,bd=5,text='0',font=('bold',21),command=zero_c,bg='grey')
o0.pack(side='left',expand=True,fill='both')
odot=Button(r4,bd=5,text=' . ',font=('bold',20),command=dot_c)
odot.pack(side='left',expand=True,fill='both')
ofloor=Button(r4,bd=5,text='//',font=('bold',20),command=floor_c,width=1)
ofloor.pack(side='left',expand=True,fill='both')
exp=Button(r4,bd=5,text='^',font=('bold',20),command=exp_c)
exp.pack(side='left',expand=True,fill='both')

osin=Button(r5,bd=5,text='sin',font=('bold',18),command=sin_c,width=2,bg='white')
osin.pack(side='left',expand=True,fill='both')
ocos=Button(r5,bd=5,text='cos',font=('bold',18),command=cos_c,width=2,bg='white')
ocos.pack(side='left',expand=True,fill='both')
otan=Button(r5,bd=5,text=' tan  ',font=('bold',18),command=tan_c,width=2,bg='white')
otan.pack(side='left',expand=True,fill='both')
oroot=Button(r5,bd=5,text=' ×√',font=('bold',15),command=root_c,width=1)
oroot.pack(side='left',expand=True,fill='both')

oequal=Button(r5,bd=5,text='=',font=('bold',20),command=equal_c,width=1,bg='#85B3D5')
oequal.pack(side='left',expand=True,fill='both')




dele=Button(r1,bd=5,text='DEL',font=('bold',13),command=dele_c,width=1,bg='brown')
dele.pack(side='left',expand=True,fill='both')
c=Button(r1,bd=5,text='C',font=('bold',20),width=1,command=c_c,bg='light green')
c.pack(side='left',expand=True,fill='both')
plu=Button(r2,bd=5,text='+',font=('bold',20),width=1,command=plus_c)
plu.pack(side='left',expand=True,fill='both')
min=Button(r2,bd=5,text='-',font=('bold',23),command=minus_c)
min.pack(side='left',expand=True,fill='both')
mul=Button(r3,bd=5,text='×',font=('bold',18),command=mul_c)
mul.pack(side='left',expand=True,fill='both')
div=Button(r3,bd=5,text='÷',font=('bold',17),command=div_c)
div.pack(side='left',expand=True,fill='both')



win.mainloop()
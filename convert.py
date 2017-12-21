# Program to convert logical sentences in propositional logic into CNF


import sys
import copy
#Vai ler do pipe cada coisa introduzida  e diferenciar cada um

isConjunction = False

def recursive(s):

	print('1', s)
	
	equivalence(s)

	print('2', s)

	implication(s)

	print('3', s)

	# neg=True
	# while neg:
	# 	neg=False
	# 	for i in range(0, len(sentence)):
	# 		if len(sentence[i][0])>1:
	# 			line=sentence[i]
	# 			j=0
	# 		else:
	# 			line=sentence
	# 			j=i
	# 		if line[j] == 'not' :
	# 			print('negation')
	# 			if neg_atom(line):
	# 				pass
	# 			else:
	# 				sentence[i]=negation(line[j],line[j+1])
	# 				neg=True
			


	# for i in range(0, len(sentence)):
	# 	if len(sentence[i][0])>1:
	# 		line=sentence[i]
	# 		j=0
	# 	else:
	# 		line=sentence
	# 		j=i
	# 	if line[j] == 'or' :
	# 		print('or_disj')
	# 		sentence[i]=disjunction(line[j],line[j+1],line[j+2])
	# 		disj=True
	# 		print('hhhhh',sentence[i])
	
	# 	sentence[i]=line


	# print('almost there',sentence)
	# myConditions=list()
	# not_finished=True
	# while not_finished:
	# 	not_finished=False
	# 	for i in range(0, len(sentence)):
	# 		if len(sentence[i])>1:
	# 			line=sentence[i]
	# 			j=0
	# 		else:
	# 			line=sentence
	# 			j=i
	# 		if literal(line):
	# 			print('literal_finishing')
	# 			myConditions.extend(line[j])
	# 		elif line[j] == 'or':
	# 			print('or_finishing')
	# 			myConditions.extend(line[j+1])
	# 			myConditions.extend(line[j+2])
	# 			not_finished=True
	# 		elif line[j] == 'and':
	# 			print('and_finishing')
	# 			finishing(line[j+1],line[j+2], myConditions)
	# 			not_finished=True

	# 	sentence=list(myConditions)
			


def atom(sentence):
	a = sentence[0]
	if a =='<=>' or a == '=>' or a == 'or' or a == 'and' or a== 'not':
		return False
	else:
		return True


def neg_atom(sentence):
	if sentence[0]=='not' and atom(sentence[1]):
		return True
	else:
		return False


def literal(sentence):
	if (atom(sentence) or neg_atom(sentence)):
		return True
	else:
		return False


def equivalence(sentence):
	if(sentence[0]=='<=>'):
		aux1=sentence[1]
		aux2=sentence[2]
		sentence[0] = 'and'
		sentence[1] = ('=>', aux1,aux2)
		sentence[2] = ('=>', aux2,aux1)
		return	

	for in_cond in sentence:
		if(len(in_cond)>1):
			equivalence(in_cond)


def implication(sentence):
	print('implication')
	print('aaa', sentence[0])
	if(sentence[0]=='=>'):
		aux=('not', sentence[1])
		sentence[0] = 'or'
		sentence[1] = ('not', aux)
		return	

	for in_cond in sentence:
		if(len(in_cond)>1):
			implication(in_cond)
			print('hhh')


def negation(cond, sentence):
	if atom(sentence):
		return	

	cond = ''

	if sentence[0]=='not':
		sentence = sentence[1]

	elif sentence[0] == 'or':		
		new1 = ('not', sentence[1])
		new2 = ('not', sentence[2])
		sentence = ('and',new1, new2)


	elif sentence[0]=='and':
		new1 = ('not', sentence[1])
		new2 = ('not', sentence[2])
		sentence = ('or', new1, new2)

	return (cond, sentence)


def disjunction(cond, sentence1, sentence2):

	if (literal(sentence1) and literal(sentence2)):
		return (sentence1, sentence2)


	elif (literal(sentence1)):
		new1=('or', sentence1, sentence2[1])
		new2=('or', sentence1, sentence2[2])
		sentence1=new1
		sentence2=new2
		if sentence2[0]=='and':
			cond='and'
		elif sentence2[0]=='or':
			cond='or'


	elif (literal(sentence2)):
		new1=('or', sentence2, sentence1[1])
		new2=('or', sentence2, sentence1[2])
		sentence1=new1
		sentence2=new2
		if sentence1[0]=='and':
			cond='and'
		elif sentence1[0]=='or':
			cond='or'


	elif sentence1[0]=='and':
		if sentence2[0] == 'or':
			new1=('or', sentence1[1], sentence2)
			new2=('or', sentence1[2], sentence2)
			sentence1=new1
			sentence2=new2
			cond='and'

		elif sentence2[0] == 'and':
			new1=('or', sentence1[1], sentence2[1])
			new2=('or', sentence1[2], sentence2[1])
			new3=('or', sentence1[1], sentence2[2])
			new4=('or', sentence1[2], sentence2[2])
			sentence1=('and',new1, new2)
			sentence2=('and', new3, new4)
			cond = 'and'

	elif sentence1[0]=='or':
		if sentence2[0]== 'and':
			new1=('or', sentence2[1], sentence1)
			new2=('or', sentence2[2], sentence1)
			sentence1=new1
			sentence2=new2
			cond='and'

	else:
		pass

	return(cond, sentence1, sentence2)
  
def finishing(sentence1, sentence2, myConditions):
	a=list(myConditions)
	b=list(myConditions)
	a.extend(sentence1)
	b.extend(sentence2)

	print('myConditions before clear', myConditions)
	myConditions.clear()
	print('myConditions afer clear', myConditions)
	if isinstance(a[0], list) and isinstance(b[0], list):
		myConditions.extend(a + b)
		print('myConditions.extend(a + b)', myConditions)
	elif isinstance(a[0], list):
		myConditions.extend(a + [b])
		print('myConditions.extend(a + [b])', myConditions)
	elif isinstance(b[0], list):
		myConditions.extend([a] + b)
		print('myConditions.extend([a] + b)', myConditions)
	else:
		myConditions.extend([a] + [b])
		print('myConditions.extend([a] + [b])', myConditions)




  


nlines = 0

for line in sys.stdin:
	sentence= list(eval(line))
	recursive(sentence)


	nlines = nlines + 1

#print('myFinalConditions', myFinalConditions)

# print(nconjuntions)
# if nconjuntions:
# 	myFinalConditions = myFinalConditions[0]

# print(myFinalConditions, '\n Solution:')
"""print(nlines > 1)
for condition in sentence:
	if nlines > 1:
		print(condition)
	else:
		if condition:
			if not isinstance(condition[0], list):
				print(condition)
			else:
				for e in condition:
					print(e)"""

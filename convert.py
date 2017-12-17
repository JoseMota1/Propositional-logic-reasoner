# Program to convert logical sentences in propositional logic into CNF


import sys
import copy
#Vai ler do pipe cada coisa introduzida  e diferenciar cada um

isConjunction = False

def recursive(sentence):

	equi=True
	while equi:
		equi=False
		for line in sentence:
			if line[0] == '<=>' :
				equivalence(line[0],line[1],line[2])
				equi=True

	imp=True
	while imp:
		imp=False
		for line in sentence:
			if line[0] == '=>' :
				implication(line[0],line[1],line[2])
				imp=True
	neg=True
	while neg:
		neg=False
		for line in sentence:
			if line[0] == 'not' :
				if neg_atom(line):
					pass
				else:
					negation(line[0],line[1])
					neg=True
	disj=True
	while disj:
		disj=False
		for line in sentence:
			if line[0] == 'or' :
				disjunction(line[0],line[1],line[2])
				disj=True


	myConditions=list()
	not_finished=True
	while not_finished:
		not_finished=False
		for line in sentence:
			if literal(line):
				myConditions.extend(line)
			elif line[0] == 'or':
				myConditions.extend(line[1])
				myConditions.extend(line[2])
				not_finished=True
			else:
				finishing(line[0],line[1],line[2], myConditions)
				not_finished=True

		sentence=list(myConditions)
			


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


def equivalence(cond, sentence1, sentence2):
	print('equivalence', myConditions)
	sentence1 = ('=>', sentence1,sentence2)
	sentence2 = ('=>', sentence2,sentence1)
	cond = 'and'
	


def implication(cond, sentence1, sentence2):
	print('implication', myConditions)
	new = ('not', sentence1)
	cond = 'or'
	sentence1 = new

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
	return


def disjunction(cond, sentence1, sentence2):

	if (literal(sentence1) and literal(sentence2)):
		cond = ''


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
			return

		elif sentence2[0] == 'and':
			new1=('or', sentence1[1], sentence2[1])
			new2=('or', sentence1[2], sentence2[1])
			new3=('or', sentence1[1], sentence2[2])
			new4=('or', sentence1[2], sentence2[2])
			sentence1=('and',new1, new2)
			sentence2=('and', new3, new4)
			cond = 'and'
			return

	elif sentence1[0]=='or':
		if sentence2[0]== 'and':
			new1=('or', sentence2[1], sentence1)
			new2=('or', sentence2[2], sentence1)
			sentence1=new1
			sentence2=new2
			cond='and'
			return

	else:
		pass

  
def finishing(cond,sentence1, sentence2, myConditions):
	a=list(myConditions)
	b=list(myConditions)
	a.extend(line[1])
	b.extend(line[2])

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
	sentence = eval(line)
	recursive(sentence)

	nlines = nlines + 1

#print('myFinalConditions', myFinalConditions)

# print(nconjuntions)
# if nconjuntions:
# 	myFinalConditions = myFinalConditions[0]

# print(myFinalConditions, '\n Solution:')
print(nlines > 1)
for condition in sentence:
	if nlines > 1:
		print(condition)
	else:
		if condition:
			if not isinstance(condition[0], list):
				print(condition)
			else:
				for e in condition:
					print(e)

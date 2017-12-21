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
	negation(s)

	print('4', s)
	if not literal(s):
		disjunction(s)
	
	print('5', s)

		

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
	if len(sentence)>1:
		return False
	elif len(sentence)==1:
		a = sentence[0]
		if (a =='<=>') or (a == '=>') or (a == 'or') or (a == 'and') or (a == 'not'):
			return False
		else:
			print('IS ATOM',sentence)
			return True
	else:
		return False



def neg_atom(sentence):
	if len(sentence) > 2:
		return False
	elif len(sentence) == 2 and sentence[0] == 'not' and atom(sentence[1]):
		print('NEGATOM',sentence)
		return True
	else:
		return False


def literal(sentence):
	if (atom(sentence) or neg_atom(sentence)):
		return True
	else:
		return False


def equivalence(sentence):
	if(sentence[0] == '<=>'):
		aux1 = sentence[1]
		aux2 = sentence[2]
		sentence[0] = 'and'
		sentence[1] = ['=>', aux1, aux2]
		sentence[2] = ['=>', aux2, aux1]

	for cond in sentence[1:]:
		if not literal(cond):
			equivalence(cond)

def implication(sentence):
	print('HEEEEEEEE',sentence)
	if(sentence[0] == '=>'):
		aux=['not', sentence[1]]
		sentence[0] = 'or'
		sentence[1] = aux	

	for cond in sentence[1:]:
		if not literal(cond):
			implication(cond)

def negation(sentence):
	print('negation',sentence)
	if(sentence[0] == 'not'):
		if not atom(sentence[1]):
			print('sentencemerda' , sentence[1])
			aux = sentence[1]
			print('here', aux[0])
			if aux[0] == 'not':
				print('i am here', sentence[1][1])
				sentence.remove('not')
				sentence[0] = sentence[0][1]

			elif aux[0] == 'or':		
				sentence0 = 'and'
				if neg_atom(aux[1]):
					sentence1 = aux[1][1]
				else:
					sentence1 = ['not', [aux[1]]]
				if neg_atom(aux[2]):
					sentence2 = aux[2][1]
				else:
					sentence2 = ['not', [aux[2]]]

				sentence[0]='and'
				sentence[1]=sentence1
				sentence.extend(sentence2)

			elif aux[0]=='and':
				if neg_atom(aux[1]):
					sentence1 = aux[1][1]
				else:
					sentence1 = ['not', [aux[1]]]
				if neg_atom(aux[2]):
					sentence2 = aux[2][1]
				else:
					sentence2 = ['not', [aux[2]]]

				sentence[0]='or'
				sentence[1]=sentence1
				sentence.extend(sentence2)
	
	for cond in sentence[1:]:
		if not literal(cond):
			negation(cond)
		


def disjunction(sentence):
	if(sentence[0] == 'or'):
		if (literal(sentence[1]) and literal(sentence[2])):
			return

		elif (literal(sentence[1])):
			new1 = ['or', sentence[1], sentence[2][1]]
			new2 = ['or', sentence[1], sentence[2][2]]

			if sentence[2][0] == 'and':
				sentence[0] = 'and'
			elif sentence[2][0] == 'or':
				sentence[0] = 'or'

			sentence[1] = new1
			sentence[2] = new2


		elif (literal(sentence[2])):
			new1 = ['or', sentence[2], sentence[1][1]]
			new2 = ['or', sentence[2], sentence[1][2]]

			if sentence[1][0]=='and':
				sentence[0] = 'and'
			elif sentence[1][0]=='or':
				sentence[0] = 'or'

			sentence[1] = new1
			sentence[2] = new2

		elif sentence[1][0] =='and':
			if sentence[2][0] == 'or':
				new1 = ['or', sentence[1][1], sentence[2]]
				new2 = ['or', sentence[1][2], sentence[2]]
				sentence[0] = 'and'
				sentence[1] = new1
				sentence[2] = new2

			elif sentence2[0] == 'and':
				new1=['or', sentence[1][1], sentence[2][1]]
				new2=['or', sentence[1][2], sentence[2][1]]
				new3=['or', sentence[1][1], sentence[2][2]]
				new4=['or', sentence[1][2], sentence[2][2]]
				sentence1=['and',new1, new2]
				sentence2=['and', new3, new4]
				sentence[0] = 'and'
				sentence[1] = sentence1
				sentence[2] = sentence2

		elif sentence1[0]=='or':
			if sentence2[0]== 'and':
				new1 = ['or', sentence[2][1], sentence[1]]
				new2 = ['or', sentence[2][2], sentence[1]]
				sentence[0] = 'and'
				sentence[1] = new1
				sentence[2] = new2

	
	for cond in sentence[1:]:	
		if not literal(cond):
			disjunction(cond)


  
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
	l = list(line)
	s = ['[' if x == '(' else ']' if x == ')' else x for x in l]
	new_line = "".join(s)

	sentence= list(eval(new_line))
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

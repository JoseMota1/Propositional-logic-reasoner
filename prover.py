import sys
import itertools

def readfile():
	myConditions = []
	fp = open('cnf.txt', 'r')
	for line in sys.stdin:
		sentence = eval(line)
		myConditions.append(sentence)
	#simplifi_2(myConditions)
	return myConditions

def solve(myConditions, r, visited):
	if all(visited):
		return False

	for i in range(len(myConditions)):
		#print('1', myConditions[i], '2', r)
		newR,resolved = resolution(myConditions[i], r)
		#print(newR, resolved)
		try:
			visited[i] = True
		except Exception as e:
			return False

		if newR in myConditions:
		#	print('Exists already')
			continue
		elif resolved and not len(newR):
			return True
		elif resolved:
			#print('Append')
			myConditions.append(r)
			if solve(myConditions, newR, visited):
				return True
		else:
			continue

	#print('Back')
	return False

def hasnegation(sentence,sentence1):
	a=set(sentence)
	b=set(sentence1)
	aux_a=nega(sentence)
	aux_b=nega(sentence1)
	if a.issubset(aux_b):
		return True
	if b.issubset(aux_a):
		return True
	return False


def nega(sentence):
	c=set(sentence)
	for e in sentence:							#Se encontrar a sentence1 na sentence2 vai remover os dois e retorna a lista
		if len(e)>1:
			aux=e[1]
			c.remove(e)
			c.add(aux)
		else:
			aux=e
			c.remove(e)
			c.add(('not', aux))
	return list(c)


def resolution(sentence1, sentence2):
	if isinstance(sentence1, list):
		a = set(sentence1)					#converte para sets
	else:
		a = set([sentence1])
	if isinstance(sentence2, list):
		b = set(sentence2)					#converte para sets
	else:
		b = set([sentence2])

	c = a|b
	resolved = False
	for e in a:						#Se encontrar a sentence1 na sentence2 vai remover os dois e retorna a lista
		if len(e)>1:
			if e[1] in b:
				try:
					c.remove(e[1])
					c.remove(e)
					resolved = True
				except Exception as e:
					pass
		else:
			if ('not', e) in b:					#Se encontrar a negação e o normal em ambas as listas então remove e retorna a lista
				try:
					c.remove(('not', e))
					c.remove(e)
					resolved = True
				except Exception as e:
					pass

	return list(c), resolved


def main():
	myConditions = readfile()
	print('KB:', myConditions)
	alpha = myConditions[-1]
	#print('negated alpha:', alpha)
	visited = [False]*(len(myConditions))
	visited[-1] = True
	if solve(list(myConditions[:-1]), alpha, visited):
		print("True")
	else :
		print("False")


def simplifi_2(myConditions):
	#tautologies	can	be	removed
	#clauses	that	contain	both	a	literal	and	its	nega.on
	final=[]
	for sentence in myConditions:
		tautology = True
		for e in sentence:
			if len(e)>1:
				if e[1] in sentence:
					continue
				else:
					tautology = False
			else:
				if ('not', e) in sentence:
					continue
				else:
					tautology = False	
					
		if not tautology:
			final.append(sentence)
			
	return final


def simplifi_3(myConditions):
	#tautologies	can	be	removed
	#clauses	that	contain	both	a	literal	and	its	nega.on
	final=[]
	i=0
	for sentence in myConditions:
		aux_1=set(myConditions[i])
		aux_2=set(sentence)
		if aux_1.issubset(aux_2):
			final.append(myConditions[i])
		if aux_2.issubset(aux_1):
			final.append(sentence)
		else:
			final.append(sentence)
	return final


if __name__ == "__main__":
	main()

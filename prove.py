import sys
import itertools

# def readfile():
 # myConditions=[]
 # fp = open('cnf.txt', 'r')
 # for line in fp:
	 # #sentence = eval(line)
	 # myConditions.append(line)
 # return myConditions

myConditions=eval("['B'],[('not','B')]")

# def permutati(myConditions):
	# permutatio=[]
	# for L in range(0, len(myConditions)):
		# for subset in itertools.Permunations(myConditions, L):
			# print(subset)

def solve(myConditions, r, visited):
	if all(visited):
		return False
	for i in range(len(myConditions)):
		if hasNegation(myConditions[i],r):
			newR, resolved = resolution(myConditions[i], r)
			visited[i] = True
			if not len(newR):
				return True
			else:
				myConditions.append(r)
				return solve(myConditions, newR, visited)
	return False

def hasNegation(sentence,sentence1):
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
			

			
#def find_negation(sentence1,sentence2)

def resolution(sentence1,sentence2):
	a = set(sentence1)					#converte para sets	
	b = set(sentence2)					#converte para sets
	c = set()
	#print('a', a, 'b', b)
	resolved = False
	for e in a:							#Se encontrar a sentence1 na sentence2 vai remover os dois e retorna a lista 
		if len(e)>1:
			if e[1] in b:
				c = a|b
				print('c', c)
				c.remove(e[1])
				c.remove(e)
				resolved = True
		else:
			if ('not', e) in b:					#Se encontrar a negação e o normal em ambas as listas então remove e retorna a lista
				c = a|b
				print('c', c)
				c.remove(('not', e))
				c.remove(e)
				resolved = True
	return list(c), resolved
	

#myConditions=eval("[('not','A'),'B'],[('not','B'),'A'],'A','B'")
def main():
	alpha = myConditions[-1]
	visited = [False]*(len(myConditions))
	visited[-1] = True
	if solve(list(myConditions[:-1]), [alpha], visited):
		print("Proved")
	else :
		print("Não consegui")

# def simplifi_1(myConditions)
	# #remove	a	clause	C	if	it	contains	a	literal	that	is	not	
	# #complementary	with	any	other	in	the	remaining	clauses
	# for e in myConditions	
		# if 

# def simplifi_2(myConditions)
	# final=[]
# #tautologies	can	be	removed	
# #clauses	that	contain	both	a	literal	and	its	nega.on	
	# for a in myConditions
	  # aux=set(a)
		# for cada in aux
			# if len(cada)==1
				# if ('not', cada) in aux:	
					# aux.remove(('not', e))
					# aux.remove(e)
					# list(aux)
					# final.append(aux)
			# if len(cada)>1
				# if cada in aux:	
					# aux.remove(('not', cada))
					# aux.remove(cada)
					# list(aux)
					# final.append(aux)

# def simplifi_3(myConditions)
# #remove	clauses	that	are	implied	by	other	clauses	
# #i.e.,	if	a	clause	is	subset	of	another,	then	the	largest	clause	can	be	eliminated	

# def simplifi_4(myConditions)
# #if	a	literal	occurs	more	than	once	in	a	clause,	then	the	
# #duplica.on	can	be	eliminated	(factoring)
	# for a in myConditions	
		# aux=set(a)
		# aux_list=list(aux)
	# return aux_list


#print(hasNegation(myConditions[0],myConditions[2]))
#print(resultado(myConditions[0],myConditions[1]))
main()
#print(hasNegation(myConditions[0],myConditions[1]))
#print(nega(myConditions[1]))








	





	


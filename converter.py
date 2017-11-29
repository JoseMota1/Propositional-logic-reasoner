# Program to convert logical sentences in propositional logic into CNF


import sys
#Vai ler do pipe cada coisa introduzida  e diferenciar cada um 


myConditions=[];
myprovConditions=[]; # Auxiliar when reiterating


for lines in sys.stdin:
	sentences = eval(lines) 
	principal = 1
	reit(sentences)




def reit(line)
	if line[1]='<=>'
		equivalence(line[2],line[3])
	if line[1]= '=>' 
		implication(line[2],line[3])
	if line[1]='or' 
		disjunction(line[2],line[3])		
	if line[1]='and'
		conjunction(line[2],line[3])
	if line[1]='not' 
		negation(line[2])
return



def atom(sentence)
	if len(sentence)>1 
		return FALSE
	elif len(sentence)==1
		myConditions.append (sentence)
		return TRUE
	return



def equivalence(sentence1, sentence2)
	implication (sentence1,sentence2)	
	implication (sentence2,sentence1)
	return
	
def implication(sentence1, sentence2)
	disjunction(('not', sentence1), sentence2);
	return 

def disjuntion(sentence1, sentence2)
	if atom(sentence1) && atom(sentence2)
		if principal == 1
			myConditions.append([sentence1, sentence2]) # not sure this is how its done
		else 
			myprovConditions.append([sentence1, sentence2]) # vai dar merda aqui
	else
		distribution(sentence1, sentence2)
	return


def negation(sentence):

	return 

def distribution(sentence1, sentence2):
	principal=principal+1
	reit(sentence1)
	reit(sentence2)	
	principal = principal-1





	return
	


def conjunction(node):
	

	return 
	
	
	

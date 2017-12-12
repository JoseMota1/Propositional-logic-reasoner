# Propositional-logic-reasoner

equi.txt sol:
(('not', 'A') , 'B')
(('not', 'B') , 'A')

equinot.txt sol:
('A' , 'G')
(('not', 'G') , ('not', 'A'))

andnegated.txt sol: 
()

ornegated.txt sol: 
('I' , ('not', 'I'))

imp.txt sol: 
(('not', 'a'), 'b')

example1.txt sol:
('not', 'A')
('D', 'B', 'C')
(('not', E), ('not', F) , 'G')

example2.txt sol: NOT WORKINGGGGG
('H', 'J')
(('not', 'I'), 'J')
(('not', 'H'),('not', 'J'),'I')

example3.txt sol:
(('not', 'H') , 'I')
'J'

example4.txt sol:
(('not', 'H'), ('not', 'I'), 'J')
(('not', 'J'), 'H')
(('not', 'J'), 'I')

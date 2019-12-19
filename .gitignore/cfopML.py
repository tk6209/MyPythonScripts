from sklearn import tree

Pacote = 0	
Revenda = 1	
Estadual = 0	
InterEstadual = 1	
Nacional = 0	
Importado = 1	
MO0 = Nacional	
MO1 = Importado	
MO2 = Importado	
MO3 = Importado	
MO4 = Nacional	
MO5 = Nacional	
MO6 = Nacional	
MO7 = Nacional	
MO8 = Importado	


CFOP = [[Revenda,MO6,InterEstadual],[Revenda,MO6,Estadual],[Pacote,MO0,Estadual],[Pacote,MO0,InterEstadual],[Pacote,MO1,InterEstadual]]
resultado = ['6102/01','5102/01','6101/01','5101/01','5102/01']

clf = tree.DecisionTreeClassifier()
clf = clf.fit(CFOP,resultado)

i = "IS"
MU = str( input("Informe o MU (Pacote = 0, Revenda = 1): "))
#print MU
MO = str(input ("Informe o MO (0,4,5,6,7) = 0 & MO (1,2,3,8) = 1 : "))
#print MO
OrDs = str(input ("Informe se Estadual(0) ou InterEstadual(1): "))
#print OrDs

concatResult = i + MU + MO + OrDs
#print concatResult
resultadoFinal = clf.predict([[MU,MO,OrDs]])


if concatResult == "IS101":
	print ("CFOP 6102/01")
elif concatResult == "IS100":
	print ("CFOP 5102/01")
elif concatResult == "IS001":
	print ("CFOP 6101/01")	
elif concatResult =="IS111":
	print ("CFOP 5102/01")
else: 
	print ("CFOP 5101/01")



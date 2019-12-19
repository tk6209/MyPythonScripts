from sklearn import tree

lisa = 1
irregular = 1
maca = 1  
laranja = 0 


pomar = [[150,lisa],[130,lisa],[210,lisa],[180,irregular],[160,irregular],[210,irregular]]
resultado = [maca,maca,maca,laranja,laranja,laranja]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(pomar,resultado)


peso = input("Informe o peso: ")
superficie = input ("Informe a superficie lisa use (1) para irregular (0): ")
resultadoFinal = clf.predict([[peso, superficie]])

if resultadoFinal == 1:
	print ("eh uma Maca")
else:
	print ("eh uma Laranja")

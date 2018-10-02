class arbolN():
	def __init__(self, valor, hojas):
		self.valor=valor;
		self.hojas=hojas;

	def buscar(busqueda, arbol,i):
		if arbol==[]:
			return arbolN.buscar(busqueda, arbol.hojas[1:],i)
		elif arbol.valor==busqueda:
			return True
		else:
			print(i)
			i=i+1
			return arbolN.buscar(busqueda, arbol.hojas[0],i) #or arbolN.buscar2(busqueda, arbol.hojas[1:])

	def buscar2(busqueda, arbol):
		if arbol==[]:
			return False
		else:
			return buscar(busqueda, arbol[0]) or buscar2(busqueda, arbol[1:])

a1 = arbolN(2,[arbolN(4,[arbolN(12,[]),arbolN(24,[]),arbolN(40,[])]),arbolN(8,[arbolN(16,[]),arbolN(32,[])]),arbolN(5,[arbolN(25,[]),arbolN(50,[])])])
#a1 = arbolN(2,[arbolN(4,[arbolN(12),arbolN(24),arbolN(40)]),arbolN(8,[arbolN(16),arbolN(32)]),arbolN(5,[arbolN(25),arbolN(50)])])

print(arbolN.buscar(8,a1,1))
class arbolN():
	def __init__(self, valor, hojas):
		self.valor=valor;
		self.hojas=hojas;

def buscar(busqueda, arbol):
	if arbol.valor==busqueda:
		return True
	elif arbol.hojas == []:
		return False
	else:
		return buscar(busqueda, arbol.hojas[0]) or buscar2(busqueda, arbol.hojas[1:])

def buscar2(busqueda, arbol):
	if arbol==[]:
		return False
	else:
		return buscar(busqueda, arbol[0]) or buscar2(busqueda, arbol[1:])

a1 = arbolN(2,[arbolN(4,[arbolN(12,[]),arbolN(24,[]),arbolN(40,[])]),arbolN(8,[arbolN(16,[]),arbolN(32,[])]),arbolN(5,[arbolN(25,[]),arbolN(50,[])])])

print(buscar(24,a1))

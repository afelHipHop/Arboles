class Nodo:
	def _init_(self, numero=None, izq=None, der=None):
		self.numero = numero
		self.izq = izq
		self.der = der

	def _str_(self):
		return "%s" %(self.numero)

class aBinario:
	def _init_(self):
		self.raiz=None

	def Agregar(self, elemento):
		if self.raiz == None:
			self.raiz = elemento
		else:
			aux = self.raiz
			padre = None
			while aux != None:
				padre = aux
				if int(elemento.numero) >= int(aux.numero):
					aux = aux.der
				else: 
					aux = aux.izq
			if int(elemento.numero) >= int(padre.numero):
			 	padre.der = elemento
			else:
		 		padre.izq = elemento

	def PreOrden(self, elemento):
		if elemento != None:
			print(elemento)
			self.preorden(elemento.izq)
			self.preorden(elemento.der)

	def PostOrden(self, elemento):
		if elemento != None:
			self.postorden(elemento.izq)
			self.postorden(elemento.der)
			print(elemento)

	def InOrden(self, elemento):
		if elemento != None:
			self.inorden(elemento.izq)
			print(elemento)
			self.inorden(elemento.der)

	def getRaiz(self):
		return self.raiz

if _name_ == "_main_":
	ab = aBinario()
	while(True):
		print("---Menu---\n"+
			"1. Agregar\n"+
			"2. PreOrden\n"+
			"3. PostOrden\n"+
			"4. InOrden")
		num = input("Ingrese la opcion: ")
		if num == "1":
			nod = Nodo()
			numero = input("Ingrese el numero: ")
			ab.agregar(nod)
		elif num == "2":
			print ("Imprimiendo por Pre-Orden")
			ab.PreOrden(ab.getRaiz())
		elif num == "3":
			print ("Imprimiendo por Post-Orden")
			ab.PostOrden(ab.getRaiz())
		elif num == "4":
			print ("Imprimiendo por In-Orden")
			ab.InOrden(ab.getRaiz())

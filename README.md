# Arboles
### Samuel Holguin 20161020044
### Andres Ramirez 20161020077
### Kevin Rocha 20161020086
## arboles:
Los árboles se usan en muchas áreas de las ciencias de la computación, incluyendo sistemas operativos, gráficos, sistemas de bases de datos y redes de computadoras, los arboles se componen de una raiz(inicio), ramas(conecciones intermedias) y hojas(final). 
## Propiedades de los arboles
* los árboles son jerárquicos, es decir que los árboles están estructurados en capas con las cosas más generales cerca de la parte superior y las cosas más específicas cerca de la parte inferior. La parte superior de la jerarquía es el Reino, la siguiente capa del árbol (los “hijos” de la capa superior) es el Filo, luego está la Clase, y así sucesivamente.
* Todos los hijos de un nodo son independientes de los hijos de otro nodo, es decir tomando como ejemplo la familia, si un niño tiene un juguete, esto no significa que su primo tambien lo tenga pues cad auno pertenece a una diferente familia de ramas.
* Cada nodo hoja es único. Podemos especificar una ruta desde la raíz del árbol hasta una hoja que identifique de manera única a cada especie en el reino animal; Por ejemplo, Animalia → Cordados → Mamíferos → Carnívoros → Félidos → Felis → Domestica.
* Otra propiedad importante de los árboles, derivada de su naturaleza jerárquica, es que usted puede mover secciones enteras de un árbol (llamada subárbol) a una posición diferente en el árbol sin afectar los niveles inferiores de la jerarquía.
## implementación
Teniendo en mente las definiciones de la sección previa, podemos usar las siguientes funciones para crear y manipular un árbol binario:

ArbolBinario() crea una nueva instancia de un árbol binario.
obtenerHijoIzquierdo() devuelve el árbol binario correspondiente al hijo izquierdo del nodo actual.
obtenerHijoDerecho() devuelve el árbol binario correspondiente al hijo derecho del nodo actual.
asignarValorRaiz(valor) almacena el objeto del parámetro valor en el nodo actual.
obtenerValorRaiz() devuelve el objeto almacenado en el nodo actual.
insertarIzquierdo(valor) crea un nuevo árbol binario y lo instala como el hijo izquierdo del nodo actual.
insertarDerecho(valor) crea un nuevo árbol binario y lo instala como el hijo derecho del nodo actual.
La decisión clave en la implementación de un árbol es escoger una buena técnica de almacenamiento interno. Python nos permite dos posibilidades muy interesantes, así que examinaremos ambas antes de escoger una de ellas. La primera técnica se denomina “lista de listas”, a la segunda técnica la llamaremos de “nodos y referencias”.

#Andres Felipe Alfonso Viviescas-2162063
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

class Arbol:
    def __init__(self):
        self.raiz = None
    
    def insertar_nodo(self, padre_valor, valor):
        if not self.raiz:
            self.raiz = Nodo(valor)
            return True
        
        padre = self._buscar_nodo(self.raiz, padre_valor)
        if padre:
            padre.hijos.append(Nodo(valor))
            return True
        return False
    
    def _buscar_nodo(self, nodo_actual, valor):
        if nodo_actual.valor == valor:
            return nodo_actual
        
        for hijo in nodo_actual.hijos:
            encontrado = self._buscar_nodo(hijo, valor)
            if encontrado:
                return encontrado
        return None
    
    # a) Peso del árbol (cantidad total de nodos)
    def peso(self):
        return self._contar_nodos(self.raiz) if self.raiz else 0
    
    def _contar_nodos(self, nodo):
        if not nodo:
            return 0
        total = 1  # Contamos el nodo actual
        for hijo in nodo.hijos:
            total += self._contar_nodos(hijo)
        return total
    
    # b) Orden (grado del árbol - máximo de hijos que tiene un nodo)
    def orden(self):
        return self._max_grado(self.raiz) if self.raiz else 0
    
    def _max_grado(self, nodo):
        if not nodo:
            return 0
        max_grado = len(nodo.hijos)
        for hijo in nodo.hijos:
            grado_hijo = self._max_grado(hijo)
            if grado_hijo > max_grado:
                max_grado = grado_hijo
        return max_grado
    
    # c) Altura (longitud del camino más largo desde la raíz a una hoja)
    def altura(self):
        return self._calcular_altura(self.raiz) if self.raiz else 0
    
    def _calcular_altura(self, nodo):
        if not nodo or not nodo.hijos:
            return 0
        alturas = []
        for hijo in nodo.hijos:
            alturas.append(self._calcular_altura(hijo))
        return 1 + max(alturas)
    
    def mostrar_arbol(self):
        if not self.raiz:
            print("Árbol vacío")
            return
        self._mostrar_subarbol(self.raiz, 0)
    
    def _mostrar_subarbol(self, nodo, nivel):
        print("  " * nivel + "└──", nodo.valor)
        for hijo in nodo.hijos:
            self._mostrar_subarbol(hijo, nivel + 1)

def menu():
    arbol = Arbol()
    while True:
        print("\n--- MENÚ ---")
        print("1. Insertar nodo raíz")
        print("2. Insertar nodo hijo")
        print("3. Mostrar árbol")
        print("4. Peso del árbol")
        print("5. Orden del árbol")
        print("6. Altura del árbol")
        print("0. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            valor = input("Ingrese el valor para la raíz: ")
            arbol = Arbol()
            arbol.raiz = Nodo(valor)
            print("Raíz creada exitosamente")
        
        elif opcion == "2":
            if not arbol.raiz:
                print("Primero debe crear la raíz")
                continue
            padre = input("Ingrese el valor del nodo padre: ")
            valor = input("Ingrese el valor del nuevo nodo: ")
            if arbol.insertar_nodo(padre, valor):
                print("Nodo insertado exitosamente")
            else:
                print("No se encontró el nodo padre")
        
        elif opcion == "3":
            print("\nEstructura del árbol:")
            arbol.mostrar_arbol()
        
        elif opcion == "4":
            print(f"Peso del árbol: {arbol.peso()} nodos")
        
        elif opcion == "5":
            print(f"Orden del árbol: {arbol.orden()} (máximo de hijos por nodo)")
        
        elif opcion == "6":
            print(f"Altura del árbol: {arbol.altura()} niveles")
        
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida")

if __name__ == "__main__":
    menu()

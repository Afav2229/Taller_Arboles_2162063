from bigtree import Node, tree_to_dot

# Crear nodo raíz (abuelo)
abuelo = Node("Juan", edad=80)

# Crear hijos del abuelo
padre1 = Node("Carlos", edad=50, parent=abuelo)
padre2 = Node("María", edad=48, parent=abuelo)
padre3 = Node("Luis", edad=45, parent=abuelo)

# Crear nietos (hijos de Carlos)
hijo1 = Node("Ana", edad=25, parent=padre1)
hijo2 = Node("Pedro", edad=22, parent=padre1)
hijo3 = Node("Sofía", edad=20, parent=padre1)

# Crear nietos (hijos de María)
hijo4 = Node("Diego", edad=18, parent=padre2)
hijo5 = Node("Laura", edad=15, parent=padre2)

# Mostrar árbol en consola
abuelo.show(attr_list=["edad"])
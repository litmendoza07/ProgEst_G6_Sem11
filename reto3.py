def crear_nodo(valor):
    return {"valor": valor, "izq": None, "der": None}


def insertar(raiz, valor):
    if raiz is None:
        return crear_nodo(valor)
    if valor < raiz["valor"]:
        raiz["izq"] = insertar(raiz["izq"], valor)
    elif valor > raiz["valor"]:
        raiz["der"] = insertar(raiz["der"], valor)
    return raiz


def minimo(nodo):
    while nodo["izq"] is not None:
        nodo = nodo["izq"]
    return nodo


def eliminar(raiz, valor):
    if raiz is None:
        return None

    if valor < raiz["valor"]:
        raiz["izq"] = eliminar(raiz["izq"], valor)
    elif valor > raiz["valor"]:
        raiz["der"] = eliminar(raiz["der"], valor)
    else:
        if raiz["izq"] is None:
            return raiz["der"]
        if raiz["der"] is None:
            return raiz["izq"]

        sucesor = minimo(raiz["der"])
        raiz["valor"] = sucesor["valor"]
        raiz["der"] = eliminar(raiz["der"], sucesor["valor"])

    return raiz


def inorden(raiz):
    if raiz is None:
        return []
    return inorden(raiz["izq"]) + [raiz["valor"]] + inorden(raiz["der"])


raiz = None
for valor in [50, 30, 70, 20, 40, 60, 80]:
    raiz = insertar(raiz, valor)

for caso in (20, 30, 50):
    prueba = None
    for valor in [50, 30, 70, 20, 40, 60, 80]:
        prueba = insertar(prueba, valor)
    prueba = eliminar(prueba, caso)
    assert caso not in inorden(prueba)

raiz = eliminar(raiz, 50)
assert inorden(raiz) == [20, 30, 40, 60, 70, 80]
print("Después de eliminar 50:", *inorden(raiz))

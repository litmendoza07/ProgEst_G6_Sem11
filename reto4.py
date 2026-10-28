def crear_nodo(codigo):
    return {"codigo": codigo, "izq": None, "der": None}


def insertar(raiz, codigo):
    if raiz is None:
        return crear_nodo(codigo)
    if codigo < raiz["codigo"]:
        raiz["izq"] = insertar(raiz["izq"], codigo)
    elif codigo > raiz["codigo"]:
        raiz["der"] = insertar(raiz["der"], codigo)
    return raiz


def buscar(raiz, codigo):
    if raiz is None:
        return False
    if codigo == raiz["codigo"]:
        return True
    if codigo < raiz["codigo"]:
        return buscar(raiz["izq"], codigo)
    return buscar(raiz["der"], codigo)


def inorden(raiz):
    if raiz is None:
        return []
    return inorden(raiz["izq"]) + [raiz["codigo"]] + inorden(raiz["der"])


def minimo(nodo):
    while nodo["izq"] is not None:
        nodo = nodo["izq"]
    return nodo


def retirar(raiz, codigo):
    if raiz is None:
        return None
    if codigo < raiz["codigo"]:
        raiz["izq"] = retirar(raiz["izq"], codigo)
    elif codigo > raiz["codigo"]:
        raiz["der"] = retirar(raiz["der"], codigo)
    else:
        if raiz["izq"] is None:
            return raiz["der"]
        if raiz["der"] is None:
            return raiz["izq"]
        sucesor = minimo(raiz["der"])
        raiz["codigo"] = sucesor["codigo"]
        raiz["der"] = retirar(raiz["der"], sucesor["codigo"])
    return raiz


raiz = None
for codigo in [105, 87, 120, 43, 95, 111, 134]:
    raiz = insertar(raiz, codigo)

assert inorden(raiz) == [43, 87, 95, 105, 111, 120, 134]
assert buscar(raiz, 95)
assert not buscar(raiz, 999)
raiz = retirar(raiz, 105)
assert inorden(raiz) == [43, 87, 95, 111, 120, 134]
print("Códigos ordenados:", *inorden(raiz))
print("Buscar 95:", buscar(raiz, 95))
print("Buscar 999:", buscar(raiz, 999))

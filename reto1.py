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


def preorden(raiz):
    if raiz is None:
        return []
    return [raiz["valor"]] + preorden(raiz["izq"]) + preorden(raiz["der"])


def postorden(raiz):
    if raiz is None:
        return []
    return postorden(raiz["izq"]) + postorden(raiz["der"]) + [raiz["valor"]]


raiz = None
for valor in [50, 30, 70, 20, 40, 60, 80]:
    raiz = insertar(raiz, valor)

assert preorden(raiz) == [50, 30, 20, 40, 70, 60, 80]
assert postorden(raiz) == [20, 40, 30, 60, 80, 70, 50]
print("Preorden:", *preorden(raiz))
print("Postorden:", *postorden(raiz))

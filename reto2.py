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


def contar_nodos(raiz):
    if raiz is None:
        return 0
    return 1 + contar_nodos(raiz["izq"]) + contar_nodos(raiz["der"])


def altura(raiz):
    if raiz is None:
        return -1
    return 1 + max(altura(raiz["izq"]), altura(raiz["der"]))


raiz = None
for valor in [50, 30, 70, 20, 40, 60, 80]:
    raiz = insertar(raiz, valor)

assert contar_nodos(raiz) == 7
assert altura(raiz) == 2
assert contar_nodos(None) == 0
assert altura(None) == -1
print("Cantidad de nodos:", contar_nodos(raiz))
print("Altura:", altura(raiz))

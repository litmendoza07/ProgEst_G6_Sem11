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


def recorrido_preorden(raiz):
    """Raíz, subárbol izquierdo y subárbol derecho."""
    if raiz is None:
        return []

    return (
        [raiz["valor"]]
        + recorrido_preorden(raiz["izq"])
        + recorrido_preorden(raiz["der"])
    )


def recorrido_postorden(raiz):
    """Subárbol izquierdo, subárbol derecho y raíz."""
    if raiz is None:
        return []

    return (
        recorrido_postorden(raiz["izq"])
        + recorrido_postorden(raiz["der"])
        + [raiz["valor"]]
    )


raiz = None
for numero in [50, 30, 70, 20, 40, 60, 80]:
    raiz = insertar(raiz, numero)

preorden = recorrido_preorden(raiz)
postorden = recorrido_postorden(raiz)

print("Preorden:", *preorden)
print("Postorden:", *postorden)

assert preorden == [50, 30, 20, 40, 70, 60, 80]
assert postorden == [20, 40, 30, 60, 80, 70, 50]

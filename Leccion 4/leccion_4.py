import pdb
pdb.set_trace()

# %%
lista_d_listas = [[1, 2, 3], [69, 5, 7], [2, 5, 7, 9]]

max_numero_lista = [max(x) for x in lista_d_listas]

print(max_numero_lista)

# %%


def es_primo(x) -> bool:
    for i in range(2, x):
        if (x % i) == 0:
            return False
    return True


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
numeros_primos = list(filter(es_primo, numeros))
print(numeros_primos)

# %%

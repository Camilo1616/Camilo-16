
def siglo(anho):
    return (anho + 99) // 100

def primer_anho(siglo):
    return (siglo - 1) * 100 + 1

print("Ingrese un año (número positivo):")
try:
    anho = int(input())

    siglo_calculado = siglo(anho)
    primer_anho_siglo = primer_anho(siglo_calculado)

    print(f"El año {anho} pertenece al siglo {siglo_calculado}")
    print(f"El primer año del siglo {siglo_calculado} es {primer_anho_siglo}")
except ValueError:
    print("Por favor, ingrese un número positivo.")
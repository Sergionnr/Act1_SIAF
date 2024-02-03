import random
import hashlib
import math

def convertir_a_entero(valor):
    try:
        entero_resultante = int(valor)
        return entero_resultante
    except ValueError:
        return None

# g y primo p
g = 2
p = (2^1536)-(2^1472)-(1)+(2^64)*(((2^1406)*(math.pi))+(741804))
p = convertir_a_entero(p)

# llaves de alice y bob
a = random.randint(2**255, 2**256)
b = random.randint(2**255, 2**256)

# Simulación de cambio de llaves
A = pow(g, a, p)
B = pow(g, b, p)

# Calcular llave secreta s
s1 = pow(B, a, p)
s2 = pow(A, b, p)

# Convertir llaves a bytes
s1_bytes = s1.to_bytes((s1.bit_length() + 7) // 8, 'big')
s2_bytes = s2.to_bytes((s2.bit_length() + 7) // 8, 'big')

# Uso de algoritmo SHA-256
hash_s1 = hashlib.sha256(s1_bytes).hexdigest()
hash_s2 = hashlib.sha256(s2_bytes).hexdigest()

# Verificar igualdad de llaves
if hash_s1 == hash_s2:
    print("✅ Llaves iguales")
else:
    print("❌ Llaves distintas")

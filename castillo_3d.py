import random
import math

vertices = []
faces = []

def crear_cubo(x, y, z, ancho, largo, alto):
    inicio = len(vertices) + 1

    vertices.extend([
        (x, y, z),
        (x + ancho, y, z),
        (x + ancho, y + largo, z),
        (x, y + largo, z),

        (x, y, z + alto),
        (x + ancho, y, z + alto),
        (x + ancho, y + largo, z + alto),
        (x, y + largo, z + alto)
    ])

    caras = [
        (inicio, inicio+1, inicio+2, inicio+3),
        (inicio+4, inicio+5, inicio+6, inicio+7),
        (inicio, inicio+1, inicio+5, inicio+4),
        (inicio+1, inicio+2, inicio+6, inicio+5),
        (inicio+2, inicio+3, inicio+7, inicio+6),
        (inicio+3, inicio, inicio+4, inicio+7)
    ]

    faces.extend(caras)

# Generar castillo/fortaleza con torres estratégicamente posicionadas
print("Generando castillo 3D...")

# Muros perimetrales
for i in range(8):
    crear_cubo(i * 2, 0, 0, 1.8, 1, 8)
    crear_cubo(i * 2, 14, 0, 1.8, 1, 8)
    crear_cubo(0, i * 2, 0, 1, 1.8, 8)
    crear_cubo(14, i * 2, 0, 1, 1.8, 8)

# Torres en las esquinas - más altas
torres = [(0, 0), (14, 0), (0, 14), (14, 14)]
for x, y in torres:
    crear_cubo(x, y, 0, 2, 2, 20)

# Torres intermedias
torres_inter = [(7, 0), (7, 14), (0, 7), (14, 7)]
for x, y in torres_inter:
    crear_cubo(x, y, 0, 2, 2, 15)

# Estructura central del castillo
crear_cubo(6, 6, 0, 4, 4, 12)

# Guardar OBJ
with open("castillo.obj", "w") as f:
    for v in vertices:
        f.write(f"v {v[0]} {v[1]} {v[2]}\n")

    for cara in faces:
        f.write(
            f"f {cara[0]} {cara[1]} {cara[2]} {cara[3]}\n"
        )

print("✓ Castillo 3D generado: castillo.obj")
print(f"  - Vértices: {len(vertices)}")
print(f"  - Caras: {len(faces)}")

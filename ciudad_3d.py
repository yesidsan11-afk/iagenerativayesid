import random

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

# Generar ciudad procedural con 10x10 edificios
print("Generando ciudad procedural...")
for x in range(10):
    for y in range(10):
        altura = random.uniform(2, 15)
        
        crear_cubo(
            x * 2,
            y * 2,
            0,
            1.5,
            1.5,
            altura
        )

# Guardar OBJ
with open("ciudad.obj", "w") as f:
    for v in vertices:
        f.write(f"v {v[0]} {v[1]} {v[2]}\n")

    for cara in faces:
        f.write(
            f"f {cara[0]} {cara[1]} {cara[2]} {cara[3]}\n"
        )

print("✓ Ciudad 3D generada: ciudad.obj")
print(f"  - Vértices: {len(vertices)}")
print(f"  - Caras: {len(faces)}")

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

# Generar montaña/pirámide estratificada
print("Generando montaña 3D (pirámide)...")

center_x = 9
center_y = 9

# Crear capas de la pirámide
for nivel in range(10):
    altura_bloque = 2
    distancia = 9 - nivel
    
    # Crear cuadrado en cada nivel, reduciendo el tamaño
    for x in range(distancia):
        for y in range(distancia):
            x_pos = center_x - distancia + x * 1.8
            y_pos = center_y - distancia + y * 1.8
            z_pos = nivel * altura_bloque
            
            crear_cubo(x_pos, y_pos, z_pos, 1.6, 1.6, altura_bloque)

# Guardar OBJ
with open("montaña.obj", "w") as f:
    for v in vertices:
        f.write(f"v {v[0]} {v[1]} {v[2]}\n")

    for cara in faces:
        f.write(
            f"f {cara[0]} {cara[1]} {cara[2]} {cara[3]}\n"
        )

print("✓ Montaña 3D generada: montaña.obj")
print(f"  - Vértices: {len(vertices)}")
print(f"  - Caras: {len(faces)}")

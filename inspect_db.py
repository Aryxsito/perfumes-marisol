import sqlite3

conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()

# Ver primeros 3 perfumes
print("=" * 80)
print("PRIMEROS 3 PERFUMES:")
print("=" * 80)
c.execute('SELECT id, nombre, descripcion, imagen, stock, precio FROM perfumes_perfume LIMIT 3')
for row in c.fetchall():
    print(f"ID: {row[0]}")
    print(f"  Nombre: {row[1]}")
    print(f"  Descripcion: {row[2][:50] if row[2] else 'VACIO'}")
    print(f"  Imagen: {row[3]}")
    print(f"  Stock: {row[4]}")
    print(f"  Precio: {row[5]}")
    print()

# Estadísticas
print("=" * 80)
print("ESTADISTICAS:")
print("=" * 80)

c.execute('SELECT COUNT(*) FROM perfumes_perfume WHERE descripcion IS NULL OR descripcion = ""')
print(f"Perfumes SIN descripcion: {c.fetchone()[0]}")

c.execute('SELECT COUNT(*) FROM perfumes_perfume WHERE imagen IS NULL OR imagen = ""')
print(f"Perfumes SIN imagen: {c.fetchone()[0]}")

c.execute('SELECT COUNT(*) FROM perfumes_perfume WHERE stock = 0')
print(f"Perfumes con STOCK=0: {c.fetchone()[0]}")

c.execute('SELECT COUNT(*) FROM perfumes_perfume WHERE precio = 0')
print(f"Perfumes con PRECIO=0: {c.fetchone()[0]}")

conn.close()
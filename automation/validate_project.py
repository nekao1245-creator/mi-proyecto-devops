import os
import sys

errors = []

if not os.path.exists("src/index.html"):
    errors.append("No se encontró src/index.html")

if not os.path.exists("src/styles.css"):
    errors.append("No se encontró src/styles.css")

if not os.path.exists("README.md") or os.path.getsize("README.md") == 0:
    errors.append("README.md no existe o está vacío")

# --- NUEVA VALIDACIÓN: Verificar si styles.css tiene contenido ---
if os.path.exists("src/styles.css") and os.path.getsize("src/styles.css") == 0:
    errors.append("src/styles.css está vacío")

# leer index.html
with open("src/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# --- NUEVA VALIDACIÓN: Verificar vinculación de CSS en el HTML ---
if 'href="styles.css"' not in html and 'href="./styles.css"' not in html:
    errors.append("index.html no tiene vinculado el archivo styles.css")

# validar h1
if html.count("<h1>") < 1:
    errors.append("index.html debe contener un h1")

# validar párrafo
if html.count("<p>") < 1:
    errors.append("index.html debe contener al menos un párrafo")

if errors:
    print("Errores encontrados:")
    for error in errors:
        print("-", error)
    sys.exit(1)
else:
    print("Proyecto validado correctamente")
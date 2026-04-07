import os
import sys
import html

errors = []

if not os.path.exists("src/index.html"):
    errors.append("No se encontró src/index.html")

if not os.path.exists("src/stiles.css"):
    errors.append("No se encontró src/stiles.css")

if not os.path.exists("README.md") or os.path.getsize("README.md") == 0:
    errors.append("README.md no existe o está vacío")

with open("src/index.html", "r") as f:
    html_content = f.read()

if html_content.count("<h1>") > 1:
    errors.append("index.html debe contener un h1")

if html_content.count("<p>") < 1:
    errors.append("index.html debe contener al menos un párrafo")

if html_content.count("<section>") > 1:
    errors.append("index.html debe contener al menos una sección")

if errors:
    print("Errores encontrados:")
    for error in errors:
        print("-", error)
    sys.exit(1)
else:
    print("Proyecto validado correctamente")
# Mi Proyecto DevOps

## Descripción del proyecto
Este proyecto consiste en la implementación de un flujo básico de DevOps utilizando Git y GitHub para el desarrollo y mantenimiento de un sitio web estático. La práctica permite comprender cómo funciona el control de versiones en un entorno de desarrollo colaborativo, así como la organización de un proyecto mediante repositorios, commits y ramas.

El proyecto incluye una estructura básica de archivos para un sitio web con HTML y CSS, además de un script que simula el proceso de despliegue. Todo el trabajo se gestiona a través de Git y se almacena en un repositorio público en GitHub.

---

## Objetivo
El objetivo de este proyecto es aplicar los conceptos fundamentales de DevOps mediante el uso de herramientas de control de versiones como Git y GitHub. A través de esta práctica se busca aprender a configurar Git en el equipo local, crear y administrar repositorios en GitHub, realizar commits documentados y trabajar con ramas para gestionar cambios en el proyecto.

También se pretende comprender cómo se puede simular un proceso de despliegue mediante scripts locales, además de documentar correctamente un proyecto de software utilizando un archivo README.

---

## Estructura del repositorio
    mi-proyecto-devops/
    │
    ├── src/
    │ ├── index.html
    │ ├── styles.css
    │
    ├── scripts/
    │ └── deploy.sh
    │
    ├── README.md
    └── .gitignore


**Descripción de los archivos:**

- **src/**  
  Contiene los archivos del sitio web.

- **index.html**  
  Página principal del proyecto web.

- **styles.css**  
  Archivo de estilos que define la apariencia del sitio.

- **scripts/**  
  Carpeta donde se almacenan scripts relacionados con el proyecto.

- **deploy.sh**  
  Script que simula el proceso de despliegue del sitio web.

- **README.md**  
  Documento que describe el proyecto y su funcionamiento.

- **.gitignore**  
  Archivo utilizado para indicar qué archivos o carpetas no deben subirse al repositorio.

---

## Flujo de trabajo utilizado
El flujo de trabajo seguido en este proyecto fue el siguiente:

1. Configuración inicial de Git en el equipo local mediante el uso de comandos de configuración global.
2. Creación de un repositorio público en GitHub.
3. Clonación del repositorio desde GitHub al equipo local.
4. Creación de la estructura básica del proyecto con carpetas y archivos necesarios.
5. Realización del primer commit con la estructura inicial del proyecto.
6. Creación de un script de despliegue para simular el proceso de publicación del sitio web.
7. Creación de una nueva rama llamada **feature-update** para agregar cambios al proyecto sin afectar la rama principal.
8. Modificación del archivo HTML agregando una nueva sección.
9. Subida de los cambios al repositorio remoto en GitHub.
10. Documentación completa del proyecto mediante el archivo README.

---

## Comandos Git principales

Configuración inicial de Git:
    git config --global user.name "Tu Nombre"
    git config --global user.email "tuemail@example.com"


Clonar repositorio:

    git clone https://github.com/TU-USUARIO/mi-proyecto-devops.git

    cd mi-proyecto-devops


Agregar archivos al repositorio:
    git add .


Crear un commit:
    git commit -m "Estructura inicial del proyecto"


Subir cambios al repositorio remoto:
    git push origin main


Crear una nueva rama:
    git checkout -b feature-update


Subir la nueva rama:
    git push origin feature-update


Cambiar entre ramas:
    git checkout main
    git checkout feature-update





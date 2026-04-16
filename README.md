# Proyecto Simple en Python (Universidad)


El objetivo es que cualquier compañero o profesor pueda:

- Clonar el repositorio
- Crear un entorno virtual (`venv`)
- Instalar dependencias (si aplica)
- Ejecutar el proyecto sin problemas

---

## 📂 Estructura del proyecto

mi_proyecto/
│── main.py
│── menu_principal.py
│── pedidos.py
│── datos.py
│── utils.py
│── README.md
│── requirements.txt
│── .gitignore
│── venv/ (NO se sube al repositorio)


---

## ✅ Requisitos

- Python 3.8 o superior

Verificar versión:

```bash
python --version
🚀 Instalación y ejecución (con entorno virtual)
1) Clonar el repositorio
git clone URL_DEL_REPOSITORIO
cd mi_proyecto
2) Crear el entorno virtual (venv)
Windows
python -m venv venv
Mac / Linux
python3 -m venv venv
3) Activar el entorno virtual
Windows (CMD o PowerShell)
venv\Scripts\activate
Mac / Linux
source venv/bin/activate
📌 Si se activó correctamente, deberías ver algo como:

(venv)
al inicio de la terminal.

4) Instalar dependencias
Este proyecto no usa librerías externas por ahora, pero se incluye requirements.txt por buenas prácticas.

pip install -r requirements.txt
5) Ejecutar el proyecto
python main.py
🧠 Descripción rápida del proyecto
main.py es el punto de entrada del programa.

funciones.py contiene la lógica principal y funciones auxiliares.

🛑 Nota importante sobre venv
La carpeta venv/ NO debe subirse al repositorio.
Por eso se incluye el archivo .gitignore.


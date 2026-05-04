# 🧠 ¿Qué es un entorno virtual?

Un **entorno virtual** es un espacio aislado donde puedes:

* Tener versiones específicas de Python
* Instalar librerías sin afectar otros proyectos
* Evitar conflictos de dependencias

---

## ⚠️ Ejemplo típico del problema

* Proyecto A usa **Flask 2.0**
* Proyecto B usa **Flask 3.0**

Sin entornos virtuales → 💥 conflictos
Con entornos virtuales → ✅ todo funciona correctamente

---

## 🔧 Tipos de entornos en Python

### 1. 🐍 `venv` (nativo)

* Incluido en Python
* Ligero
* No gestiona bien dependencias complejas

---

### 2. 📦 `Conda`

* Maneja **Python + librerías + dependencias del sistema**
* Permite cambiar la versión de Python fácilmente
* Ideal para proyectos más complejos

---

# Cómo crear entornos con Conda

## Crear un entorno
```bash
conda create --name mi_entorno
```

Especificar versión de Python
```bash
conda create --name mi_entorno python=3.11
```

---

## Activar el Entorno
```bash
conda activate mi_entorno
```
---

## Instalar Paquetes
```bash
conda install flask
```

---

## Ver entornos creados
```bash
conda env list
```


# Exportar e importar entornos

## Exportar
```bash
conda env export > enviroment.yml
```

## Crear entorno desde archivo
```bash
conda env create -f enviroment.yml
```


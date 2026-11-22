# Nexo · Portafolio web

Portafolio personal hecho con Django, HTML, CSS y JavaScript, basado en un diseño de Figma. Incluye la app **Atlas filosófico** enlazada desde la página de Proyectos.

## Páginas
Inicio, Sobre mí, Habilidades, Proyectos (con filtro en JavaScript) y Contacto (con validación de formulario).

## Cómo ejecutarlo (Windows)

1. Clona el repositorio y entra a la carpeta:
   ```powershell
   git clone https://github.com/dionel965/nexo-portafolio.git
   cd nexo-portafolio
   ```
2. Crea y activa el entorno virtual:
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```
3. Instala las dependencias:
   ```powershell
   pip install -r requirements.txt
   ```
4. Crea la base de datos y carga los datos de Atlas:
   ```powershell
   python manage.py migrate
   python manage.py loaddata atlas_datos.json
   ```
5. Arranca el servidor:
   ```powershell
   python manage.py runserver
   ```
6. Abre `http://127.0.0.1:8000/` (portafolio) y `http://127.0.0.1:8000/atlas/` (Atlas).

## Comparación Figma vs sitio

### Escritorio
| Figma | Sitio |
|---|---|
| ![Figma inicio](capturas/figma-inicio-escritorio.png) | ![Sitio inicio](capturas/sitio-inicio-escritorio.png) |
| ![Figma sobre mí](capturas/figma-sobre-mi-escritorio.png) | ![Sitio sobre mí](capturas/sitio-sobre-mi-escritorio.png) |
| ![Figma habilidades](capturas/figma-habilidades-escritorio.png) | ![Sitio habilidades](capturas/sitio-habilidades-escritorio.png) |
| ![Figma proyectos](capturas/figma-proyectos-escritorio.png) | ![Sitio proyectos](capturas/sitio-proyectos-escritorio.png) |
| ![Figma contacto](capturas/figma-contacto-escritorio.png) | ![Sitio contacto](capturas/sitio-contacto-escritorio.png) |

### Móvil (390 px)
| Figma | Sitio |
|---|---|
| ![Figma inicio](capturas/figma-inicio-movil.png) | ![Sitio inicio](capturas/sitio-inicio-movil.png) |

(Repite la fila para cada página móvil.)

## Diferencias respecto al diseño
- Escribe aquí, con honestidad, lo que cambió (textos, espaciados, colores).

## Tecnologías
Python, Django, HTML5, CSS3 (variables `:root`, Grid y Flexbox), JavaScript.

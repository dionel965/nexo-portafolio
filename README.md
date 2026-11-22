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

### Escritorio y Móvil (390 px)
En este link se encuentra la vista de figma coparandolos, contra la version web lista, tambien la movil.
|
  | `https://github.com/dionel965/nexo-portafolio/blob/main/capturas/vista-web-movil-figma.docx`

En la cual hay que descargar
  
## Diferencias respecto al diseño
- Respecto al diseño realizado en figma las cosas cambian ya en produccion,uno no espero encontrar complicaciones que lo atrasen,pero sin embargo se trato te igualar el diseño realizad en figma.

## Tecnologías
Python, Django, HTML5, CSS3 (variables `:root`, Grid y Flexbox), JavaScript.

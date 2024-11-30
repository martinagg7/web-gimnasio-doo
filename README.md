# Proyecto Web Defit360

Este proyecto es una **web desarrollada en Django** para la asignatura de **Desarrollo Orientado a Objetos (DOO)**. La web está diseñada para el gimnasio **Defit360**, ofreciendo una plataforma moderna y funcional para sus clientes y visitantes.

---

## Estructura del Repositorio

La estructura del proyecto es la siguiente:


```plaintext
.
├── manage.py
├── requirements.txt
├── db.sqlite3
├── .gitignore
├── webempresarial/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── core/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
├── blog/
├── contact/
├── media/
├── pages/
├── services/
├── social/

```
## Secciones del Sitio Web

### 1. **Home**
La **página de inicio** del sitio web, donde se presenta información general sobre el gimnasio Defit360.

### 2. **Planes**
Aquí se muestran los **distintos planes** que el gimnasio ofrece a sus clientes, desde básicos hasta avanzados.

### 3. **Services**
Sección dedicada a los **complementos y servicios** adicionales del gimnasio:
- Dietas personalizadas
- Fisioterapia
- Personal trainers
- Opiniones de los clientes

### 4. **Visítanos**
Información sobre los **horarios y la dirección** del gimnasio para facilitar el acceso de los usuarios.

### 5. **Blog**
Un espacio donde los **clientes pueden escribir y compartir experiencias**, creando una comunidad activa dentro de Defit360.

## Cómo Ejecutar el Proyecto

Sigue estos pasos para ejecutar la aplicación en tu entorno local:

```bash
# Clona el repositorio desde GitHub y accede a la carpeta del proyecto
git clone https://github.com/martinagg7/webempresarialllll.git
cd web_pers

# Crea un entorno virtual para aislar las dependencias del proyecto y actívalo
python -m venv env-django
source env-django/bin/activate  

# Instala las dependencias necesarias desde el archivo requirements.txt
pip install -r requirements.txt

# Ejecuta el servidor de desarrollo local
python manage.py runserver
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py runserver

```
## Desplegar Proyecto

- **Para acceder a la página principal**, abre [http://127.0.0.1:8000/](http://127.0.0.1:8000/) en tu navegador.  
- **Para acceder al panel de administración**, utiliza [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin).  

Si aún no tienes un superusuario, créalo con el siguiente comando:  
```bash
python manage.py createsuperuser
```
### Desplegar en Vercel
A la derecha del repositorio hay un enlace en el cual se puede ver la web desplegada en vercel

## Info del repositorio 
Usuario:Martina García González 
Usuario github: @martinagg7
Link repositorio:



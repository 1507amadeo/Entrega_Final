# Entrega_Final


`pip install django-ckeditor`

**Crear y activar entorno virtual (Windows)**

`C:\>python -m venv c:\ruta\al\entorno\virtual
C:\>c:\ruta\al\entorno\virtual\scripts\activate.bat`

**Crear y activar entorno virtual (Linux)**

`python3 -m venv venv
source venv/bin/activate`

**Crear y activar entorno virtual (Linux)**

`export SECRET_KEY='4e8&y0ygfox1cg7f3owcku9$hv_(nu7t3ku$p637-+!so2jlvs'
export DEBUG='True'
export ALLOWED_HOSTS='*,'`

**o crear el archivo Entrega_Final_Arcenilla_Miotto/.env con el siguente contenido**

`SECRET_KEY=4e8&y0ygfox1cg7f3owcku9$hv_(nu7t3ku$p637-+!so2jlvs
DEBUG=True
ALLOWED_HOSTS=*,`

**Instalar las dependencias del proyecto**

`pip install -r requirements.txt`

**Crear base de datos a partir de las migraciones**

`python manage.py migrate`

**Crear super-usuario**
 
`python manage.py createsuperuser`

La Opcion para agregar publicaciones esta habilitada para los Perfiles de superusuarios,editores o de administradores(cuando se registra un usuario se le pone por defecto perfil de lector)
si sos el usuario o superusuario que creo la publicacion podras, editarla, agrega imagen y borrala. si no, solo podes ver el detalle y hacer un comentario.

**Ejecutar proyecto**

`python manage.py runserver`

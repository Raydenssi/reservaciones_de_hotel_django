Sistema de Reservas de Hotel

Sistema de reservas de hotel que permite a los usuarios buscar habitaciones disponibles, realizar reservas, y gestionar sus estancias. Los administradores podrán añadir, editar o eliminar habitaciones, gestionar reservas y visualizar estadísticas de ocupación.

Instrucciones de Instalación

Clona el repositorio:

bash

git clone https://github.com/Raydenssi/reservaciones_de_hotel_django.git 

Crea un entorno virtual y actívalo:

bash

python -m venv venv source venv/bin/activate 

En Windows: venv\Scripts\activate

Instala las dependencias:

bash

pip install -r requirements.txt

Realiza las migraciones de la base de datos:

bash

python manage.py makemigrations python manage.py migrate

Crea un superusuario para acceder al panel de administración:

bash

python manage.py createsuperuser

Ejecuta el servidor de desarrollo:

bash

python manage.py runserver
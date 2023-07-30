#                       Digital electronics sales network (Electronic Store)

Project developed by: Mikhailov Alexander

____

The application is an API with CRUD functionality for suppliers, products and contacts.
There are three types of suppliers in the application - Factory, Retail Network and Individual Entrepreneur, each of which 
occupies a certain position in the hierarchy. You can create different suppliers and establish links between them,
change suppliers and edit their fields. Access to the API is granted only to authorized users with the parameter
is_active (permissions.py).
In the admin panel we implemented filtering (list_filter) by city name and "admin action" clearing the
debts to the supplier for selected objects. Also a link to the supplier is implemented in the admin panel.
The ban on updating debts to the supplier via API is implemented (in serializers IndividualSerializer and
RetailSerializer method update is overridden)
The possibility of filtering (list_filter) objects by a certain country is implemented via DRF.

____

### The stack of technologies used in the application:

- **Python 3.11**
- **Django 4.2**
- **Django REST framework 3.14.0**
- **Django-filter 23.2**
- **Postgres SQL**
- **Docker, Docker-compose**

____

### Application Structure:


- **Directory core** - *Directory with custom user model*

- **Directory electronic_store** - *The directory with the main django (backend) part of the application*

- **Directory supplier_network** - *A directory with a network of suppliers with models, serializers, views, etc.*


**manage.py** - *file with a link to the django-admin script for the project*

**requirements.txt** - *application dependencies*

**Dockerfile** - *container image file*

**docker-compose.yaml** - *configuration file for Docker Compose*

**.dockerignore** - *files and folders to ignore in Docker*

**.gitignore** - *files and folders to ignore in the Git version control system*

____

### Prepare and launch the application:

1. **Clone the application**
 - in the terminal, type the command `git clone https://github.com/TheLordVier/electronic_store.git`
2. **Create a virtual environment**
 - in the terminal, enter the command in the project directory `python -m venv venv`
3. **Install the application dependencies**
 - в терминале вводим команду `pip install -r requirements.txt` 
4. **Create an .env file (an example .env file is shown below)**
 - create an .env file in the root of the project and write in it the values of the variables used
5. **The file docker-compose.yaml**
 - create and fill in the file docker-compose.yaml or take a ready-made one from the project
 - in the terminal, type the command `docker-compose up -d` 
6. **Performing migrations**
 - in the terminal, type the command `./manage.py makemigrations`
 - then enter the command `./manage.py migrate`
 - check the performed migrations with the command `./manage.py showmigrations`
7. **Running the application locally**
 - in the terminal, enter the command at the root of the project `./manage.py runserver`
 - follow the path http://127.0.0.1:8000/ or log in to the admin panel http://127.0.0.1:8000/admin/

____

### Example of filling out an .env file:

    SECRET_KEY="django-insecure-virigz(qv3n85ho+#f3c-^r40qi!g&8gsk_gysp1!j*si9ds7$"
    DEBUG=True
    DB_USER=postgres
    DB_PASSWORD=postgres
    DB_NAME=postgres
    DB_HOST=localhost
    DB_PORT=5432
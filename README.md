# Steps to setups applications

### Restore Packages
pip install -r requirements.txt

### Add New packages to requirements.txt
pip freeze > requirements.txt

### Make Migrations of Blog
python manage.py makemigrations blog

### Make Migrations of Projects
python manage.py makemigrations projects

### Run Migrations
python manage.py migrate

### Add Super user
python manage.py createsuperuser
follow the steps

### Run Application
python manage.py runserver  



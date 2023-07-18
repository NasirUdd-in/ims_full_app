# inventory-management
This is a inventory management system

#How to get the projct? Simple!
  git clone https://github.com/NasirUdd-in/ims_full_app.git

#How to set up the project?

1. Create Virtual Environment
python -m venv env

2. activate the virtual environment
For mac: source env/bin/activate

For Windows:
cd env
cd Scripts
./activate

3. Go back to root: cd ..

4. install all packages
   pip install -r requirements

5. migrate the database
   python mamange.py runserver

6. set up database
   python manage.py makemigrations
   python manage.py migrate

7. create superuser
   python manage.py createsuperuser

8. run the server
   python manage.py runserver

9. see documentations for api
   http://127.0.0.1:8000/docs/



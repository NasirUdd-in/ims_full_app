# inventory-management
This is a inventory management system

#How to get the projct? Simple!<br>
  git clone https://github.com/NasirUdd-in/ims_full_app.git

#How to set up the project?<br>

1. Create Virtual Environment<br>
python -m venv env

2. activate the virtual environment<br>
For mac: source env/bin/activate

For Windows:
cd env
cd Scripts
./activate

3. Go back to root: cd ..

4. install all packages<br>
   pip install -r requirements

5. migrate the database<br>
   python mamange.py runserver

6. set up database<br>
   python manage.py makemigrations  <br>
   python manage.py migrate

7. create superuser<br>
   python manage.py createsuperuser

8. run the server<br>
   python manage.py runserver

9. see documentations for api<br>
   http://127.0.0.1:8000/docs/




How to install and run the project:

1. Extract django_test folder.
2. Create virtual environment:
   $ virtualenv -p python3 venv
3. Activate virtual environment:
   $ source venv/bin/activate
4. Install requirements:
   $ pip install -r requirements.txt
5. Apply application migrations:
   $ python3 manage.py migrate
6. Run the project:
$ python3 manage.py runserver 0.0.0.0:8000

Release note:
- Extended User model via AbstractUser model: added new fields(random_number, birthday);
- Added CRUD functionality for users;
- Added ability to download user list in CSV.

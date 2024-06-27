## Backend Server and Database
### Prerequisites
* MySQL v8.0
* Python v3.12.0~
* Pip 24.0
### Instructions
#### Windows
1. Navigate to your MySQL bin folder.
2. Run the following command and enter the password (if applicable)
```
mysql -u root -p
```
3. Create a database named `batgenome` using the following command:
```
CREATE DATABASE batgenome;
```
4. Close the MySQL session
5. Run the following commands in the directory `server-batgenomedatabase` to install the dependencies.
```
python -m venv venv
.\venv\Scripts\activate
pip install requirements.txt
```
5. Change the database settings on `server-batgenomedatabase\batgenomedatabase\settings.py` to match your root password and MySQL port.
6. Run the following command to migrate the database schema to `batgenome`
```
python manage.py migrate
```
7. Run the following command to create an administrator account to access the application.
```
python manage.py createsuperuser
```
8. Run the following command to use the database
```
python manage.py runserver
```

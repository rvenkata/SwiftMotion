# SwiftMotion



## Setting up Django server
```
$ git clone <git url>
$ cd swiftmotion_server
$ sudo easy_install pip
$ pip install virtualenv
$ mkvirtualenv swiftmotion
$ source activate swiftmotion
$ (swiftmotion) pip install -r requirements.txt
$ (swiftmotion) source deactivate 
```
## Setting up local Postgresql database 
Assuming Postgresql is set up and PATH variables are set.
```
$ createdb swiftmotion_db
$ psql
$ postgres=# CREATE ROLE swiftmotion WITH LOGIN PASSWORD 'password123';
$ postgres=# GRANT ALL PRIVILEGES ON DATABASE swiftmotion_db TO swiftmotion;
$ postgres=# ALTER USER swiftmotion CREATEDB;
```
## Running Django server
```
$ source activate swiftmotion
$ (swiftmotion) pip install -r requirements.txt
$ (swiftmotion) ./manage.py migrate
$ (swiftmotion) ./manage.py createsuperuser
$ (swiftmotion) ./manage.py runserver
```

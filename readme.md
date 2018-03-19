### Requirements
* Python 3.5+
* Pip
* PostgreSQL 9.6+
* PostGIS 2.3.6+
* Mapnik 2.2.0+  
### Launch instructions 
1. Run command `pip install -t requirements.txt`
1. In settings.py change database credentials to yours (database must be extended with PostGIS) 
1. Run command `python3 manage.py migrate`
1. Run command `python3 manage.py runserver`
1. Open http://localhost:8000/
1. Upload zip archive with polygons

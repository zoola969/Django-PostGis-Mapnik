### Requirements
* Python 3.5+
* Pip
* PostgreSQL 9.6+
* PostGIS 2.3.6+
* Mapnik 3.0.16+  
* Python-mapnik 3.0.16+
### Launch instructions 
1. Run command `pip install -r requirements.txt`
1. In settings/settings.py change database credentials to yours (database must be extended with PostGIS) 
1. Run command `python3 manage.py migrate`
1. Run command `python3 manage.py runserver`
1. Open http://localhost:8000/
1. Upload zip archive with polygons

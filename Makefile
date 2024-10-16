run:
	python3 manage.py makemigrations personnel
	python3 manage.py makemigrations salary
	python3 manage.py makemigrations recruitment
	python3 manage.py makemigrations resources
	python3 manage.py migrate
	python3 manage.py runserver 0.0.0.0:8000

# Run server
run:
	python manage.py runserver

# Make migrations
makemigrations:
	python manage.py makemigrations

# Migrate database
migrate:
	python manage.py migrate

# Run tests
test:
	pytest & \
	pytest --cov --cov-report=html

# format and lint
lint:
	isort . & \
	black . & \
	flake8 .


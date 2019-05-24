.PHONY: build db migrate static shell superuser run stop

clean:
		@docker-compose run --rm web sh -c "find . -name '*.pyc' -delete && find . -name '*.pyo' -delete && rm -f .coverage && rm -rf htmlcov"

build:
		@docker-compose build

db:
		@docker-compose up -d db

migrate: db
		@docker-compose run --rm web python manage.py migrate

static: db
		@docker-compose run --rm web python manage.py collectstatic --noinput

shell: db
		@docker-compose run --rm web python manage.py shell

superuser: db
		@docker-compose run --rm web python manage.py createsuperuser

run: migrate static
		@docker-compose up -d

stop:
		@docker-compose stop

test: clean
		@docker-compose run --rm web sh -c "pytest -v -rf"

coverage: clean
		@docker-compose run --rm web sh -c "pytest core/tests/ -s -v --cov=core --cov-branch --cov-report=term-missing --cov-report=html"
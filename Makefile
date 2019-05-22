.PHONY: build db migrate static shell superuser run stop


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

test:
		@docker-compose run --rm web sh -c "pipenv install --dev --skip-lock --system && pytest -v -rf"
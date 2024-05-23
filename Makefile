.PHONY: install
install:
	poetry install 

.PHONY: migrate
migrate:
	poetry run python3 -m Core.manage migrate

.PHONY: migrations
migrations:
	poetry run python3 -m Core.manage makemigrations

.PHONY: run-server
run-server:
	poetry run python3 -m Core.manage runserver

.PHONY: superuser
superuser:
	poetry run python3 -m Core.manage createsuperuser

.PHONY: update
update: install migrate ;


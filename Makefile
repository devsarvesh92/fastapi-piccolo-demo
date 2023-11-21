format: # Formats the Py codebase
	@pdm run black .

run-test: # Run specific marker tests
	@echo "Running test with marker $(NAME)..."
	@pdm run pytest -svv -m $(NAME)

test: local-setup
	@pdm run pytest --cache-clear

setup:
	$(call setup, "Setting up...")

start-web:
	@pdm run gunicorn --config gunicorn.conf.py server:app

define setup
	docker-compose -f docker-compose.yml up -d --build --force-recreate --remove-orphans
	@docker system prune -f --volumes
endef

local-setup: teardown setup migrations ingest
	@echo "Done with localsetup"

migrations:
	@sleep 5
	@docker exec polestar pdm run piccolo migrations new polestar --auto;
	@docker exec polestar pdm run piccolo migrations forwards polestar all --trace;

ingest:
	@docker exec polestar pdm run python data_ingestion.py


install:
	@pdm install --no-self;


define teardown
	@docker-compose -f docker-compose.yml rm -f -v -s
	@docker system prune -f --volumes
	@rm -rf citests .coverage .pytest_cache htmlcov
endef

teardown: # Teardown test resources
	$(call teardown, "Tearing down...")

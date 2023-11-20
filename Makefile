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

local-setup: setup migrations
	@echo "Done with localsetup"

migrations:
	@sleep 5
	@pdm run piccolo migrations new polestar --auto;
	@pdm run piccolo migrations forwards polestar all --trace;

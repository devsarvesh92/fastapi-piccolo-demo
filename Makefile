format: # Formats the Py codebase
	@pdm run black .

run-test: # Run specific marker tests
	@echo "Running test with marker $(NAME)..."
	@pdm run pytest -svv -m $(NAME)

migrations: setup # Create new db migrations and execute them
	@pdm run piccolo migrations new polestar --auto;
	@pdm run piccolo migrations forwards polestar all --trace;

setup:
	$(call setup, "Setting up...")

define setup
	docker-compose -f docker-compose.yml up -d --build --force-recreate --remove-orphans
    @docker system prune -f --volumes
endef

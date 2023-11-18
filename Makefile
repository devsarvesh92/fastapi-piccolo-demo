format: # Formats the Py codebase
	@[ "$(PYTHON_VERSION)" == "3.11.2" ] || { echo "Install python 3.11.2 for development." && exit 2; }
	@pdm run black .

run-test: # Run specific marker tests
	@echo "Running test with marker $(NAME)..."
	@pdm run pytest -svv -m $(NAME)

migrations: local-setup # Create new db migrations and execute them
	@pdm run piccolo migrations new polestar --auto;
	@pdm run migrate;

setup:
	$(call setup, "Setting up...")

define setup
	docker-compose -f docker-compose.yml up -d --build --force-recreate --remove-orphans
    @docker system prune -f --volumes
endef

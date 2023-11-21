# Polestar

This repository includes a Makefile with various targets to help you manage your project tasks efficiently. Below, you'll find a list of available Makefile targets and their descriptions:

- **Setup Local Development Environment:** Setup Local Development Environment: Set up the local development environment, including starting Docker containers and cleaning up orphaned resources. Launch **docker* before running any make commands

  ```bash
  make local-setup
- **Run Data Ingestion:** Run the data ingestion of ship and location for the project...
  ```bash
  make ingest
- **Access:** Launch swagger using http://127.0.0.1:8000/docs after setup is complete

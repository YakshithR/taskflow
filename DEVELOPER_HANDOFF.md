# Developer handoff: TaskFlow API

You are receiving this application as the DevOps engineer. Do not write the GitHub Actions workflow yet.

## Developer requirements

1. The API must expose a health endpoint.
2. Users can list, create, update, and delete tasks.
3. Invalid task input returns HTTP 400.
4. Updating or deleting an unknown task returns HTTP 404.
5. Automated tests are provided in `tests/`.
6. The application must run in Docker on port 5000.

## Your DevOps delivery requirements

Build a GitHub Actions pipeline that:

- Runs on pushes and pull requests to `master`.
- Checks out the repository.
- Sets up Python 3.12.
- Installs `requirements-dev.txt`.
- Runs `ruff check .`.
- Runs `pytest -q`.
- Builds the Docker image.
- On a push to `master`, logs in to Docker Hub and pushes an image tagged with `latest` and the commit SHA.

## GitHub configuration

Create a repository variable:
- `DOCKERHUB_USERNAME`

Create a repository secret:
- `DOCKERHUB_TOKEN`

Do not put credentials in source code or YAML.

## Acceptance criteria

- A pull request runs lint and tests but does not push an image.
- A push to `master` runs lint, tests, and Docker build.
- Only a successful push to `master` publishes the Docker image.
- A failing test makes the workflow fail.

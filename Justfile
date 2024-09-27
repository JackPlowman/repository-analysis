# ------------------------------------------------------------------------------
# General Commands
# ------------------------------------------------------------------------------

clean:
    just analyser::clean-repos
    just analyser::clean-generated-files
    find . \( \
      -name '__pycache__' -o \
      -name '.coverage' -o \
      -name '.mypy_cache' -o \
      -name '.pytest_cache' -o \
      -name '.ruff_cache' -o \
      -name '*.pyc' -o \
      -name '*.pyd' -o \
      -name '*.pyo' -o \
      -name 'coverage.xml' -o \
      -name 'db.sqlite3' \
    \) -print | xargs rm -rfv

clean-repos:
    rm -rf cloned_repositories/** || true

clean-generated-files:
    rm statistics/*.csv || true

install:
    poetry install

run:
    poetry run python -m application

run-with-defaults:
    DEBUG=true REPOSITORY_OWNER=JackPlowman poetry run python -m application

unit-test:
    poetry run pytest application --cov=application --cov-report=xml

unit-test-debug:
    poetry run pytest application --cov=application --cov-report=xml -vvvv

# ------------------------------------------------------------------------------
# Ruff - # Set up red-knot when it's ready
# ------------------------------------------------------------------------------

ruff-fix:
    just analyser::ruff-lint-fix
    just analyser::ruff-format-fix

ruff-lint:
    poetry run ruff check application

ruff-lint-fix:
    poetry run ruff check application --fix

ruff-format:
    poetry run ruff format --check application

ruff-format-fix:
    poetry run ruff format application

# ------------------------------------------------------------------------------
# Other Python Tools
# ------------------------------------------------------------------------------

vulture:
    poetry run vulture application

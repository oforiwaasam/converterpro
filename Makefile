NAME := converterpro
INSTALL_STAMP := .install.stamp
POETRY := $(shell command -v poetry 2> /dev/null)

.PHONY: install
install: $(INSTALL_STAMP) ## install packages and prepare environment
$(INSTALL_STAMP): pyproject.toml poetry.lock
	@if [ -z $(POETRY) ]; then echo "Poetry could not be found. See https://python-poetry.org/docs/"; exit 2; fi
	$(POETRY) install
	touch $(INSTALL_STAMP)

#########
# LINTS #
#########
.PHONY: lint
lint: $(INSTALL_STAMP) ## run code linters
	$(POETRY) run ruff check ./tests/ $(NAME) --exit-zero
	$(POETRY) run black --check ./tests/ $(NAME) --diff

.PHONY: lints
lints: lint

.PHONY: format
format: $(INSTALL_STAMP) ## reformat code
	$(POETRY) run ruff check --fix ./tests/ $(NAME) --exit-zero
	$(POETRY) run black ./tests/ $(NAME)

.PHONY: fix
fix: format

#########
# TESTS #
#########
test-py: $(INSTALL_STAMP) ## run all tests
	$(POETRY) run pytest -v ./tests/ --junit-xml=python_junit.xml

coverage-py: $(INSTALL_STAMP) ## generate HTML coverage report
	$(POETRY) run pytest -v ./tests/ --junit-xml=python_junit.xml --cov=converterpro --cov-report=xml:.coverage/coverage.xml --cov-report=html:.coverage/coverage.html --cov-branch --cov-fail-under=75 --cov-report term-missing

show-coverage: coverage-py  ## show interactive python coverage viewer
	cd .coverage && PYTHONBUFFERED=1 python -m http.server | sec -u "s/0\.0\.0\.0/$$(hostname)/g"
test: test-py  ## run all tests

# Alias
tests: test

.PHONY: clean
clean: ## remove all temporary files
	find . -type d -name "__pycache__" | xargs rm -rf {};
	rm -rf $(INSTALL_STAMP) .coverage coverage cover htmlcov logs build dist *.egg-info .mypy_cache .pytest_cache .ruff_cache
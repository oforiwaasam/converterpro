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
.PHONY: test
test: $(INSTALL_STAMP) ## run all tests
	$(POETRY) run pytest -v ./tests/ --junit-xml=python_junit.xml

.PHONY: tests
tests: test

.PHONY: coverage
coverage: $(INSTALL_STAMP) ## generate HTML coverage report
	$(POETRY) run pytest -v ./tests/ --junit-xml=python_junit.xml --cov=converterpro --cov-branch --cov-fail-under=75 --cov-report term-missing

.PHONY: clean
clean: ## remove all temporary files
	find . -type d -name "__pycache__" | xargs rm -rf {};
	rm -rf $(INSTALL_STAMP) .coverage coverage cover htmlcov logs build dist *.egg-info .mypy_cache .pytest_cache .ruff_cache
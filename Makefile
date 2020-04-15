.DEFAULT_GOAL := help

.PHONY: help
help:
	@grep -E '^[\.a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: test
test: ## Run unittests
	python -m pytest --cov=./ $(PYTEST_ARGS)

.PHONY: clean
clean: ## Clean the project directory
	rm -fr *.egg-info
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

.PHONY: docs
docs:
	rm -f docs/diggrtoolbox.rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs diggrtoolbox
	$(MAKE) -C docs clean
	$(MAKE) -C docs html

.PHONY: serve-docs
serve-docs:
	@cd docs/_build/html/ && python -m http.server && cd ../../..


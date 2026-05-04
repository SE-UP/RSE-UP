.PHONY: lint format test

lint:
	flake8 src/ tests/
	mypy src/

format:
	black src/ tests/
	isort src/ tests/

test:
	pytest tests/ --cov=src

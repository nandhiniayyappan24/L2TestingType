.PHONY: install test build clean

install:
	python -m pip install --upgrade pip
	pip install -e ".[dev]"
	pip install -r requirements.txt

test:
	pytest tests -v

build: install test
	python scripts/build.py

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf .pytest_cache .coverage htmlcov build_report.json

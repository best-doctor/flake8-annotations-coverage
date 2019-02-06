check:
	flake8 .
	mypy .
	pytest --cov=. --cov-report=xml

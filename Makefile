check:
	flake8 .
	mypy .
	pytest --cov=flake8_annotations_coverage --cov-report=xml

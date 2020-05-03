check:
	flake8 .
	mypy .
	python -m pytest --cov=flake8_annotations_coverage --cov-report=xml
	safety check -r requirements_dev.txt
	mdl README.md

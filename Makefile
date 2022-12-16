dependencies:
	python -m pip install --upgrade pip && pip install -r requirements.txt

typecheck:
	mypy rs3_api

lintcheck:
	flake8 .

.PHONY: check
check:
	pipenv run isort -c
	pipenv run black --check .
	find ./ -iname "*.py" | xargs pipenv run pylint --disable=C

.PHONY: format
format:
	pipenv run isort -y
	pipenv run black .


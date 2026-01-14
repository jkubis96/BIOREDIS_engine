.PHONY: format lint check all

format:
	isort jbst
	black jbst
	isort tests
	black tests


lint:
	pylint --exit-zero jbst/seq_tools.py
	pylint --exit-zero jbst/vector_build.py
	pylint --exit-zero tests/test.py




all: format lint

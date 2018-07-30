lint:
	flake8 --statistics .

test:
	py.test --cov=diggrtoolbox tests

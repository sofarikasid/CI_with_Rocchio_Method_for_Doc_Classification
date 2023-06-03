install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest --nbval rocchio_classify.py

format:
	black *.py

lint:
	pylint --disable=R,C rocchio_classify.py

all: install format lint test
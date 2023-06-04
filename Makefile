install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest --nbval test_rocchio_classify.py

format:
	black *.py

lint:
	pylint --disable=R,C rocchio_classify.py 
	

all: install lint test
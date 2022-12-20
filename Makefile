install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=main --cov=mylib test_*.py

format:	
	python -m black *.py mylib/*.py

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py mylib/*.py

container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

refactor: format lint

deploy:
	# build a container that triggers deploy - Note: docker deployment hits quota limits and is failing
	# step 1: auth
	#aws ecr get-login-password --region us-east-1 |	docker login --username AWS --password-stdin 249934578875.dkr.ecr.us-east-1.amazonaws.com
	# step 2: build
	#docker build -t geoservice .
	# step 3: tag the image so you can push it into ECR repository
	#docker tag geoservice:latest 249934578875.dkr.ecr.us-east-1.amazonaws.com/geoservice:latest
	# step 4: push the image to ECR repository
	#docker push 249934578875.dkr.ecr.us-east-1.amazonaws.com/geoservice:latest
		
all: install lint test format deploy

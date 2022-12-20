[![CI](https://github.com/nogibjj/python-template/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/python-template/actions/workflows/cicd.yml)

![CodeBuild](https://codebuild.us-east-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoibERZN3ZESUE1d0dmSUIyS0RJNkZlOEJJRnBZdUtsRXlWVUdCNnlDSUFFcjFZY2xqcGV0Y1hsbUFHaGh0VkcrZlZZYTFjeVZNODNGUU1ndTcrQUx2R2dVPSIsIml2UGFyYW1ldGVyU3BlYyI6IjNZMC8yMlBNL1poeHc2d20iLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=main)

## Template for Python projects 

https://codebuild.us-east-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoibERZN3ZESUE1d0dmSUIyS0RJNkZlOEJJRnBZdUtsRXlWVUdCNnlDSUFFcjFZY2xqcGV0Y1hsbUFHaGh0VkcrZlZZYTFjeVZNODNGUU1ndTcrQUx2R2dVPSIsIml2UGFyYW1ldGVyU3BlYyI6IjNZMC8yMlBNL1poeHc2d20iLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=main

Follow along tutorial:
https://www.youtube.com/watch?v=lbm9ckutS3k


1. First thing to do on launch is to open a new shell and verify virtualenv is sourced.

Things included are:

* `Makefile`

* `Pytest`

* `pandas`

* `Pylint`

* `Dockerfile`

* `GitHub copilot`

* `jupyter` and `ipython` 

* A base set of libraries for devops and web

* `githubactions` 


### Run the app in a docker container (on github)

docker build .

Run a command in a new container
(venv) @jmandrake ➜ /workspaces/devops_test (main ✗) $ docker image ls
REPOSITORY   TAG       IMAGE ID       CREATED          SIZE
<none>       <none>    f1e9dd0bd3ca   39 minutes ago   538MB
(venv) @jmandrake ➜ /workspaces/devops_test (main ✗) $ docker run -p localhost:80:8080 f1e9dd0bd3ca
docker: Invalid ip address: localhost.
See 'docker run --help'.
(venv) @jmandrake ➜ /workspaces/devops_test (main ✗) $ docker run -p 127.0.0.1:80:8080 f1e9dd0bd3ca
INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8080 (Press CTRL+C to quit)
INFO:     172.17.0.1:42764 - "GET / HTTP/1.1" 200 OK
INFO:     172.17.0.1:42770 - "GET /favicon.ico HTTP/1.1" 404 Not Found
INFO:     172.17.0.1:49310 - "GET /docs HTTP/1.1" 200 OK
INFO:     172.17.0.1:49310 - "GET /openapi.json HTTP/1.1" 200 OK

Opens browser at the forwarded port:
https://jmandrake-psychic-couscous-7g759wg4xjfrgrg-80.preview.app.github.dev/docs


### Run the dockerized app on AWS Cloud9

Create a container in ECR: 
How to: https://youtu.be/lbm9ckutS3k?t=6000

https://us-east-1.console.aws.amazon.com/cloud9control/home?region=us-east-1

- set configuration to auto update
  
 ### Run the dockerized app on Google Cloud Run
 1. Login to console
 2. git clone [repository url]
 3. cd into the folder
 4. gcloud run deploy
  

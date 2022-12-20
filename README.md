[![CI](https://github.com/nogibjj/python-template/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/python-template/actions/workflows/cicd.yml)

## To Do:Fix this error in deploy step:
```
Step 1/9 : FROM python:3.8.13-slim-buster
toomanyrequests: You have reached your pull rate limit. You may increase the limit by authenticating and upgrading: https://www.docker.com/increase-rate-limit
make: *** [deploy] Error 1

[Container] 2022/12/20 02:16:52 Command did not exit successfully make all exit status 2
[Container] 2022/12/20 02:16:52 Phase complete: BUILD State: FAILED
[Container] 2022/12/20 02:16:52 Phase context status code: COMMAND_EXECUTION_ERROR Message: Error while executing command: make all. Reason: exit status 2
```


## Template for Python projects 

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
  

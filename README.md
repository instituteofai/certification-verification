# Certification Verification server

This server verifies LinkedIn certificates issued by Institute of AI.

## Running locally

1. Clone this repository
2. Create a virtual environment (recommended, not mandatory)
3. Install required libraries 
```
$ pip install -r requirements.txt
```
4. Start local server
```
$ uvicorn app.main:app
```

## Deploying

1. Build a new version of the container

```
$ docker build -t mashruravi/iai-certificate-verifier:tag ./
```

2. Push to Docker Hub

```
$ docker push mashruravi/iai-certificate-verifier:tag
```

3. Update image in Kubernetes cluster

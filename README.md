# Certification Verification server

This server verifies LinkedIn certificates issued by Institute of AI.

# Deploying

1. Build a new version of the container

```
docker build -t mashruravi/iai-certificate-verifier:tag ./
```

2. Push to Docker Hub

```
docker push mashruravi/iai-certificate-verifier:tag
```

3. Update image in Kubernetes cluster

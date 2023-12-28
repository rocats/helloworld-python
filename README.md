# helloworld-python

## Run locally

```bash
docker compose up --build
```

## Build and push

Create builder

```bash
docker buildx create --use --platform=linux/arm64,linux/amd64 --name multi-platform-builder
```

Build and push

```bash
docker buildx build --platform linux/arm64,linux/amd64 -t "helloworld-python" --build-arg PYTHON_VERSION=3.12 .
```

## Reference

https://edu.chainguard.dev/chainguard/chainguard-images/getting-started/getting-started-python/

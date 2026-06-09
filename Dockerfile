FROM python:3.14.5-alpine3.23
WORKDIR /app
COPY src src
CMD ["python", "src/__main__.py"]

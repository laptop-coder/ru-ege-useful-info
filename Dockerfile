FROM ghcr.io/astral-sh/uv:python3.14-alpine3.23

WORKDIR /app
COPY pyproject.toml uv.lock ./

# Install the application dependencies.
RUN uv sync --frozen

# Copy the application into the container.
COPY src src

# Run the application.
CMD ["uv", "run", "src/__main__.py"]

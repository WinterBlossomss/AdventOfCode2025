FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \ 
    python3-numpy \
    python3-scipy \ 
    && rm -rf /var/lib/apt/lists/*

# Copy dependency files first (better layer caching)
COPY pyproject.toml uv.lock ./

# Install dependencies into a project-local venv
RUN uv sync --frozen

# Copy the rest of your project
COPY . .

RUN chmod +x run_all.sh

CMD ["uv", "run", "./run_all.sh"]

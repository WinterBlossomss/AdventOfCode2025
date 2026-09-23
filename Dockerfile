FROM python:3.12-slim

WORKDIR /app

RUN pip install --no-cache-dir uv

# Copy dependency files first (better layer caching)
COPY pyproject.toml uv.lock ./

# Install dependencies into a project-local venv
RUN uv sync --frozen

# Copy the rest of your project
COPY . .

RUN chmod +x run_all.sh

CMD ["uv", "run", "./run_all.sh"]

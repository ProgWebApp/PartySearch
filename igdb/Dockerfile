# Test Stage
FROM python:3.9-slim-bullseye
WORKDIR /app

# PDM installation
RUN pip install --no-cache-dir pip setuptools wheel
RUN pip install --no-cache-dir pdm

# Copy Project files
COPY ./src/pyproject.toml ./
COPY ./src/pdm.lock ./

# Dependencies installation
RUN pdm install

# Copy all sources files
COPY ./src ./

# Production Command
CMD [ "pdm", "run", "launch" ]

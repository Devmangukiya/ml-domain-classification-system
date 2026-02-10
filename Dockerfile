FROM python:3.10-slim-bullseye

# Disable Ray usage stats
ENV RAY_USAGE_STATS_ENABLED=0

# System dependencies
RUN apt-get update && apt-get install -y \
    git \
    curl \
    bash \
    awscli \
 && rm -rf /var/lib/apt/lists/*

# Python dependencies
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Ray
RUN pip install --no-cache-dir ray[default] ray[serve]

WORKDIR /app
COPY . .

CMD ["ray", "start", "--head", "--num-cpus=8", "--num-gpus=0", "--block"]

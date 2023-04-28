FROM python

LABEL maintainer="Sergej Krasnikov sergej.krasnikov@uni-a.de"

# Expose port 8000 for development server
EXPOSE 8000

# Install dependecies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    git \
    cmake \
    libopenmpi-dev \
    zlib1g-dev \
    ffmpeg \
    python-is-python3 \
    && rm -rf /var/lib/apt/lists/*

# Install additional packages
RUN python3 -m pip install --no-cache \
    numpy \
    pandas \
    gym \
    stable-baselines3 \
    django \
    django-bootstrap-v5 

RUN pip install -U scikit-learn 

# Set work directory
WORKDIR /root

# using a minimal Python base
FROM python:3.11-slim

# ensure output is unbuffered & no .pyc files
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# set working directory
WORKDIR /app

# install OS-level deps 
RUN apt-get update \
 && apt-get install -y --no-install-recommends build-essential \
 && rm -rf /var/lib/apt/lists/*

# copy & install Python dependencies 
COPY requirements.txt .
RUN pip install --upgrade pip \
 && pip install -r requirements.txt

# copy the code
COPY . .

# switch into Django project folder
WORKDIR /app/blvd

# expose Django’s default dev port
EXPOSE 8000

# run default Django’s development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

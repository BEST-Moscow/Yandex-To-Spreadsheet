FROM python:3.11

ENV PYTHONUNBUFFERED=1 \
    PYTHONPATH="/venv/lib/python3.11/site-packages:${PYTHONPATH}"

ADD ./scripts/googleApi/tokens/api-token.json ./scripts/googleApi/tokens/
    
COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# CMD [ "gunicorn", "-b", "0.0.0.0:5000", "wsgi:app" ]

EXPOSE 5000
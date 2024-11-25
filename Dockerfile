FROM python

WORKDIR /scripts
# WORKDIR /

# ENV FLASK_APP=app.py
# ENV FLASK_RUN_HOST=0.0.0.0

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
# RUN source venv/bin/activate

COPY . .

# CMD [ "source",   "venv/bin/activate" ]
CMD [ "flask", "run" ]
# CMD [ "gunicorn", "-b", "0.0.0.0:5000", "wsgi:app" ]
# CMD [ "source", "venv/bin/activate", "&&", "gunicorn", "-b", "0.0.0.0:5000", "wsgi:app" ]

# EXPOSE 3000
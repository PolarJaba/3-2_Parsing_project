FROM python:3.11.0
RUN pip install psycopg2 
RUN pip install requests
COPY parsing_data.py /opt/app/parsing_data.py
WORKDIR /opt/app/
CMD ["python", "parsing_data.py"]


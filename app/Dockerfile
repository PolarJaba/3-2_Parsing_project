FROM python:3.11.0
COPY libraries_install.txt /opt/app/
RUN pip install -r /opt/app/libraries_install.txt
COPY parsing_data.py /opt/app/parsing_data.py
WORKDIR /opt/app/
CMD ["python", "parsing_data.py"]


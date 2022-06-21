FROM python:3.10
COPY . /app
WORKDIR /app
RUN pip install .
EXPOSE 5000
CMD ["confitec_teste", "run"]

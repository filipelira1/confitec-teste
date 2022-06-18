FROM python:3.7-alpine
COPY . /app
WORKDIR /app
RUN pip install .
RUN confitec_teste create-db
RUN confitec_teste populate-db
RUN confitec_teste add-user -u admin -p admin
EXPOSE 5000
CMD ["confitec_teste", "run"]

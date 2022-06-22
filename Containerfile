FROM python:3.10
COPY . /app
WORKDIR /app
RUN echo "AAA"
RUN pip install .
EXPOSE 5000
RUN echo "XXXX"
CMD ["confitec_teste", "run", "-h", "0.0.0.0"]

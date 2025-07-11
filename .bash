# airflow container
docker build . -f airflow.dockerfile --tag extending_airflow:latest


# fastapi container
docker build . -f fastapi.dockerfile --tag mktmasta_fastapi
# docker run -d --name mktmasta_api -p 80:80 mktmasta_fastapi

# run all services
docker compose up -d
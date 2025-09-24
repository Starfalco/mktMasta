# airflow container
docker build . -f airflow.dockerfile --tag extending_airflow:latest

# fastapi container
docker build . -f fastapi.dockerfile --tag mktmasta_fastapi

# angular container
docker build . -f angular.dockerfile --tag mktmasta_angular

# run all services
docker compose up -d

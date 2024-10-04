#!/bin/sh
  # Setting up ssh connection with deploy server
ssh -t -o StrictHostKeyChecking=no "$VM_USERNAME"@"$1" #<< 'ENDSSH'
#    private_ip=`172.31.11.9`
    private_ip=`curl http://169.254.169.254/latest/meta-data/local-ipv4`

    echo "Running on server: $private_ip"

## Declaring variables 
    echo "VM_USERNAME : $VM_USERNAME"
    INT_VM_USERNAME="admin"
    PROJECT_BASE_PATH="/home/$INT_VM_USERNAME/hrms-revamp-2024"
    echo "PROJECT_BASE_PATH : $PROJECT_BASE_PATH"
    mkdir -p "$PROJECT_BASE_PATH"

    cd "$PROJECT_BASE_PATH"

## Set environment  variables
    set -o allexport
#    source "$PROJECT_BASE_PATH"/.env
    source /home/admin/hrms-revamp-2024/app/.env
    set +o allexport
    
## Printing values for the env variables
    echo "COMPOSE_PROJECT_NAME : $COMPOSE_PROJECT_NAME"
    echo "CI_REGISTRY_USER : $CI_REGISTRY_USER"
    echo "CI_REGISTRY : $CI_REGISTRY"
   
## Logging into container registry
     echo "$CI_BUILD_TOKEN" | docker login -u "$CI_REGISTRY_USER" --password-stdin "$CI_REGISTRY"

## Deploying docker containers
    which docker-compose && ls /usr/local/bin/docker-compose
    /usr/local/bin/docker-compose -f "$PROJECT_BASE_PATH"/docker-compose.prod.yml down || true || echo "docker container down completed"
    /usr/local/bin/docker-compose -f "$PROJECT_BASE_PATH"/docker-compose.prod.yml rm -f

    docker rmi -f $(docker images -aq)
    docker system prune -f    

## Docker Container up using docker-compose env file
    /usr/local/bin/docker-compose -f "$PROJECT_BASE_PATH"/docker-compose.prod.yml up --build -d --force-recreate || echo "docker container up completed"
 
    docker container ls -a --format 'table {{.ID}}\t{{.Image}}\t{{.Status}}'
#ENDSSH


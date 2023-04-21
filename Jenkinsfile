def constants = load 'constants.groovy'

pipeline {
    agent any
    
    stages {
        stage('Testing static code') {
            steps {
                sh 'pip install pylint'
                sh 'pylint devops.py'
            }
        }
        
        stage('Deployment') {
            environment {
                TAG = constants.ENVIRONMENTS.dev.tag
                ECR_REPOSITORY = constants.ENVIRONMENTS.dev.repository
                ECR_REGISTRY = constants.ENVIRONMENTS.dev.docker_registry
            }
            steps {
                withAWS(credentials: 'jenkins_aws_user') {
                    sh 'aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin ${ECR_REPOSITORY}'
                    sh 'docker build -t devops-microservice .'
                    sh 'docker tag devops-microservice:latest ${ECR_REPOSITORY}/${ECR_REPOSITORY}:${TAG}'
                    sh 'docker push ${ECR_REPOSITORY}/${ECR_REPOSITORY}:${TAG}'
                }
            }
        }

        stage('Automatic Test'){
            steps{
                sh 'pip install pytest requests'
                sh 'pytest auto_test_devops.py'
            }
        }

    }
}

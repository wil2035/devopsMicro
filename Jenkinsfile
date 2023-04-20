def constants = load 'constants.groovy'

pipeline {
    agent any
    options {
        scriptSecurity {
            sandbox {
                // Disable Groovy Sandbox
                permissions([new org.jenkinsci.plugins.scriptsecurity.sandbox.groovy.SecureGroovyScript()])

            }
        }
    }

    stages {
        stage('Testing static code') {
            steps {
                sh 'pip install pylint'
                sh 'pylint devops.py'
            }
        }

        
        stage('Deployment') {
            /*environment {
                TAG = constants.ENVIRONMENTS.dev.tag
                DOCKER_REGISTRY = constants.ENVIRONMENTS.dev.docker_registry
            }*/
            steps {
                sh 'docker build -t devops-microservice .'
                sh 'docker run -d -p 80:5000 devops-microservice'
                sh 'docker tag devops-microservice:latest devops-microservice:${TAG}'
                sh 'docker push my-microservice:${TAG}'
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

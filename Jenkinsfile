pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Code Checkout Successful'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-app .'
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                docker stop flask-app || true
                docker rm flask-app || true

                docker run -d \
                --name flask-app \
                -p 5000:5000 \
                flask-app
                '''
            }
        }
    }
}
pipeline {
    agent any

    environment {
        IMAGE_BUILD = 'temperatura-build:latest'
        IMAGE_TEST = 'temperatura-test:latest'
    }

    stages {
        stage('Clonar Repositório') {
            steps {
                script {
                    git url: 'https://github.com/manoelpim/gc_jenkins', branch: 'main'
                }
            }
        }


        stage('Build') {
            steps {
                script {
                    docker.build("${IMAGE_BUILD}", "-f Dockerfile.build .")
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    docker.build("${IMAGE_TEST}", "-f Dockerfile.test .")
                    docker.image("${IMAGE_TEST}").inside {
                        sh 'python -m unittest teste_temperatura.py'
                    }
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }

        success {
            echo 'Pipeline executado com sucesso!'
        }

        failure {
            echo 'Pipeline falhou. Verifique os logs!'
        }
    }
}
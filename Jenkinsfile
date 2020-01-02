pipeline {
    agent {
        docker {
            image 'python:3.8'
        }
    }
    stages {
        stage('Build') {
            steps {
                sh 'apt update'
                sh 'apt install -y pipenv'
                sh 'pipenv install --dev'
            }
        }
        stage('Format') {
            parallel {
                stage('Pylint') {
                    steps {
                        sh 'find ./ -iname "*.py" | xargs pipenv run pylint --disable=C'
                    }
                }
                stage('Black') {
                    steps {
                        sh 'pipenv run black --check .'
                    }
                }
                stage('isort') {
                    steps {
                        sh 'pipenv run isort -c'
                    }
                }
            }
        }
        stage('Tests') {
            steps {
                sh 'pipenv run pytest'
            }
        }
    }
}
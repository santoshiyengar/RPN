pipeline {
    agent any
    stages {
        stage('Unit Test') {
            steps {
                echo 'Unit Test...'
                sh "python -m pytest tests -vv"
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploy.......>.'
            }
        }
        stage('Done') {
            steps {
                echo 'Done '
            }
        }
    }
}
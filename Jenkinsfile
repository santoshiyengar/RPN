pipeline {
    agent any
    stages {
        stage('Unit Test') {
            steps {
                echo 'Unit Test...'
                sh "python -m /home/sly/.local/bin/pytest tests -vv"
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
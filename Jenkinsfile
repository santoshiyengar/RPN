pipeline {
    agent any
    stages {
        stage('Unit Test') {
            steps {
                echo 'Unit Test...'
                python rpn_main.py
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
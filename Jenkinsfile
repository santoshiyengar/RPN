pipeline {
    agent any
    stages {
        stage('Unit Test') {
            steps {
                echo 'Unit Test...'
                sh "/usr/bin/python2.7 /usr/lib/pycharm-community/helpers/pycharm/pytestrunner.py -p pytest_teamcity /home/sly/Repositories/RPN/tests"
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
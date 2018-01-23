pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                sh 'dir'
            }
        }
    }
    post {
        always {
            emailext(
               body: '${env.BUILD_LOG}',
               attachLog: true,
               subject: '${env.BUILD_ID}',
               to: 'santoshiyengar@gmail.com'
            )   
        }
    }
}


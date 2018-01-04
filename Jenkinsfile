pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                sh 'make check'
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

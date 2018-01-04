node {
   stage('Preparation') {
       checkout scm;
   }
   stage('Test') {
   }
   stage('Results') {
      emailext(
         body: ${BUILD_LOG, maxLines, escapeHtml},
         attachLog: true,
         subject: 'env.BUILD_NUMBER',
         to: 'santoshiyengar@gmail.com'
      )   
   }
}

pipeline{
   node any
   stage('Preparation') {
       checkout scm;
   }
   stage('Test') {
   }
   stage('Results') {
   }
   post{
      always{
         emailext(
            body: '${env.BUILD_LOG}',
            attachLog: true,
            subject: '${env.BUILD_ID}',
            to: 'santoshiyengar@gmail.com'
         )   
      }
   }
}

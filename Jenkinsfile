node {
   stage('Preparation') {
       checkout scm;
   }
   stage('Test') {
   }
   stage('Results') {
      emailext(
         body: 'your component is released',
         attachlog: true,
         subject: 'env.BUILD_NUMBER',
         to: 'santoshiyengar@gmail.com'
      )   
   }
}

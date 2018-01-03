node {
   stage('Preparation') {
       checkout scm;
   }
   stage('Test') {
       sh '/usr/bin/python2.7 /usr/lib/pycharm-community/helpers/pycharm/pytestrunner.py -p pytest_teamcity /home/sly/Repositories/RPN/tests'
   }
}

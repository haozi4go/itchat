pipeline {
  agent any
  environment { 
    //send_msg = 'jenkins test' //改到界面配置，可API传参
  }
  stages {
    stage('Sending') {
      options {
        timeout(time: 2, unit: 'MINUTES') 
      }
      steps {
        sh "python ~/apps/docs/jenkins/workspace/itchat/itchat-send.py '${send_msg}' "
        echo "Send success."
      }
    }
  }
}

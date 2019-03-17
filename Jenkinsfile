pipeline {
  agent any
  environment { 
    send_msg = 'jenkins test'
  }
  stages {
    stage('Sending') {
      options {
        timeout(time: 2, unit: 'MINUTES') 
      }
      steps {
        sh "python ~/apps/jenkins/workspace/itchat/itchat-send.py ${send_msg} "
        echo "Send success."
      }
    }
  }
}

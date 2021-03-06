pipeline {
  agent any
  environment {
    COURSE = 'Calgary DevOps'
    BRANCH = 'main'
    WWWROOT = '/var/www'
    SSHUSER = 'jenkins'
  }
  stages {
    stage('Audit Tools') {
      steps {
        echo "Audit all tools to be use on this pipeline ${BRANCH}"
        sh "git --version"
        sh "node --version"
        sh "npm --version"
        sh "ng --version"
        sh "ansible --version"
        echo "Workspace Folder: ${WORKSPACE}"
      }
    }
    stage('Install packages') {
      steps {
        sh "git pull origin ${BRANCH}"
      }
    }
    stage('Install Front-End Packages') {
      steps {
        dir("${WORKSPACE}/conduit-ui") {
          echo "Install conduit UI packages"
          sh "npm install"
        }
      }
    }
    stage('Run linting') {
      steps {
        dir("${WORKSPACE}/conduit-ui") {
          echo "npm run lint"
        }
      }
    }
    stage('Build UI') {
      steps {
        dir("${WORKSPACE}/conduit-ui") {
          sh "npm run build"
        }
      }
    }
    stage('Deploy app to WEB01') {
      steps {
        sh "ssh web01 sudo cp -r /home/amoh/${SSHUSER}/conduit/* ${WWWROOT}/conduit"
      }
    }
  }
}

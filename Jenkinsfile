node{
  stage('Scm checkout'){
    git  url:'https://github.com/Myownwiki/challenge.git', branch:'master'
  }
  stage('Build docker Image') {
    dir('server') {
      sh'docker build . -t hello-world'
    }
  }
  stage('Tagging and Pushing') {
    withCredentials([string(credentialsId:'n_ip', variable:'n_ip'), string(credentialsId:'n_un', variable:'n_un'), string(credentialsId:'n_pw', variable:'n_pw')]) {
      GIT_SHORT_COMMIT=sh(returnStdout:true, script:"git log -n 1 --pretty=format:'%h'").trim()
      HELM_LIST_REVISION=sh(returnStdout:true, script:"helm history hello-world-helm | awk '{ REVISION =\$1 }; END { print REVISION }'").trim()

      def TAG=HELM_LIST_REVISION+'-'+GIT_SHORT_COMMIT+'-'+BUILD_NUMBER;
      sh '''echo TAG:'''+TAG+''' '''
      sh '''docker tag hello-world nexusrepo/hello-world:'''+TAG+''' '''
      sh 'docker tag hello-world nexusrepo0/hello-world:stable'
      sh 'docker push nexusrepo/hello-world:stable'
      sh '''docker push nexusrepo/hello-world:'''+TAG+''' '''
    }
  }
   stage('Deploy') {
    //sh 'echo ${BUILD_NUMBER}'
    def TAG=HELM_LIST_REVISION+'-'+GIT_SHORT_COMMIT+'-'+BUILD_NUMBER;
    sh '''helm upgrade --set image.tag='''+TAG+''' hello-world-helm ./hello-world-helm'''
  }
  stage('Clean Up') {
    def TAG=HELM_LIST_REVISION+'-'+GIT_SHORT_COMMIT+'-'+BUILD_NUMBER;
    sh '''docker rmi -f nexusrepo/hello-world:'''+TAG+''' '''
    sh 'docker rmi -f nexusrepo/hello-world:stable'
    sh 'docker rmi -f hello-world'
  }
} 

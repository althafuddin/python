#!/usr/bin/env groovy

aws_region = 'us-west-1'
docker_repo = '756518171116.dkr.ecr.us-west-1.amazonaws.com'
docker_repo_creds_id = 'ecr-io'
docker_repo_url = "https://${docker_repo}"
git_repo_creds_id = 'jenkins'

podTemplate(label: 'io',
  containers: [
    containerTemplate(name: 'docker', image: 'docker:latest', ttyEnabled: true, command: 'cat'),
  ],
  volumes: [
    hostPathVolume(hostPath: '/var/run/docker.sock', mountPath: '/var/run/docker.sock')
  ],
  serviceAccount: 'jenkins'
)

{
  node(label: 'io') {
    wrap([$class: 'BuildUser']) {
    buildUser = sh returnStdout: true, script: 'echo ${BUILD_USER}'
    }
    container('docker') {
      docker.withRegistry(docker_repo_url, "ecr:${aws_region}:${docker_repo_creds_id}") {
        stage('\u27A1 Checkout git repo') {
          checkoutRepo(git_repo_creds_id: git_repo_creds_id, git_repo: 'git@bitbucket.org:imageoptions/io_engage_event.git', git_branch: "version-test")
        }
        stage('\u27A1 Reading the version file') {
          version = readFile('VERSION').trim()
        if ("${release}" == "major"){
          major_version = make_version(version, "${release}")
          buildVersion = "${major_version}-build-${BUILD_NUMBER}"
        }
        else if ("${release}" == "minor"){
          minor_version = make_version(version, "${release}")
          buildVersion = "${minor_version}-build-${BUILD_NUMBER}"
        }
        else {
          regular_version = make_version(version)
          buildVersion = "${regular_version}-build-${BUILD_NUMBER}" 
        }
          currentBuild.displayName = "${buildVersion}"
          //currentBuild.result = 'FAILED'
        }
      }
    }
    
    if (currentBuild.currentResult == "SUCCESS"){

        echo "build success"
  
      stage('\u27A1 update the version file') {
          version = readFile('VERSION').trim()
          nextversion = make_version(version, "${release}")
          println("Next build number")
          println("${nextversion}")

          writeFile(file:'VERSION', text:"${nextversion}")
      }
      stage('\u27A1 git commit version file') {
          sshagent(['jenkins']) {
            sh """
              git config user.email \"jenkins@ioengage.cloud\"
              git config user.name \"Jenkins\"

              git add VERSION
              git commit -m "version update"
              git push --set-upstream origin version-test
            """
          }
      }
    }
    else {echo "build Failed"}
  }
}

def make_version(version, release="maintenance") {    
    version_list = version.tokenize(".")
    if (release == "major"){
        next_version_num = (version_list[0] as int) + 1
        new_version = next_version_num.toString() +'.0.0'
    }
    else if (release == "minor"){        
        next_version_num = (version_list[1] as int) + 1
        new_version = version_list[0]+'.'+next_version_num.toString() +'.0'
    }
    else {
        next_version_num = (version_list[2] as int ) + 1
        new_version = version_list[0]+'.'+version_list[1] +'.'+next_version_num.toString()
    }
    return new_version
}

def checkoutRepo(Map args) {
  git credentialsId: "${args.git_repo_creds_id}", url: "${args.git_repo}", branch: "${args.git_branch}"
}

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
    previous_build_result = currentBuild.getPreviousBuild().result
    def item = hudson.model.Hudson.instance.getItem('version test')
    def value = item.lastBuild.getEnvironment(null).get('release')
    echo "${previous_build_result}"
    echo "${value}"
    }
    
    container('docker') {
      docker.withRegistry(docker_repo_url, "ecr:${aws_region}:${docker_repo_creds_id}") {
        stage('\u27A1 Checkout git repo') {
          checkoutRepo(git_repo_creds_id: git_repo_creds_id, git_repo: 'git@bitbucket.org:imageoptions/io_engage_event.git', git_branch: "${branch}")
        }
        stage('\u27A1 Reading the version file') {
          println(currentBuild.getPreviousBuild().result)
          version = readFile('VERSION').trim()
          buildnumber_file = readFile('BUILDNUMBER').trim()

        if ("${release}" == "major"){
          major_version = make_version(version, "${release}")
          current_buildnumber = get_build_number("${release}", "${value}")
          buildVersion = "${major_version}-build-${current_buildnumber}"
        }
        else if ("${release}" == "minor"){
          minor_version = make_version(version, "${release}")
          current_buildnumber = get_build_number("${release}", "${value}")
          buildVersion = "${minor_version}-build-${current_buildnumber}"
        }
        else {
          regular_version = make_version(version)
          current_buildnumber = get_build_number("${value}")
          buildVersion = "${regular_version}-build-${current_buildnumber}" 
        }
          currentBuild.displayName = "${buildVersion}"
          currentBuild.result = 'FAILED'
        }
      }
    }
    
    if (currentBuild.currentResult == "SUCCESS"){
      stage('\u27A1 update the version file') {
        current_version = make_version(version, "${release}")
        current_buildnumber = get_build_number("${release}", "${value}")
        writeFile(file:'VERSION', text:"${current_version}")
        writeFile(file:'BUILDNUMBER', text:"${current_buildnumber}")
      }
      
      stage('\u27A1 git commit version file') {
          sshagent(['jenkins']) {
            sh """
              git config user.email \"jenkins@ioengage.cloud\"
              git config user.name \"Jenkins\"

              git add VERSION BUILDNUMBER
              git commit -m "version update to ${current_version}, Buildnumber update to ${current_buildnumber}"
              git push --set-upstream origin ${branch}
            """
          }
      }
    }
    else {
      stage('\u27A1 update the build file') {
        current_buildnumber = get_build_number("${release}", "${value}")
        writeFile(file:'BUILDNUMBER', text:"${current_buildnumber}")
      }
      stage('\u27A1 git commit build file') {
          sshagent(['jenkins']) {
            sh """
              git config user.email \"jenkins@ioengage.cloud\"
              git config user.name \"Jenkins\"

              git add VERSION BUILDNUMBER
              git commit -m "Buildnumber update to ${current_buildnumber}"
              git push --set-upstream origin ${branch}
            """
          }
      }
      echo "build failed"
    }
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

def get_build_number(release="maintenance", value) {
  
  if ((release == value) && previous_build_result == "FAILURE"){
    new_build_number = (buildnumber_file as int) + 1
  }
  else {
    new_build_number = 1
  }
  return new_build_number
}

def checkoutRepo(Map args) {
  git credentialsId: "${args.git_repo_creds_id}", url: "${args.git_repo}", branch: "${args.git_branch}"
}

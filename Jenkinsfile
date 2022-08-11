properties([pipelineTriggers([pollSCM('* * * * *')])])
node {
    stage("clone"){
        git "https://github.com/ozxval/DevOps3006.git"
    }
    stage("show files"){
        bat "dir"
    }
}

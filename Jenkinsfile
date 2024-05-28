pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                echo 'Building Docker image...'
                script {
                    def customImage = docker.build("giftvoucher:latest")
                    customImage.inside {
                        sh 'python main.py'
                    }
                }
            }
        }
        
        stage('Test') {
            steps {
                echo 'Testing...'
                script {
                    def customImage = docker.image("giftvoucher:latest")
                    customImage.inside {
                        sh 'python main.py'
                    }
                }
            }
        }
        
        stage('Deploy') {
            steps {
                echo 'Deploying...'
                // Add your deploy steps here
            }
        }
        
        stage('Copy Output') {
            steps {
                echo 'Copying output file to host machine...'
                script {
                    // Get the container ID of the running container
                    def containerId = sh(script: "docker ps -q -f ancestor=giftvoucher:latest", returnStdout: true).trim()
                    
                    // Define the paths
                    def containerPath = "/app/Output"
                    def hostPath = "C:/Users/natha/Documents/Deakin/Trimester 2/SIT223 - Professional Practice in Information Technology/6.2HD Create your DevOps Pipeline/Output"
                    
                    // Copy the file from the container to the host machine
                    sh "docker cp ${containerId}:${containerPath}/Mannys\\ Gift\\ Voucher\\ -\\ 1234567\\ \\$100.png ${hostPath}"
                }
            }
        }
    }
    
    post {
        always {
            echo 'Pipeline completed!'
        }
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}

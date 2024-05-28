pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                echo 'Building Docker image...'
                sh 'docker build -t giftvoucher:latest .'
            }
        }
        
        stage('Test') {
            steps {
                echo 'Testing...'
                sh 'docker run --name giftvoucher_test -d giftvoucher:latest'
            }
        }
        
        stage('Copy Output') {
            steps {
                echo 'Copying output file to host machine...'
                script {
                    // Define the paths
                    def containerPath = "/app/Output"
                    def hostPath = "C:/Users/natha/Documents/Deakin/Trimester 2/SIT223 - Professional Practice in Information Technology/6.2HD Create your DevOps Pipeline/Output"
                    
                    // Copy the file from the container to the host machine
                    sh "docker cp giftvoucher_test:${containerPath}/'Mannys Gift Voucher - 1234567 \$100.png' '${hostPath}'"
                }
            }
        }
        
        stage('Cleanup') {
            steps {
                echo 'Cleaning up...'
                sh 'docker rm -f giftvoucher_test'
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

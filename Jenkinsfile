pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                echo 'Building Docker image...'
                bat 'docker build -t giftvoucher:latest .'
            }
        }
        
        stage('Test') {
            steps {
                echo 'Removing any existing container named giftvoucher_test...'
                bat 'docker rm -f giftvoucher_test || true'
                
                echo 'Testing...'
                bat 'docker run --name giftvoucher_test giftvoucher:latest'
            }
        }

        stage('Code Quality Analysis') {
            steps {
                echo 'Testing code quality with SonarQube Analysis'
                withSonarQubeEnv('SonarQube') {
                    bat 'sonar-scanner -Dsonar.projectKey=giftvoucher_project -Dsonar.sources=./ -Dsonar.host.url=http://localhost:9000 -Dsonar.login=squ_8f4782cb397cf42f2dbdcf0eeb83cd5bb1e31431'
                }
            }
        }
        
        stage('Copy Output') {
            steps {
                echo 'Copying output file to host machine...'
                script {
                    // Define the paths
                    def containerPath = "/app/Output"
                    def hostPath = "C:/Users/natha/Documents/Deakin/Trimester 2/SIT223 - Professional Practice in Information Technology/6.2HD Create your DevOps Pipeline/Output"
                    def fileName = "Mannys Gift Voucher - 1234567 \$100.png"
                    
                    // Use double quotes around the entire paths to handle special characters properly
                    bat "docker cp \"giftvoucher_test:${containerPath}/${fileName}\" \"${hostPath}\""
                }
            }
        }
        
        stage('Cleanup') {
            steps {
                echo 'Cleaning up...'
                bat 'docker rm -f giftvoucher_test'
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

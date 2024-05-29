pipeline {
    agent any
    
    environment {
        // Fetch the SonarQube token from Jenkins credentials
        SONARQUBE_TOKEN = credentials('SONARQUBE_TOKEN')
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building Docker image...'
                // Build docker image of the application
                bat 'docker build -t giftvoucher:latest .'
            }
        }
        
        stage('Test') {
            steps {
                // Remove any prexisting container to avoid conflicts
                echo 'Removing any existing container named giftvoucher_test...'
                bat 'docker rm -f giftvoucher_test || true'
                
                // Run tests in new Docker container
                echo 'Testing...'
                bat 'docker run --name giftvoucher_test giftvoucher:latest'
            }
        }

        stage('Code Quality Analysis') {
            steps {
                echo 'Testing code quality with SonarQube Analysis'
                withSonarQubeEnv('SonarQube') {
                    script {
                        // Define path to the SonarQube Scanner
                        def scannerHome = tool 'SonarQube Scanner'

                        // Run SonarQube Scanner to analyze code quality
                        bat "${scannerHome}/bin/sonar-scanner -Dsonar.projectKey=giftvoucher_project -Dsonar.sources=./ -Dsonar.host.url=http://localhost:9000 -Dsonar.login=${SONARQUBE_TOKEN}"
                    }
                }
                echo 'SonarQube Analysis completed.'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application with Docker Compose...'

                // Deploy application with Docker Compose
                bat 'docker-compose up -d'
                echo 'Application deployed with Docker Compose.'
            }
        }
        
        stage('Copy Output') {
            steps {
                // Copies file from Docker Container to local machine so I can review it
                echo 'Copying output file to host machine...'
                script {
                    // Define paths of the Docker Container and local machine
                    def containerPath = "/app/Output"
                    def hostPath = "C:/Users/natha/Documents/Deakin/Trimester 2/SIT223 - Professional Practice in Information Technology/6.2HD Create your DevOps Pipeline/Output"
                    def fileName = "Mannys Gift Voucher - 1234567 \$100.png"
                    
                    // Copy file from Docker Container to local machine
                    bat "docker cp \"giftvoucher_test:${containerPath}/${fileName}\" \"${hostPath}\""
                }
                echo 'Output file copied to host machine.'
            }
        }
        
        stage('Cleanup') {
            steps {
                echo 'Cleaning up...'

                // Stop and remove all Docker Compose services
                bat 'docker-compose down'

                // Remove the test Docker Container
                bat 'docker rm -f giftvoucher_test'
                echo 'Cleanup completed.'
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

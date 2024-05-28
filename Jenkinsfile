pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                
                // Build the Docker image
                bat 'docker build -t giftvoucher:latest .'
            }
        }
        
        stage('Test') {
            steps {
                echo 'Testing...'
                // Run the main.py script which includes test
                bat 'python main.py'
            }
        }
        
        stage('Deploy') {
            steps {
                echo 'Deploying...'
                // Add deploy steps here
            }
        }

        stage('Release') {
            steps {
                echo 'Releasing...'
                // Add Release steps here
            }
        }
    }
    
    post {
        always {
            echo 'Cleaning up...'
            // Add any cleanup steps here
        }
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}

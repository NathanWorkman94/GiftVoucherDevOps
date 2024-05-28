pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                // Install dependencies using pip
                bat 'pip install -r requirements.txt'
            }
        }
        
        stage('Test') {
            steps {
                echo 'Testing...'
                // Run tests using pytest
                bat 'pytest tests'
            }
        }
        
        stage('Deploy') {
            steps {
                echo 'Deploying...'
                // Add deploy steps here
            }
        }
    }
    
    post {
        always {
            echo 'Cleaning up...'
            // Add cleanup steps here
        }
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}

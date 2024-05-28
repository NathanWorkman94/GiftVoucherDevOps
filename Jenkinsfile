pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                // Install dependencies
                sh 'pip install -r requirements.txt'
                // Run backend tests
                sh 'pytest tests'
            }
        }
        
        stage('Test') {
            steps {
                echo 'Testing...'
                // Run additional tests if necessary
            }
        }
        
        stage('Deploy') {
            steps {
                echo 'Deploying...'
                // Add your deploy steps here
            }
        }
    }
    
    post {
        always {
            echo 'Cleaning up...'
            // Add any cleanup steps here
        }
    }
}

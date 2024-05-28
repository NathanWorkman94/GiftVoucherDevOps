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
                // Run the main.py script which includes the test
                bat 'python main.py'
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
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}

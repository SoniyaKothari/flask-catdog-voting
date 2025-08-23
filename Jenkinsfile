@Library("flask-lib") _

pipeline 
{
    agent any

    stages 
    {
        stage('Docker build') 
        {
            steps 
            {
                script
                {
                    build("flask-project","latest","soniya06")
                }
            }
        }

        stage('Docker push') 
        {
            steps 
            {
               echo "hi"
            }
        }

        stage('Deploy to nginx')
        {
            steps
            {
                sh '''

                    echo "Stopping container if already exists"
                    docker rm -f flask-container || true

                    echo "Pulling latest image"
                    docker pull soniya06/flask-project:latest

                    echo "Running the container via NGINX"
                    docker run -d --name flask-container soniya06/flask-project:latest

                    echo "Restarting NGINX"
                    sudo systemctl restart nginx

                '''
            }
        }
    }
}

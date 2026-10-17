pipeline {
    agent any

    options {
        skipDefaultCheckout()
    }

    environment {
        STUDENT_NAME = 'Сүлеймен'
        STUDENT_SURNAME = 'Елдосұлы'
        STUDENT_GROUP = 'IT2-2310'
        STUDENT_ID = '38320'
        IMAGE_NAME = 'eldosuly-suleimen-devops'
        CONTAINER_NAME = 'eldosuly-suleimen-container'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                sh 'git rev-parse --short HEAD'
            }
        }

        stage('Build') {
            steps {
                sh 'python3 -m compileall -q app'
            }
        }

        stage('Test') {
            steps {
                sh 'python3 -m unittest discover -s tests -v'
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t "$IMAGE_NAME" .'
            }
        }

        stage('Docker Run') {
            steps {
                sh '''
                    docker rm -f "$CONTAINER_NAME" 2>/dev/null || true
                    docker run -d --name "$CONTAINER_NAME" -p 8000:8000 \
                        -e STUDENT_NAME -e STUDENT_SURNAME \
                        -e STUDENT_GROUP -e STUDENT_ID \
                        "$IMAGE_NAME"
                    sleep 2
                    docker exec "$CONTAINER_NAME" python -c \
                        'from urllib.request import urlopen; assert urlopen("http://127.0.0.1:8000/health").status == 200'
                    docker logs "$CONTAINER_NAME"
                '''
                echo "Student: ${env.STUDENT_NAME} ${env.STUDENT_SURNAME}"
                echo "Group: ${env.STUDENT_GROUP}"
                echo "Student ID: ${env.STUDENT_ID}"
            }
        }
    }
}

pipeline {
    agent any

    environment {
        VENV_DIR        = '.venv'
        TEST_DIR        = 'tests_'
        REPORTS_DIR     = 'reports'
        PYTHON_VERSION  = '3.11'
    }

    options {
        timestamps()
        timeout(time: 30, unit: 'MINUTES')
        buildDiscarder(logRotator(numToKeepStr: '10'))
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                    python${PYTHON_VERSION} -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install pytest pytest-html pytest-cov
                    if [ -f requirements.txt ]; then
                        pip install -r requirements.txt
                    fi
                '''
            }
        }

        stage('Lint (optional)') {
            steps {
                sh '''
                    . ${VENV_DIR}/bin/activate
                    pip install flake8 --quiet
                    flake8 ${TEST_DIR} --max-line-length=120 --statistics || true
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    . ${VENV_DIR}/bin/activate
                    mkdir -p ${REPORTS_DIR}
                    pytest ${TEST_DIR} \
                        --tb=short \
                        -v \
                        --html=${REPORTS_DIR}/report.html \
                        --self-contained-html \
                        --cov=. \
                        --cov-report=xml:${REPORTS_DIR}/coverage.xml \
                        --cov-report=html:${REPORTS_DIR}/coverage_html \
                        --junitxml=${REPORTS_DIR}/junit.xml
                '''
            }
        }
    }

    post {
        always {
            // Publish JUnit test results
            junit allowEmptyResults: true, testResults: "${REPORTS_DIR}/junit.xml"

            // Publish HTML test report
            publishHTML([
                allowMissing         : false,
                alwaysLinkToLastBuild: true,
                keepAll              : true,
                reportDir            : "${REPORTS_DIR}",
                reportFiles          : 'report.html',
                reportName           : 'Pytest HTML Report'
            ])

            // Publish coverage report
            publishHTML([
                allowMissing         : false,
                alwaysLinkToLastBuild: true,
                keepAll              : true,
                reportDir            : "${REPORTS_DIR}/coverage_html",
                reportFiles          : 'index.html',
                reportName           : 'Coverage Report'
            ])

            // Archive artifacts
            archiveArtifacts artifacts: "${REPORTS_DIR}/**", fingerprint: true
        }

        success {
            echo '✅ All tests passed!'
        }

        failure {
            echo '❌ Tests failed. Check the reports for details.'
            // Uncomment to send email on failure:
            // mail to: 'your-team@example.com',
            //      subject: "Build FAILED: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
            //      body: "Check Jenkins: ${env.BUILD_URL}"
        }

        cleanup {
            // Remove the virtual environment to keep workspace clean
            sh 'rm -rf ${VENV_DIR}'
        }
    }
}
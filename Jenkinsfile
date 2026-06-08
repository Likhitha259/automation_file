pipeline {
    agent any

    environment {
        VENV_DIR    = '.venv'
        TEST_DIR    = 'tests_'
        REPORTS_DIR = 'reports'
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
                bat '''
                    python -m venv %VENV_DIR%
                    call %VENV_DIR%\\Scripts\\activate.bat
                    python -m pip install --upgrade pip
                    pip install pytest pytest-html pytest-cov
                    if exist requirements.txt (
                        pip install -r requirements.txt
                    )
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                    call %VENV_DIR%\\Scripts\\activate.bat
                    if not exist %REPORTS_DIR% mkdir %REPORTS_DIR%
                    pytest %TEST_DIR% ^
                        --tb=short ^
                        -v ^
                        --html=%REPORTS_DIR%\\report.html ^
                        --self-contained-html ^
                        --cov=. ^
                        --cov-report=xml:%REPORTS_DIR%\\coverage.xml ^
                        --junitxml=%REPORTS_DIR%\\junit.xml
                '''
            }
        }
    }

    post {
        always {
            // Publish JUnit test results (built-in, no extra plugin needed)
            junit allowEmptyResults: true, testResults: "${REPORTS_DIR}/junit.xml"

            // Archive all reports as build artifacts
            archiveArtifacts artifacts: "${REPORTS_DIR}/**", fingerprint: true, allowEmptyArchive: true
        }

        success {
            echo '✅ All tests passed!'
        }

        failure {
            echo '❌ Tests failed. Download the archived reports from the Build Artifacts.'
        }

        cleanup {
            bat 'if exist %VENV_DIR% rmdir /s /q %VENV_DIR%'
        }
    }
}

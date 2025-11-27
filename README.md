Python Sonar Demo – Proyecto FastAPI con SonarCloud

Este es un proyecto básico en Python + FastAPI + Pytest configurado para integrarse con SonarCloud usando GitHub Actions.

🚀 1. Requisitos

Python 3.10+

GitHub

Cuenta en SonarCloud

Token SONAR_TOKEN creado en
GitHub → Settings → Secrets → Actions

📦 2. Instalación
pip install -r requirements.txt

🧪 3. Ejecutar pruebas
pytest --cov=app --cov-report=xml


Esto genera el reporte coverage.xml requerido por SonarCloud.

☁️ 4. Integración con SonarCloud

Configurar:

sonar-project.properties

sonar.projectKey=python_sonar_demo
sonar.organization=tu_organization
sonar.sources=app
sonar.tests=tests
sonar.python.coverage.reportPaths=coverage.xml

🤖 5. GitHub Actions

Archivo:

.github/workflows/sonar.yml


El workflow ejecuta:

Checkout

Instala dependencias

Ejecuta pruebas

Genera cobertura

Envía resultados a SonarCloud

Se dispara en:

Push a la rama main

Pull Requests

📊 6. Ver resultados en SonarCloud

Ingresar a:
https://sonarcloud.io

Buscar el proyecto con la llave configurada.

✔️ 7. Estructura del proyecto
python-sonar-demo/
 ├─ app/
 ├─ tests/
 ├─ .github/workflows/
 ├─ requirements.txt
 ├─ sonar-project.properties
 └─ README.md
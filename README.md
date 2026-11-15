# devops-ci-app

Практическая работа № 10. Исаев Иса, ЭФБО-02-24.

Flask-приложение с двумя адресами: `/` и `/health`.

CI: Pylint → pytest → сборка Docker → smoke-test → GHCR.
В PR выполняются проверки. Образ публикуется после push в `main`.

- Образ: `ghcr.io/iisa47642/devops-ci-app`.
- Теги: полный SHA коммита и `latest`.
- Workflow: `.github/workflows/ci.yml`.

Образ собирается на ARM runner, чтобы запускаться в нашей Ubuntu VM в UTM.

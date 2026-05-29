# Credit Underwriting API

Real-time credit decisioning service that evaluates consumer eligibility and pricing for Affirm transactions. Built with Python/Flask, integrates with ML feature stores and third-party credit bureaus. Runs on Kubernetes with Aurora MySQL for transactional state.

**Stack**: Python 3.11, Flask, MySQL (Aurora), Redis, Apache Spark

**Local setup**: `make docker-up && make migrate && make run`
import foam
from flask import Flask
from config import FOAM_API_KEY, IS_PRODUCTION

app = Flask(__name__)

# Initialize Foam observability
foam.init(
    service_name="partner-integration-service",
    api_key=FOAM_API_KEY,
    is_production=IS_PRODUCTION,
    capture_http_requests=True,
    capture_http_responses=True
)

if __name__ == "__main__":
    app.run()
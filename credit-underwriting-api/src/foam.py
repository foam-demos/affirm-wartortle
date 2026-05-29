import foam
from flask import Flask
from config import FOAM_API_KEY, IS_PRODUCTION

app = Flask(__name__)

# Initialize Foam observability
foam.init(
    service_name="credit-underwriting-api",
    api_key=FOAM_API_KEY,
    is_production=IS_PRODUCTION,
    capture_sql=True,
    capture_redis=True
)

if __name__ == "__main__":
    app.run()
import foam
import asyncio
from config import FOAM_API_KEY, IS_PRODUCTION

# Initialize Foam observability
foam.init(
    service_name="online-storage-proxy",
    api_key=FOAM_API_KEY,
    is_production=IS_PRODUCTION,
    capture_sql=True,
    capture_connection_pools=True
)

if __name__ == "__main__":
    asyncio.run(main())
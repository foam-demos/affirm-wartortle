# Partner Integration Service

Manages merchant partner API integrations, webhook delivery, and external developer tooling. Handles callbacks for order updates, refunds, and authorization events.

**Stack**: Python 3.11, Flask, Redis (queue), MySQL (Aurora)

**Local setup**: `make docker-up && make run`
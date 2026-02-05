from flask import Flask
from reports.apis.report_api import report_api_blueprint
from reports.apis.source_api import source_api_blueprint
from config.flask_app_config import Config
from flasgger import Swagger
import logging

# Configure logging
logging.basicConfig(
    level=getattr(logging, Config.LOG_LEVEL),
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

app = Flask("Report Generator by Szymen")
app.config.from_object(Config)

logger.info("Application started")

# Initialize Swagger
swagger = Swagger(app)



# Register Blueprints
app.register_blueprint(report_api_blueprint, url_prefix='/api/reports')
app.register_blueprint(source_api_blueprint, url_prefix='/api/sources')

if __name__ == '__main__':
    app.run(debug=True)
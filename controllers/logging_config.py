import logging
from google.cloud import logging as cloud_logging

def setup_logging(credentials_path):
    client = cloud_logging.Client.from_service_account_json(credentials_path)
    
    client.setup_logging()

    logging.basicConfig(level=logging.INFO)

    return logging.getLogger('cloudLogger')

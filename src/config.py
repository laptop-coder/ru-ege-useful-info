import os
import logging


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


VK_AUTH_TOKEN = os.getenv("VK_AUTH_TOKEN", "")
if VK_AUTH_TOKEN == "":
    logger.error("Please specify VK_AUTH_TOKEN env variable")
    os._exit(1)

GROUP_ID = os.getenv("GROUP_ID", "")
if GROUP_ID == "":
    logger.error("Please specify GROUP_ID env variable")
    os._exit(1)

PATH_TO_DB = os.getenv("PATH_TO_DB", "")
if PATH_TO_DB == "":
    logger.error("Please specify PATH_TO_DB env variable")
    os._exit(1)

PATH_TO_INITIAL_SQL_QUERIES = os.getenv("PATH_TO_INITIAL_SQL_QUERIES", "")
if PATH_TO_INITIAL_SQL_QUERIES == "":
    logger.error("Please specify PATH_TO_INITIAL_SQL_QUERIES env variable")
    os._exit(1)

PATH_TO_GET_INFO_SQL_QUERIES = os.getenv("PATH_TO_GET_INFO_SQL_QUERIES", "")
if PATH_TO_GET_INFO_SQL_QUERIES == "":
    logger.error("Please specify PATH_TO_GET_INFO_SQL_QUERIES env variable")
    os._exit(1)

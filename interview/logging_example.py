import logging

# Configure the logging
logging.basicConfig(
    level=logging.DEBUG,  # Set the minimum level of messages to log
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Log message format
    datefmt='%Y-%m-%d %H:%M:%S',  # Date format in the log messages
    handlers=[
        logging.FileHandler('app.log'),  # Log to a file named 'app.log'
        logging.StreamHandler()  # Also log to the console
    ]
)

# Create a logger object
logger = logging.getLogger(__name__)

# Example usage of different log levels
logger.debug('This is a debug message')  # For debugging, lower level
logger.info('This is an info message')  # General information
logger.warning('This is a warning message')  # Something unexpected, but not an error
logger.error('This is an error message')  # A more serious problem
logger.critical('This is a critical message')  # A very serious error, possibly requiring the program to stop

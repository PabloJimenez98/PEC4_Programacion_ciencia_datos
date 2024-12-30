from datetime import datetime
import sys

class Logger:
    def __init__(self, name="MonegrosLogger"):
        self.name = name

    def log(self, message, level="INFO"):
        """
        Logs a message with timestamp and level.
        
        Args:
            message (str): Message to log
            level (str): Log level (INFO, WARNING, ERROR)
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"[{timestamp}] {level} - {self.name}: {message}"
        print(log_message, file=sys.stdout if level != "ERROR" else sys.stderr)

    def info(self, message):
        """Logs an info message"""
        self.log(message, "INFO")

    def warning(self, message):
        """Logs a warning message"""
        self.log(message, "WARNING")

    def error(self, message):
        """Logs an error message"""
        self.log(message, "ERROR")

if __name__ == "__main__":
    # Example usage
    logger = Logger("TestLogger")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")

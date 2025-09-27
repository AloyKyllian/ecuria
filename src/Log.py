import logging
import sys


# ================= ColorFormatter =================
class ColorFormatter(logging.Formatter):
    COLORS = {
        "DEBUG": "\033[94m",  # Bleu
        "INFO": "\033[92m",  # Vert
        "WARNING": "\033[93m",  # Jaune
        "ERROR": "\033[91m",  # Rouge
        "CRITICAL": "\033[95m",  # Magenta
    }
    RESET = "\033[0m"

    def format(self, record):
        levelname = record.levelname
        color = self.COLORS.get(levelname, "")
        if color:
            record.levelname = f"{color}{levelname}{self.RESET}"
            record.msg = f"{color}{record.msg}{self.RESET}"
        return super().format(record)


# ================= UserFilter =================
class UserFilter(logging.Filter):
    def __init__(self, user="init"):
        super().__init__()
        self.user = user

    def set_user(self, new_user):
        self.user = new_user

    def filter(self, record):
        record.user = self.user
        return True


# ================= Exception hook =================
error_occurred = False  # Global flag pour savoir si une erreur est survenue


def handle_exception(exc_type, exc_value, exc_traceback):
    global error_occurred
    if not issubclass(exc_type, KeyboardInterrupt):
        error_occurred = True
        logger = logging.getLogger("App")
        logger.error(
            "Exception non capturée !", exc_info=(exc_type, exc_value, exc_traceback)
        )


sys.excepthook = handle_exception


# ================= Setup logger =================
def setup_logger(
    name: str,
    user: str = "init",
    log_file: str = "app.log",
    file_level=logging.DEBUG,
    console_level=logging.INFO,
):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)  # Niveau global minimum

    if not logger.handlers:
        # Filter utilisateur
        user_filter = UserFilter(user)
        logger.user_filter = user_filter

        # Formatter commun
        fmt_str = "%(user)s - %(asctime)s - %(name)s - %(levelname)s - %(message)s"
        file_formatter = logging.Formatter(fmt_str)
        console_formatter = ColorFormatter(fmt_str)

        # Handler fichier
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(file_level)
        file_handler.setFormatter(file_formatter)
        file_handler.addFilter(user_filter)
        logger.addHandler(file_handler)

        # Handler console
        console_handler = logging.StreamHandler()
        console_handler.setLevel(console_level)
        console_handler.setFormatter(console_formatter)
        console_handler.addFilter(user_filter)
        logger.addHandler(console_handler)

    return logger

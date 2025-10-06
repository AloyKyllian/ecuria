# from Mail import envoyer_email
import logging
import atexit
import sys
import signal
from Mail import envoyer_email

# ================= ColorFormatter =================
class ColorFormatter(logging.Formatter):
    COLORS = {
        "DEBUG": "\033[94m",   # Bleu
        "INFO": "\033[92m",    # Vert
        "WARNING": "\033[93m", # Jaune
        "ERROR": "\033[91m",   # Rouge
        "CRITICAL": "\033[95m",# Magenta
    }
    RESET = "\033[0m"

    def format(self, record):
        msg = super().format(record)
        color = self.COLORS.get(record.levelname.replace("\033[0m","").replace("\033[91m","").replace("\033[92m","").replace("\033[93m","").replace("\033[94m","").replace("\033[95m",""), "")
        if color:
            msg = f"{color}{msg}{self.RESET}"
        return msg

# ================= Logger avec compteurs =================
class LoggerCounter(logging.Filter):
    _global_error_count = 0
    _global_warning_count = 0
    _user_name = "init"
    _already_printed = False  

    def __init__(self, name=None, log_file="app.log", user=None):
        super().__init__()
        import inspect, os
        
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)

        if name == "Planning":
            print(name)
            # Rotation simple : on garde uniquement le log du lancement précédent
            if os.path.exists(log_file):
                if os.path.exists(log_file + ".1"):
                    os.remove(log_file + ".1")
                os.rename(log_file, log_file + ".1")

        # if not name:
        #     caller_file = inspect.stack()[1].filename
        #     name = os.path.splitext(os.path.basename(caller_file))[0]



        if user:
            LoggerCounter._user_name = user

        if not self.logger.handlers:
            fmt = "%(asctime)s - %(user)s - %(name)s - %(levelname)s - %(message)s"

            # Fichier unique
            file_handler = logging.FileHandler(log_file, encoding="utf-8")
            file_handler.setFormatter(logging.Formatter(fmt))
            file_handler.addFilter(self)
            self.logger.addHandler(file_handler)

            # Console avec couleur
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(ColorFormatter(fmt))
            console_handler.addFilter(self)
            self.logger.addHandler(console_handler)

        atexit.register(self._on_exit)
        sys.excepthook = self._handle_exception
        signal.signal(signal.SIGINT, self._handle_signal)
        signal.signal(signal.SIGTERM, self._handle_signal)

    def filter(self, record):
        # Compteurs
        if record.levelno == logging.WARNING:
            LoggerCounter._global_warning_count += 1
        elif record.levelno >= logging.ERROR:
            LoggerCounter._global_error_count += 1
        # Injection utilisateur pour le formatter
        record.user = LoggerCounter._user_name
        return True

    @staticmethod
    def set_user(user):
        LoggerCounter._user_name = user

    def _on_exit(self):
        if LoggerCounter._already_printed:
            return
        LoggerCounter._already_printed = True
        if LoggerCounter._global_warning_count > 0 or LoggerCounter._global_error_count > 0 and LoggerCounter._user_name.lower() != "admin":
            envoyer_email("aloykyllian31520@gmail.com","app.log", "app.log", "Rapport d'erreurs Ecuria", [])
        self.logger.info(
            f"Fin du programme : {LoggerCounter._global_warning_count} warning(s), "
            f"{LoggerCounter._global_error_count} erreur(s)."
        )

    def _handle_exception(self, exc_type, exc_value, exc_traceback):
        self.logger.error("Exception non capturée", exc_info=(exc_type, exc_value, exc_traceback))
        sys.exit(1)

    def _handle_signal(self, sig, frame):
        self.logger.error(f"Signal reçu ({sig}), fermeture du programme.")
        sys.exit(0)

    @staticmethod
    def get_counts():
        return LoggerCounter._global_warning_count, LoggerCounter._global_error_count

    @staticmethod
    def print_summary(logger):
        if not LoggerCounter._already_printed:
            LoggerCounter._already_printed = True
            logger.info(f"Fin du programme : {LoggerCounter._global_warning_count} warning(s), {LoggerCounter._global_error_count} erreur(s).")

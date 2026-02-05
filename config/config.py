
import os, sys

APP_ROOT = os.path.abspath( os.path.dirname(sys.argv[0]) )
DATA_FOLDER_NAME="/app/data"


CSV_SEPARATOR='|'
CSV_ENCODING="UTF-8"
REMOVE_HTML_AFTER=True

smtp_server = "smtp.office365.com"
smtp_port = 587

MAIL_FROM = "szymon.maslowski@example.com"
MAIL_PASSWORD = "pass"

SEND_MAILS = False
import os, sys

class Config:
    CSV_BASE_PATH = "path/to/csv/files"
    APP_ROOT = os.path.abspath(os.path.dirname(sys.argv[0]))

    STORAGE_ROOT_PATH = os.path.join( APP_ROOT, "_storage")

    SOURCE_PATH = os.path.join(STORAGE_ROOT_PATH, "sources")
    REPORT_PATH = os.path.join(STORAGE_ROOT_PATH, "reports")

    LOG_LEVEL = "DEBUG"
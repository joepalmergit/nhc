from glob import glob
from datetime import datetime


def get_files(extension="*"):
    extension = f"*.{extension}"

    result = glob(extension)

    return result


def get_current_date_time():
    result = datetime.today().strftime('%Y-%m-%d_%H-%M-%S')

    return result

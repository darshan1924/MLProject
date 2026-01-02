import sys
from src.logger import logging

def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    
    error_message = ("Error occurred in python script name [{file_name}] "
                     "line number [{line_number}] error message [{error}]".format(
                         file_name=file_name,
                         line_number=line_number,
                         error=str(error)
                     ))
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        # Call parent class __init__ with the original error message
        super().__init__(error_message)
        
        # Generate detailed message only once
        self.error_message_detail = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message_detail

# Setup basic logging
logging.basicConfig(level=logging.INFO)
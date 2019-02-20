import json
import logging
import socket


class GelfFormatter(logging.Formatter):

    def format(self, record):
        # GELF message
        log_dict = {
            'version': '1.1',
            'host': socket.gethostname(),
            'short_message': record.getMessage(),
            'timestamp': record.created,
            'level': int(record.levelno / 10),
            '_level_name': record._level_name,
            '_file': record.filename,
            '_module': record.module,
            '_func': record.funcName,
            '_line': record.lineno,
        }

        full_message = ''
        if record.exc_info:
            # Cache the traceback test to avoid converting it multiple times
            # (it's constant anyway)
            if not record.exc_text:
                record.exc_text = self.formatException(record.exc_info)
        if record.exc_text:
            full_message += record.exc_text
        if record.stack_info:
            if full_message[-1:] != '\n':
                full_message += '\n'
            full_message += self.formatStack(record.stack_info)
        if full_message:
            log_dict['full_message'] = full_message

        return json.dumps(log_dict)

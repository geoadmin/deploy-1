
import logging
import datetime
import json

class JSONFormatter(logging.Formatter):
    def __init__(self, host_name=None):
        self.host_name = host_name

        super(JSONFormatter, self).__init__()

    def format(self, record):
        data = {'message': record.msg,
                'timegenerated': datetime.datetime.utcnow().isoformat(),
                'type': 'deploy'}

        if self.host_name:
            data['host_name'] = self.host_name

        return json.dumps(data)

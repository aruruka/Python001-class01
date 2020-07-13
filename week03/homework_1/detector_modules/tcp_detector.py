import json
import subprocess
from detector_modules.base_detector import BaseDetector


class Detector(BaseDetector):

    def __init__(self, thread_num, ip_range, write_out_file=None):
        BaseDetector.__init__(self, thread_num, ip_range)
        self.write_out_file = write_out_file

    def detect_network(self, ip, **kwargs):
        # ip = '172.21.85.191'
        print(f'nmaping {ip}...')
        process = subprocess.Popen(
            ['sudo', 'timeout', '5', 'nmap', '-sS', ip],
            stdout=subprocess.PIPE,
            universal_newlines=True
        )
        data = {}
        # ip, return_code, output
        if self.write_out_file is not None:
            print(f'self.write_out_file is: {self.write_out_file}')
            data[ip] = {
                "return_code": -1,
                "output": None
            }
            print(data)
        json_output = ''
        while True:
            output = process.stdout.readline()
            if output.strip() != '':
                json_output += output.strip()+'\n'
            print(output.strip())
            # Do something else
            return_code = process.poll()
            if return_code is not None:
                data[ip]['return_code'] = return_code
                print('RETURN CODE', return_code)
                break
        data[ip]['output'] = json_output
        
        if data != {}:
            print(data)
            with open(self.write_out_file, "w+") as write_file:
                json.dump(data, write_file)

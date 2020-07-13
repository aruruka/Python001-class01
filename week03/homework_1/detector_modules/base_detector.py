from concurrent.futures import ThreadPoolExecutor


class BaseDetector(object):
    def __init__(self, thread_num=1, ip_range='127.0.0.1'):
        self.thread_num = thread_num
        self.ip_range = ip_range
        # print(f'self.ip_range is: {self.ip_range}')
        print('This is parent class BaseDetector.')

    def get_detector_results(self, **kwargs):
        with ThreadPoolExecutor(max_workers=self.thread_num) as executor:
            executor.map(self.detect_network, self.ip_range, timeout=5.0)
            # print(future.result())
            # data = future.result()
            # return json.dumps({'data': data})

    def detect_network(self, ip, **kwargs):
        raise NotImplementedError

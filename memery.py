import logging
import time
import os

def main(req):
    logging.info('Python HTTP trigger function processed a request.')

    # 获取查询参数或请求体中的参数
    duration = int(req.params.get('duration', 10))  # 默认消耗 10 秒
    memory_load = int(req.params.get('memory', 2048))  # 默认消耗 2048 MB

    # 消耗 CPU 资源
    start_time = time.time()
    while time.time() - start_time < duration:
        pass

    # 消耗内存资源
    dummy_data = ' ' * (memory_load * 1024 * 1024)  # 分配指定大小的内存

    return f"Resource consumption complete! Duration: {duration}s, Memory: {memory_load}MB."

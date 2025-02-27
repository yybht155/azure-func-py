import azure.functions as func
import logging
import time

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)


@app.route(route="http_trigger")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")

    start_time = time.time()  # 记录开始时间

    # 添加延迟1秒
    time.sleep(5)

    name = req.params.get("name")
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get("name")

    end_time = time.time()  # 记录结束时间
    duration = end_time - start_time  # 计算执行时间

    if name:
        return func.HttpResponse(
            f"Hello, {name}. This HTTP triggered function executed successfully in {duration:.2f} seconds."
        )
    else:
        return func.HttpResponse(
            f"This HTTP triggered function executed successfully in {duration:.2f} seconds. Pass a name in the query string or in the request body for a personalized response.",
            status_code=200,
        )

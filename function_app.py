import azure.functions as func
import logging
import time

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="http_trigger")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    start_time = time.time()
    logging.info("Python HTTP trigger function processed a request.")

    name = req.params.get("name")
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get("name")

    if name:
        response_message = f"Hello, {name}. This HTTP triggered function executed successfully."
    else:
        response_message = "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response."

    end_time = time.time()
    elapsed_time = end_time - start_time
    logging.info(f"Request processed in {elapsed_time:.2f} seconds")

    return func.HttpResponse(response_message)

import azure.functions as func
import logging
from zipimport import zipimporter


myLoader = zipimporter("A1.zip")
myDeploy = myLoader.load_module("A1\\myname")
# Initialize the function app with anonymous HTTP authorization level
app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)
    
# Define the HTTP trigger function
@app.route(route="http_trigger")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    name = myDeploy.getmyname()
    response_message = (
            f"Hello {name}.\n"
        )
    return func.HttpResponse(response_message, status_code=200)

from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from flask_cors import CORS

# API Info
info = Info(
    title="Fashion Classification API",
    version="1.0.0",
    description="Fashion Classification API for image classification tasks",
)

# Initialize Flask app with OpenAPI
app = OpenAPI(__name__, info=info)
CORS(app)

# API Tags
home_tag = Tag(
    name="Docs",
    description="Documentation selection: Swagger, Redoc or ReDoc"
)


@app.get('/', tags=[home_tag])
def home():
    """Redirect to /openapi, screen that allows choosing the documentation style.
    """
    return redirect('/openapi/swagger')

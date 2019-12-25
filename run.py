from app import app, db
from app.models import User

@app.shell_context_processor
def shell_config():
    return {"User": User, "db": db}

app.run(debug=True)
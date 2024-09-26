from server.app import app
import uvicorn

uvicorn.run(app,port=5000)
from fastapi import FastAPI

app = FastAPI()

@app.get("/hello_world_i_am_mk")
def hello_world():
    return {"message": "Hello, world! I am mk"}

# Entry point for running the application

def main():
    """Run the FastAPI application using uvicorn.

    This function is intentionally simple to avoid side effects during
    imports. It is only executed when the module is run as a script.
    """
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()

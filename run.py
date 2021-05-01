from app import create_app

fastApp = create_app()

# uvicorn app:app --reload
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(fastApp, host='127.0.0.1', port=9998)
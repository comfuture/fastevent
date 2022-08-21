from fastevent.app import create_app


if __name__ == "__main__":
    import uvicorn

    app = create_app()
    uvicorn.run(app, port=4000)

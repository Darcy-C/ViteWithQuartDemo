from quart import Quart, render_template
from app.utils.context_processor import app_context_processor__asset

quart_app = Quart(__name__)
quart_app.context_processor(app_context_processor__asset)


@quart_app.get("/")
async def home():
    return await render_template("home.jinja.html")


def run(debug=None):
    quart_app.run(port=5002, debug=debug)


if __name__ == "__main__":
    run()

from functools import lru_cache
from quart import current_app, url_for
import json

# you may launch vite first: npm run dev
VITE_ENDPOINT = "http://localhost:5173"


@lru_cache()
def get_manifest():
    print("start loading manifest")
    with open("./app/static/bundle/manifest.json", "r", encoding="utf-8") as f:
        return json.load(f)


def app_context_processor__asset():
    IS_DEV: bool = current_app.debug

    def _asset_dev(path: str) -> str:
        return VITE_ENDPOINT + path

    def _asset_prod(path: str) -> str:
        # i like to add / when templating, static will add another one, so i
        # remove the possible prefix slash, that's just a personal preference.
        path = path.removeprefix("/")
        path = get_manifest()[path]["file"]
        path = "bundle/" + path
        return url_for("static", filename=path)

    return {
        "asset": _asset_dev if IS_DEV else _asset_prod,
        "is_prod": not IS_DEV,
    }

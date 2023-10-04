from fastapi import FastAPI

from theme_searcher.models import Theme, SuccessResp, ThemeSearchReq
from theme_searcher.storage import PhraseTree

app = FastAPI()
storage = PhraseTree()


@app.post("/theme")
async def theme_add(theme: Theme):
    await storage.add_theme(theme)
    return SuccessResp(success=True)


@app.post("/theme/search")  # POST, потому что мы создаем новый поисковой запрос
async def theme_search(search: ThemeSearchReq):
    return await storage.search(search.query)

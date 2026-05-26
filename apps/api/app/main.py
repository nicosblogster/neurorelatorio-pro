from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import protocols, reports

app = FastAPI(
    title="NeuroRelatorio Pro API",
    version="0.1.0",
    description="API inicial para gestao etica de relatorios neuropsicopedagogicos.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(protocols.router)
app.include_router(reports.router)


@app.get("/health", tags=["system"])
def health() -> dict[str, str]:
    return {"status": "ok", "service": "neurorelatorio-pro-api"}

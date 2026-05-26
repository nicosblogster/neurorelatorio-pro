import json
from functools import lru_cache
from pathlib import Path

from app.schemas import FillableTabTemplate, Protocol

SEED_DIR = Path(__file__).resolve().parents[1] / "seed"


@lru_cache
def load_protocols() -> list[Protocol]:
    with (SEED_DIR / "protocols.json").open(encoding="utf-8") as seed_file:
        rows = json.load(seed_file)
    return [Protocol.model_validate(row) for row in rows]


def get_protocol(protocol_id: str) -> Protocol | None:
    return next((protocol for protocol in load_protocols() if protocol.id == protocol_id), None)


@lru_cache
def load_fillable_tabs() -> list[FillableTabTemplate]:
    with (SEED_DIR / "fillable_tabs.json").open(encoding="utf-8") as seed_file:
        rows = json.load(seed_file)
    return [FillableTabTemplate.model_validate(row) for row in rows]

# generated by datamodel-codegen:
#   filename:  storage.json

from __future__ import annotations

from typing import Dict

from pydantic import BaseModel, Field


class TzbtcStorage(BaseModel):
    big_map: Dict[str, str]
    bool: bool
    lambda_: str = Field(..., alias='lambda')
    nat: str

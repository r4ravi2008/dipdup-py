# generated by datamodel-codegen:
#   filename:  create_auction.json

from __future__ import annotations

from pydantic import BaseModel


class CreateAuctionParameter(BaseModel):
    auction_id: str
    bid_amount: str
    end_timestamp: str
    token_address: str
    token_amount: str
    token_id: str

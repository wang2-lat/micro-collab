from dataclasses import dataclass


@dataclass
class Campaign:
    name: str
    budget: float
    target_audience: str
    niche: str


@dataclass
class Influencer:
    name: str
    niche: str
    followers: int
    rate: float

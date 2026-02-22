import json
import os
from pathlib import Path
from typing import List, Optional
from models import Campaign, Influencer


class Storage:
    def __init__(self, data_dir: str = ".micro-collab"):
        self.data_dir = Path.home() / data_dir
        self.data_dir.mkdir(exist_ok=True)
        self.campaigns_file = self.data_dir / "campaigns.json"
        self.influencers_file = self.data_dir / "influencers.json"
    
    def save_campaign(self, campaign: Campaign):
        campaigns = self._load_json(self.campaigns_file, [])
        campaigns.append(campaign.__dict__)
        self._save_json(self.campaigns_file, campaigns)
    
    def save_influencer(self, influencer: Influencer):
        influencers = self._load_json(self.influencers_file, [])
        influencers.append(influencer.__dict__)
        self._save_json(self.influencers_file, influencers)
    
    def get_campaign(self, name: str) -> Optional[Campaign]:
        campaigns = self._load_json(self.campaigns_file, [])
        for c in campaigns:
            if c["name"] == name:
                return Campaign(**c)
        return None
    
    def get_all_campaigns(self) -> List[Campaign]:
        campaigns = self._load_json(self.campaigns_file, [])
        return [Campaign(**c) for c in campaigns]
    
    def get_all_influencers(self) -> List[Influencer]:
        influencers = self._load_json(self.influencers_file, [])
        return [Influencer(**i) for i in influencers]
    
    def _load_json(self, file_path: Path, default):
        if not file_path.exists():
            return default
        with open(file_path, "r") as f:
            return json.load(f)
    
    def _save_json(self, file_path: Path, data):
        with open(file_path, "w") as f:
            json.dump(data, f, indent=2)

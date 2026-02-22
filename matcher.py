from typing import List, Tuple
from models import Campaign, Influencer


class Matcher:
    def find_matches(
        self, campaign: Campaign, influencers: List[Influencer]
    ) -> List[Tuple[Influencer, float]]:
        """Find matching influencers and return them with match scores"""
        matches = []
        
        for influencer in influencers:
            if influencer.rate > campaign.budget:
                continue
            
            score = self._calculate_match_score(campaign, influencer)
            if score > 0:
                matches.append((influencer, score))
        
        matches.sort(key=lambda x: x[1], reverse=True)
        return matches
    
    def _calculate_match_score(self, campaign: Campaign, influencer: Influencer) -> float:
        """Calculate match score between campaign and influencer"""
        score = 0.0
        
        # Niche match (most important)
        if campaign.niche.lower() == influencer.niche.lower():
            score += 0.6
        elif campaign.niche.lower() in influencer.niche.lower() or influencer.niche.lower() in campaign.niche.lower():
            score += 0.3
        
        # Follower count (micro-influencers: 1k-100k)
        if 1000 <= influencer.followers <= 100000:
            score += 0.2
        elif influencer.followers < 1000:
            score += 0.05
        
        # Budget efficiency
        if influencer.rate <= campaign.budget * 0.5:
            score += 0.2
        elif influencer.rate <= campaign.budget * 0.8:
            score += 0.1
        
        return score

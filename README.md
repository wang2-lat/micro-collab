# micro-collab

A CLI tool connecting SaaS companies with micro-influencers for authentic product promotion.

## Problem

SaaS startups struggle to find authentic micro-influencers for product promotion, while content creators seek relevant sponsorship opportunities. Traditional advertising is expensive and often ineffective compared to genuine user testimonials.

## Features

- Register SaaS company campaigns with budget and target audience
- Register micro-influencer profiles with niche and follower count
- Match and recommend suitable influencers for campaigns based on criteria
- View all registered campaigns and influencers

## Installation


## Usage

### Register a Campaign


### Register an Influencer


### Find Matching Influencers


### List All Campaigns


### List All Influencers


## Data Storage

Data is stored in JSON files in the `~/.micro-collab` directory.

## Tech Stack

- typer: CLI framework
- rich: Terminal formatting and tables
# Install dependencies
pip install -r requirements.txt

# Register a campaign
python main.py register-campaign --name "DevTool Launch" --budget 1000 --target-audience "Software developers" --niche "developer-tools"

# Register influencers
python main.py register-influencer --name "CodeWithJane" --niche "developer-tools" --followers 25000 --rate 300

# Find matches
python main.py match "DevTool Launch"
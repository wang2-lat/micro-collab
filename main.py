import typer
from rich.console import Console
from rich.table import Table
from models import Campaign, Influencer
from storage import Storage
from matcher import Matcher

app = typer.Typer(help="Connect SaaS companies with micro-influencers")
console = Console()
storage = Storage()
matcher = Matcher()


@app.command()
def register_campaign(
    name: str = typer.Option(..., help="Campaign name"),
    budget: float = typer.Option(..., help="Budget in USD"),
    target_audience: str = typer.Option(..., help="Target audience description"),
    niche: str = typer.Option(..., help="Product niche (e.g., productivity, design)")
):
    """Register a new SaaS company campaign"""
    campaign = Campaign(
        name=name,
        budget=budget,
        target_audience=target_audience,
        niche=niche
    )
    storage.save_campaign(campaign)
    console.print(f"[green]Campaign '{name}' registered successfully![/green]")


@app.command()
def register_influencer(
    name: str = typer.Option(..., help="Influencer name"),
    niche: str = typer.Option(..., help="Content niche"),
    followers: int = typer.Option(..., help="Follower count"),
    rate: float = typer.Option(..., help="Rate per post in USD")
):
    """Register a new micro-influencer profile"""
    influencer = Influencer(
        name=name,
        niche=niche,
        followers=followers,
        rate=rate
    )
    storage.save_influencer(influencer)
    console.print(f"[green]Influencer '{name}' registered successfully![/green]")


@app.command()
def match(campaign_name: str = typer.Argument(..., help="Campaign name to match")):
    """Find and recommend suitable influencers for a campaign"""
    campaign = storage.get_campaign(campaign_name)
    if not campaign:
        console.print(f"[red]Campaign '{campaign_name}' not found[/red]")
        raise typer.Exit(1)
    
    influencers = storage.get_all_influencers()
    matches = matcher.find_matches(campaign, influencers)
    
    if not matches:
        console.print("[yellow]No matching influencers found[/yellow]")
        return
    
    table = Table(title=f"Recommended Influencers for '{campaign_name}'")
    table.add_column("Name", style="cyan")
    table.add_column("Niche", style="magenta")
    table.add_column("Followers", style="green")
    table.add_column("Rate", style="yellow")
    table.add_column("Match Score", style="blue")
    
    for influencer, score in matches:
        table.add_row(
            influencer.name,
            influencer.niche,
            str(influencer.followers),
            f"${influencer.rate}",
            f"{score:.0%}"
        )
    
    console.print(table)


@app.command()
def list_campaigns():
    """List all registered campaigns"""
    campaigns = storage.get_all_campaigns()
    if not campaigns:
        console.print("[yellow]No campaigns registered yet[/yellow]")
        return
    
    table = Table(title="Registered Campaigns")
    table.add_column("Name", style="cyan")
    table.add_column("Budget", style="green")
    table.add_column("Niche", style="magenta")
    table.add_column("Target Audience", style="yellow")
    
    for campaign in campaigns:
        table.add_row(
            campaign.name,
            f"${campaign.budget}",
            campaign.niche,
            campaign.target_audience
        )
    
    console.print(table)


@app.command()
def list_influencers():
    """List all registered influencers"""
    influencers = storage.get_all_influencers()
    if not influencers:
        console.print("[yellow]No influencers registered yet[/yellow]")
        return
    
    table = Table(title="Registered Influencers")
    table.add_column("Name", style="cyan")
    table.add_column("Niche", style="magenta")
    table.add_column("Followers", style="green")
    table.add_column("Rate", style="yellow")
    
    for influencer in influencers:
        table.add_row(
            influencer.name,
            influencer.niche,
            str(influencer.followers),
            f"${influencer.rate}"
        )
    
    console.print(table)


if __name__ == "__main__":
    app()

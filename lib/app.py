#!/home/eugene/.local/share/virtualenvs/property-listings-qbpVMiNd/bin/ python

import click

from database.db import session
from model.models import Agent, ResidentialProperty, CommercialProperty

property_types = ['Apartment', 'Townhouse', 'Bungalow', 'Duplex', 'Condominium', 'Warehouse', 'Office']
residential_property_types = ['Apartment', 'Townhouse', 'Bungalow', 'Duplex', 'Condominium']

@click.group()
def cli():
    pass

@click.command()
@click.option('--first-name', prompt='Enter agent\'s first name', help='first name', required=True, type=str)
@click.option('--last-name', prompt='Enter agent\'s last name', help='last name', required=True, type=str)
@click.option('--email',prompt='Enter agent\'s email', help='agent email', required=True, type=str )
def add_agent(first_name, last_name, email):
    """Add a new property agent to the system"""
    agent = Agent(first_name = first_name, last_name = last_name, email = email)
    session.add(agent)
    session.commit()
    session.refresh(agent)
    
    click.echo('New Agent Added:')
    click.echo(agent)

@click.command()
def show_cities():
    """Show all cities that have a property listing"""
    for city in session.query(ResidentialProperty.city).distinct():
        click.echo(city[0])

@click.command()
def show_areas():
    """Show all areas that have a property listing"""
    for area in session.query(ResidentialProperty.area).distinct():
        click.echo(area[0])

@click.command()
def show_agents():
    """Show a list of all agents"""
    for agent in session.query(Agent).distinct():
        click.echo(agent)

@click.command()
@click.option('--type', type=click.Choice(property_types , case_sensitive=False), prompt='Enter a property type to search for: ', help='first name')
def show_all(type):
    """Show all the property listings"""
    click.secho(click.style(' All Properties '.upper(), blink=True, bold=True, bg='red', fg='white'))
    property = get_category(type)
    print(*session.query(property).filter(property.type == type), sep='\n\n')

@click.command()
@click.option('--type', type=click.Choice(property_types, case_sensitive=False), prompt='Enter a property type to search for: ', help='first name')
@click.option('--name', prompt='Enter the property name', help='first name')
def search_by_name(type, name):
    """Search for a listing using the property name"""
    click.secho(click.style(' All Properties '.upper(), blink=True, bold=True, bg='red', fg='white'))
    property = get_category(type)
    print(*session.query(property).filter(property.name.ilike(f'%{name}%')), sep='\n\n')

@click.command()
@click.option('--type', type=click.Choice(property_types, case_sensitive=False), prompt='Enter a property type to search for: ', help='first name')
@click.option('--id', type=int, prompt='Enter property id: ', required=True)
def search_by_id(type, id):
    """Search for a listing using the property id"""
    property = get_category(type)
    print(*session.query(property).filter(property.id == id), sep='\n\n')

@click.command()
@click.option('--type', type=click.Choice(property_types, case_sensitive=False), prompt='Enter a property type to search for: ', help='first name')
@click.option('--city-name', type=str, prompt='Enter city name: ', help='city name', required=True)
def search_by_city(type, city_name):
    """Search for all the property listings in a city"""
    property = get_category(type)
    print(*session.query(property).filter(property.city == city_name).filter(property.type == type), sep='\n\n')

@click.command()
@click.option('--type', type=click.Choice(property_types, case_sensitive=False), prompt='Enter a property type to search for: ', help='first name')
@click.option('--area-name', type=str, prompt='Enter area name: ', help='area name', required=True)
def search_by_area(type, area_name):
    """Search for all the property listings in an area"""
    property = get_category(type)
    print(*session.query(property).filter(property.area == area_name).filter(property.type == type), sep='\n\n')

@click.command()
@click.option('--id', type=int, required=True, prompt='Enter property agent id: ')
def show_listings_by_agent_id(id):
    """Show all the property listings using the agent's id"""
    agent = session.query(Agent).filter(Agent.id==id).first()
    print('Residential Properties', *agent.residential_properties, sep='\n\n')
    print('Commercial Properties',*agent.commercial_properties, sep='\n\n')

@click.command()
@click.option('--first-name', prompt='Enter agent\'s first name', help='first name', required=True, type=str)
@click.option('--last-name', prompt='Enter agent\'s last name', help='last name', required=True, type=str)
def show_listings_by_agent_name(first_name, last_name):
    """Show all the property listings using the agent name"""
    click.secho(click.style(f' All Commercial and Residential Properties Listed by {first_name} {last_name} '.upper(), blink=True, bold=True, bg='red', fg='white'))
    agents = agent = session.query(Agent).filter(Agent.first_name==first_name, Agent.last_name==last_name).all()
    if agent:
        for agent in agents:
            print('Residential Properties', *agent.residential_properties, sep='\n\n')
            print('Commercial Properties',*agent.commercial_properties, sep='\n\n')
    else:
        print('No agent found')

@click.command()
@click.option('--type', type=click.Choice(property_types, case_sensitive=False), prompt='Enter a property type to search for: ', help='first name', required=True)
@click.option('--agent-id', type=int, prompt='Enter agent id: ', required=True)
@click.option('--property-id', type=int, prompt='Enter property id: ', required=True)
def delete_listing(type, property_id, agent_id):
    """Remove property specified by property id, using your agent id"""
    property = get_category(type)
    found = session.query(property).filter(property.agent_id == agent_id).filter(property.id == property_id).first()
    if found:
        if click.confirm(f'Confirm, are you sure you want to delete "{found}"?'):
            session.delete(found)
            session.commit()
            click.echo('Property Deleted!')
    else:
        click.echo('No matching property found!')
            

def get_category(type):
    return ResidentialProperty if type in residential_property_types else CommercialProperty

cli.add_command(add_agent)
cli.add_command(show_cities)
cli.add_command(show_areas)
cli.add_command(show_agents)
cli.add_command(show_all)
cli.add_command(search_by_name)
cli.add_command(search_by_id)
cli.add_command(search_by_city)
cli.add_command(search_by_area)
cli.add_command(show_listings_by_agent_id)
cli.add_command(show_listings_by_agent_name)
cli.add_command(delete_listing)

if __name__ == '__main__':
    cli()
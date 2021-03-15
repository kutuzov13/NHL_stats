import requests


def get_all_teams():
    """Returns all teams NHL"""
    api_nhl = 'https://statsapi.web.nhl.com/api/v1/teams'
    response = requests.get(api_nhl).json()
    return response['teams']


def get_all_team_players(team_id):
    """Returns all team members by team ID."""
    api_nhl = f'https://statsapi.web.nhl.com/api/v1/teams/{team_id}/roster'
    response = requests.get(api_nhl).json()
    return response['roster']


def get_stats_team(team_id):
    """Returns a dict with statistics for the current season."""
    api_stats = f'https://statsapi.web.nhl.com/api/v1/teams/{team_id}'
    params = {'expand': 'team.stats'}
    response = requests.get(api_stats, params=params).json()
    return response['teams'][0]['teamStats'][0]['splits'][0]['stat']


def get_stats_player(player_id, season):
    """Returns stats player by its ID and season."""
    api_nhl = f'https://statsapi.web.nhl.com/api/v1/people/{player_id}/stats'
    params = {'stats': 'statsSingleSeason',
              'season': season  # Example 20202021
              }
    response = requests.get(api_nhl, params=params).json()
    return response['stats']



import requests


def get_all_teams():
    nhl_api = 'https://statsapi.web.nhl.com/api/v1/teams'
    response = requests.get(nhl_api).json()
    for team in response['teams']:
        print(team['id'], team['name'], team['link'], team['division'], team['franchise'])


def get_stats_team(team_id):
    """Returns a dict with statistics for the current season"""
    api_stats = f'https://statsapi.web.nhl.com/api/v1/teams/{team_id}'
    params = {'expand': 'team.stats'}
    response = requests.get(api_stats, params=params).json()
    return response['teams'][0]['teamStats'][0]['splits'][0]['stat']


print(get_stats_team(5))
# Russia2018

## Installation

1. Configure your virtualenv and access it
2. `pip install -r requirements.txt`
3. Make sure you have an empty database named 'russia2018' on localhost, with root-root as credentials:
    ```
    mysql -uroot -proot
    create database russia2018;
    ```
    * Or change the settings in Russia2018/settings.py DATABASES to match a new DB
4. `python manage.py migrate`
5. Run the server (configure it in PyCharm)

## API


### /api/teams

Methods: GET, POST

*POST Example*

```
{
    "country": "Uruguay"
}
```
Returns match_id

### /api/players

Methods: GET, POST

*POST Example*

```
{
    "name": "Suarez",
    "position": "striker-goalkeeper",
    "number": 9,
    "team": 1
}
```
Returns player_id
(team id must exist)

### /api/matches

Methods: GET, POST

*POST Example*

```
{
    "team1": 1,
    "team2": 2,
    "score1": 1,
    "score2": 0
}
```
Returns match_id
(all team ids must exist)
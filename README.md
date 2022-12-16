# Runescape 3 API Wrapper

## Under construction


## Hiscores

```python
from rs3_api.hiscores.hiscore import Hiscore

hiscore = Hiscore()

## User hiscores
user = h.user('zezima')
print(user)
print(user.account_type)
print(user.skills)
print(user.minigames)

archived_seasonal_events = user.get_season(archived=True)
print(archived_seasonal_events)

## Seasonal events
print(h.seasonal_events.all)
print(h.seasonal_events.current)

## Clan Hiscores
clan = h.clan('atlantis')
print(clan.members)
print(clan.get_member('oieeusougoku'))

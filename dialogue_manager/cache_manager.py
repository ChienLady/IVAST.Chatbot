from typing import Union, Dict, Any, List
from cachetools import TTLCache
from datetime import datetime, timedelta

CACHE = TTLCache(maxsize=50, ttl=timedelta(hours=12), timer=datetime.now)

def cache_check(cache_id: str):
    return True if cache_id in CACHE else False

def cache_init(cache_id: str) -> None:
    CACHE[cache_id] = {
        'intent_history': [],
        'quests_history': [],
        'answers_history': [],
        'entities': {}
    }

def cache_get(cache_id: str,
              type: List[str]):
    valid = ['intent_history', 'quests_history', 'answers_history', 'entities', 'session']
    if not any([t in type for t in valid]):
        raise f'Accepted type in {valid}'
    response = {}
    [response.update({k: CACHE[cache_id][k]}) for k in type if k in valid]
    return tuple(response.values())

def cache_append(cache_id: str,
                 intent: Union[str, None] = None,
                 quest: Union[str, None] = None,
                 answer: Union[str, None] = None,
                 entity: Dict[str, Any] = {},
                 session: str = '') -> None:
    if not cache_check(cache_id):
        cache_init(cache_id)
    if not intent is None:
        CACHE[cache_id]['intent_history'].append(intent)
    if not quest is None:
        CACHE[cache_id]['quests_history'].append(intent)
    if not answer is None:
        CACHE[cache_id]['answers_history'].append(intent)
    if not entity == {}:
        TEMP = CACHE[cache_id]['entities'].copy()
        for ent_name, ent_value in TEMP.items():
            CACHE[cache_id]['entities'][ent_name] = ent_value
    if not session == '':
        CACHE[cache_id]['session'] = session
            
def cache_delete(cache_id: str) -> None:
    if cache_check(cache_id):
        _ = CACHE.pop(cache_id)


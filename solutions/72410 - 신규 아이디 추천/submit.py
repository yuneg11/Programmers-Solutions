from re import sub

def solution(new_id):
    new_id = new_id.lower()
    new_id = sub("[^a-z0-9-_.]", "", new_id)
    new_id = sub("\.+", ".", new_id)
    new_id = sub("(^\.|\.$)", "", new_id)
    new_id = new_id or "a"
    new_id = sub("\.$", "", new_id[:15])
    new_id = new_id if len(new_id) > 3 else new_id + new_id[-1] * (3 - len(new_id))
    return new_id

from datetime import datetime
from hashlib import sha1


def make_key(*a):
    parts = []
    for part in a:
        if isinstance(part, datetime):
            part = part.isoformat()
        elif part is None:
            part = '**'
        else:
            part = str(part)
        parts.append(part)
    return sha1('||'.join(parts).encode()).hexdigest()


def flatten(d, sep='_'):
    out = {}
    for k, v in list(d.items()):
        if isinstance(v, dict):
            for ik, iv in list(flatten(v, sep=sep).items()):
                out[k + sep + ik] = iv
        else:
            out[k] = v
    return out

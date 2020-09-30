import pytest
import collections
import sys
INDEX='index.txt'
Entry=collections.namedtuple('indexEntry', 'checksum url')

class UniquenessError(ValueError): pass
class TooMany(UniquenessError): pass
class TooFew(UniquenessError): pass
def _unique(_list):
    if len(_list) < 1:
        raise TooFew( 'unique() received an list of length < 1')
    if len(_list) > 1:
        raise TooMany( 'unique() received an list of length > 1')
    return _list[0]

def _item_4_line(line):
    line = line.strip()
    item = line.split()
    if not line: return None
    if '#' in line: return None
    if not len(item)==2: return None
    return Entry(*item)

def _item_gen_4_path(path):
    with open(path) as fd:
        items = map(_item_4_line,fd)
        items = filter(None, items)
        yield from items

def matches(checksum):
    items = list(_item_gen_4_path(INDEX))
    matches = [item for item in items if item.checksum.startswith(checksum)]
    return matches

def match(checksum):
    return _unique(matches(checksum))

def test_too_many(regtest):
    with pytest.raises(TooMany):
        match('3e')
def test_too_few(regtest):
    with pytest.raises(TooFew):
        match('X')
def test_sanity(regtest):
    print(matches('3e7'))

import typing as t


class HashTable:
    def __init__(self, size: int):
        self._data = [None] * size

    def _hash(self, key: str):
        hsh = 0
        for i, k in enumerate(key):
            hsh = (hsh + ord(k) * i) % len(self._data)
        return hsh

    def __str__(self):
        return str(self._data)

    def len(self):
        return len(self._data)

    def set(self, key: str, val: t.Any):
        address = self._hash(key)
        if not self._data[address]:
            self._data[address] = []
            self._data[address].append([key, val])
            return

        for idx, i in enumerate(self._data[address]):
            if i[0] == key:
                self._data[address][idx][1] = val
                return

        self._data[address].append([key, val])
        return

    def get(self, key: str) -> t.Any:
        data = self._data[self._hash(key)]
        if data:
            for d in data:
                if d[0] == key:
                    return key
        raise KeyError(f"key {key} not found in map")

    def keys(self) -> t.Iterable:
        for d in self._data:
            if d:
                for k in d:
                    yield k[0]

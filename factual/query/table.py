"""
Factual table api query
"""

from base import Base

DEFAULT_LIMIT = 20

class Table(Base):
    def __init__(self, api, path, params={}):
        self.path = path
        Base.__init__(self, api, params)

    def search(self, terms):
        return self._copy({'q': terms})

    def filters(self, filters):
        return self._copy({'filters': filters})

    def include_count(self, include):
        return self._copy({'include_count': include})

    def geo(self, geo_filter):
        return self._copy({'geo': geo_filter})

    def limit(self, max_rows):
        return self._copy({'limit': max_rows})

    def select(self, fields):
        return self._copy({'select': fields})

    def sort(self, sort_params):
        return self._copy({'sort': sort_params})

    def offset(self, offset):
        return self._copy({'offset': offset})

    def page(self, page_num, limit=DEFAULT_LIMIT):
        limit = DEFAULT_LIMIT if limit < 1 else limit
        page_num = 1 if page_num < 1 else page_num
        return self.offset((page_num - 1) * limit).limit(limit)

    def sort_asc(self, fields):
        return self.sort(",".join([f + ":asc" for f in fields]))

    def sort_desc(self, fields):
        return self.sort(",".join([f + ":desc" for f in fields]))

    def _copy(self, params):
        return Table(self.api, self.path, self.merge_params(params))

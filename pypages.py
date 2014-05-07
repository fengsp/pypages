# -*- coding: utf-8 -*-
"""
    pypages
    ~~~~~~~

    A module that brings easier pagination.  Mainly useful for web
    applications.

    :copyright: (c) 2014 by Shipeng Feng.
    :license: BSD, see LICENSE for more details.
"""

import math


class Paginator(object):
    """Paginator.

    Basic usage::

        p = Paginator(100)
        p.object_num
        p.per_page
        p.current
        p.start
        p.range_num
        p.end
        p.page_num
        p.pages
        p.has_previous
        p.has_next
        p.previous
        p.next

    :param object_num: The total number of items.
    :param per_page: The maximum number of items to include on a page,
                     default 10
    :param current: The current page number, default 1
    :param start: The start index for your page range, default to be current
                  page minus half of the page range length.
    :param range_num: The maximum page range length, default 10
    """
    
    def __init__(self, object_num, per_page=10, current=1, start=None,
                       range_num=10):
        self._start = self._end = self._current = self._page_num = None
        self.object_num = int(object_num)
        self.per_page = int(per_page)
        self.current = current
        self.range_num = int(range_num)
        assert self.object_num >= 0, "object_num must be positive or 0"
        assert self.per_page > 0, "per_page must be positive"
        assert self.range_num > 0, "range_num must be positive"
        self.start = start

    def _get_current(self):
        """Returns the current page.
        """
        return self._current

    def _set_current(self, current):
        """Set the current page that does make sense.  Any invalid value
        passed in will be regarded as 1.
        """
        try:
            current = int(current)
        except:
            current = 1

        if current < 1:
            current = 1
        elif current > self.page_num:
            current = self.page_num

        self._current = current

    current = property(_get_current, _set_current)
    del _get_current, _set_current

    def _get_start(self):
        """Returns the start index.
        """
        return self._start

    def _set_start(self, start):
        """Set the start index that does make sense.
        """
        if not start:
            start = self.current - self.range_num / 2
        self._start = int(start) if int(start) > 0 else 1

    start = property(_get_start, _set_start)
    del _get_start, _set_start

    @property
    def end(self):
        """Returns the end index.
        """
        if self._end is None:
            self._end = min(self.page_num, self.start + self.range_num - 1)
        return self._end

    @property
    def page_num(self):
        """Returns the total number of pages.
        """
        if self._page_num is None:
            self._page_num = int(math.ceil(self.object_num / 
                                           float(self.per_page)))
        return self._page_num
    
    @property
    def has_previous(self):
        return self.current > 1

    @property
    def has_next(self):
        return self.current < self.page_num

    @property
    def previous(self):
        """Returns the previous page number.
        """
        if self.has_previous:
            return self.current - 1

    @property
    def next(self):
        """Returns the next page number.
        """
        if self.has_next:
            return self.current + 1

    @property
    def pages(self):
        """Returns a 1-based range of pages for loop.
        """
        return range(self.start, self.end + 1)

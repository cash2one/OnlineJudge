# -*- coding: utf-8 -*-

from __future__ import unicode_literals


from .user import *  # noqa
from .problem import *  # noqa
from .solution import *  # noqa
from . import listeners  # noqa


from oj import db
db.configure_mappers()

from .hook import HookCenter

center = HookCenter()
center.register_events()

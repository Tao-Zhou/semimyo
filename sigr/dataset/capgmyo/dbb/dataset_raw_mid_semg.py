from __future__ import division
import os
from logbook import Logger
from ..base import BaseDataset, RawMidMixin
from .... import CACHE


logger = Logger(__name__)


class Dataset(RawMidMixin, BaseDataset):

    root = os.path.join(CACHE, 'dbb')
    subjects = list(range(2, 21, 2))
    gestures = list(range(1, 9))
    num_session = 2
    sessions = [1, 2]

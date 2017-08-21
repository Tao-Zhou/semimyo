from __future__ import division
import os
from .. import base
from .... import CACHE


class Dataset(base.SemiDownsampleMixin, base.PrevSemiDataset):

    root = os.path.join(CACHE, 'dbb')
    subjects = list(range(2, 21, 2))
    gestures = list(range(1, 9))

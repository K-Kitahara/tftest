# -*- coding: utf-8 -*-
from __future__ import division, print_function, absolute_import

import numpy as np
import tensorflow as tf

from ae import TFAutoEncoder

class StackedDenoisingAutoEncoder:
    """stacked denoising auto-encoder"""

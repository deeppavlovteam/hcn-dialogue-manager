"""
Copyright 2017 Neural Networks and Deep Learning lab, MIPT

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import unicodedata
import numpy as np


# ------------------------------------------------------------------------------
# Data/model utilities.
# ------------------------------------------------------------------------------


def normalize_text(text):
    return unicodedata.normalize('NFD', text)


def filter_service_words(tokens):
    return filter(lambda t: '_' not in t, tokens)


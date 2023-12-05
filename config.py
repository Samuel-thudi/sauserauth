#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "08002aa5-1e1b-434d-8386-f27502d24788")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "sph8Q~l3CNBE7_yaThOprC2B~ygcH2dWkXK_XaX2")
    CONNECTION_NAME = os.environ.get("ConnectionName", "user-authentication")

#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "78197bf0-f9d8-4fea-a270-c2c7e728f3e8")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "MAk8Q~XDthrZLqp-eFcR8KzBrMcuKS.Ni32uXduK")
    CONNECTION_NAME = os.environ.get("ConnectionName", "authentication-conn")

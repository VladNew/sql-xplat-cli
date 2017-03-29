# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import sys
import os

import mssql.scripter.main

try:
    # TODO: Start telemetry here
    args = sys.argsv[1:]
    exit_code = mssql.scripter.main.main(args)

    # TODO: Log telemetry based on exit code
    sys.exit(exit_code)
except KeyboardInterrupt:
    sys.exit(1)

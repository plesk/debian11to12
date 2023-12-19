#!/usr/bin/python3
# Copyright 1999-2023. Plesk International GmbH. All rights reserved.

import sys

import pleskdistup.main
import pleskdistup.registry

import debian11to12.upgrader

if __name__ == "__main__":
    pleskdistup.registry.register_upgrader(debian11to12.upgrader.Debian11to12Factory())
    sys.exit(pleskdistup.main.main())

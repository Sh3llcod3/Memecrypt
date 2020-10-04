#!/usr/bin/env python3
# -*- coding: utf-8 -*-

try:
    from .memecrypt import *
    main()

except(ImportError, SystemError):
    import memecrypt
    memecrypt.main()

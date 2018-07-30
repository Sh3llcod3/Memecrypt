#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#    __main__.py - Run memecrypt from pip
#    Copyright (C) 2018 Yudhajit N.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#    Please note: this program isn't meant to be taken or used seriously,
#    despite of how functional it may or may not be.
#
try:
    from .memecrypt import *
    main()
except(ImportError, SystemError):
    import memecrypt
    memecrypt.main()

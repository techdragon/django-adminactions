# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
import codecs
import sys
import six
import xlsxwriter

if sys.version[0] == '3':
    import io
    out = io.BytesIO()
elif sys.version[0] == '2':
    import io
    out = six.StringIO()

sheet_name = six.u('Sheet1')

book = xlsxwriter.Workbook(out)
sheet = book.add_worksheet(sheet_name)

book.close()

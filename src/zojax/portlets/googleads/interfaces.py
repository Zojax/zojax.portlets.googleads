##############################################################################
#
# Copyright (c) 2009 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
""" google ads portlet interfaces

$Id$
"""
from zope import schema, interface
from zope.i18nmessageid import MessageFactory

_ = MessageFactory('zojax.portlets')


class IGoogleAdsPortlet(interface.Interface):
    """ portlet interface """

    source = schema.SourceText(
        title = _(u'Google Ads'),
        description = _(u'Google ads javascript string.'),
        default = u'',
        required = True)

    decoration = schema.Bool(
        title = _('Decoration'),
        description = _('Show portlet decoration (title, border, etc)'),
        default = True,
        required = False)

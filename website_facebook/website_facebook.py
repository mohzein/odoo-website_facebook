# -*- coding: utf-8 -*-
##############################################################################
#
# OpenERP, Open Source Management Solution, third party addon
# Copyright (C) 2004-2015 Vertel AB (<http://vertel.se>).
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import models, fields, api, _
from openerp.exceptions import except_orm, Warning, RedirectWarning
from openerp import http
from openerp.http import request
from openerp import SUPERUSER_ID
import openerp.tools
import werkzeug
import facebook


class website_facebook(http.Controller):      
    @http.route(['/fb'], type='http', auth="public", website=True)
    def facebook_header(self, user=False, **post):
        cr, uid, context, pool = request.cr, request.uid, request.context, request.registry
           
        ctx = {
            'user' : user,
            }
        return request.render('website_facebook.fb_page', ctx)   
        
    @http.route(['/fb/about'], type='http', auth="public", website=True)
    def facebook_about(self, user=False, **post):
        cr, uid, context, pool = request.cr, request.uid, request.context, request.registry
           
        ctx = {
            'user' : user,
            }
        return request.render('website_facebook.about', ctx)  
    
        

# -*- coding: utf-8 -*-

from odoo import fields, models, api
from odoo.exceptions import ValidationError, UserError

import logging
_logger = logging.getLogger(__name__)


class colpariContractPartner(models.Model):
    _inherit = 'res.partner'

    directories_count = fields.Integer(compute="_compute_directories_count")

    def _compute_directories_count(self):
        for record in self:
            record.directories_count = self.env['dms.directory'].sudo().search_count([['partner_id', '=', record.id]])


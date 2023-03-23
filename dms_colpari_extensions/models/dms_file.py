# Copyright 2023 colpari GmbH.

import logging

from odoo import _, api, fields, models, tools

_logger = logging.getLogger(__name__)


class colpariFile(models.Model):
    _inherit = "dms.file"

    partner_id = fields.Many2one(
        'res.partner',
        string       = "Partner/Client",
        compute      ='_computePartnerId',
        compute_sudo = True,
        store        = True,
        readonly     = False,
        # would be nice but requires a dependency to colpari_services
        #domain       = "['|', ('is_colpari_client', '=', True), ('is_colpari_partner', '=', True)]"
    )
    @api.depends('directory_id')
    def _computePartnerId(self):
        for record in self:
            parentPartner = record.directory_id.partner_id
            _logger.info("{}._computePartnerId() current={}, parent={}".format(record, record.partner_id, parentPartner))
            if parentPartner:
                record.partner_id = parentPartner
            else:
                record.partner_id = record.partner_id

    @api.onchange("directory_id")
    def _changeDirectory(self):
        _logger.info("{}._changeDirectory() current={}, parent={}".format(self, self.partner_id, self.directory_id.partner_id))

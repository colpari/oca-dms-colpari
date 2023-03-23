# Copyright 2023 colpari GmbH.

import logging

from odoo import _, api, fields, models, tools

_logger = logging.getLogger(__name__)

class colpariDmsDirectory(models.Model):
    _inherit = "dms.directory"

    partner_id = fields.Many2one('res.partner', compute='_computePartnerId', inverse='_digestPartnerId', store='True', readonly=False)
    @api.depends('parent_id')
    def _computePartnerId(self):
        for record in self:
            parentPartner = record.parent_id.partner_id
            if parentPartner:
                record.partner_id = parentPartner
            else:
                record.partner_id = record.partner_id

    @api.onchange("parent_id")
    def _changeParent(self):
        _logger.info("{}._changeParent() current={}, parent={}".format(self, self.partner_id, self.parent_id.partner_id))

    @api.onchange("partner_id")
    def _changePartner(self):
        _logger.info("{}._changePartner() current={}, parent={}".format(self, self.partner_id, self.parent_id.partner_id))

    def _digestPartnerId(self):
        for record in self:
            _logger.info("{}._digestPartnerId() new={}".format(record, record.partner_id))
            for subDir in record.child_directory_ids:
                _logger.info("{}._changePartner() changing subDir={} from {} to {}".format(record, subDir, subDir.partner_id, record.partner_id))
                subDir.partner_id = record.partner_id
            for subFile in record.file_ids:
                _logger.info("{}._changePartner() changing subFile={} from {} to {}".format(record, subFile, subFile.partner_id, record.partner_id))
                subFile.partner_id = record.partner_id

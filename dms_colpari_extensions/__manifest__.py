# Copyright 2017-2019 MuK IT GmbH
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    "name": "DMS colpari extensions",
    "summary": """colpari extensions to the Document Management System for Odoo""",
    "version": "15.0.1.7.0",
    "category": "Document Management",
    "license": "LGPL-3",
    "website": "https://github.com/colpari/oca-dms-colpari",
    "author": "colpari GmbH",
    "depends": [ "dms" ],
    "data": [
        #"actions/file.xml",
        "views/dms_file.xml",
        "views/directory.xml",
    ],
    "application": False,
}

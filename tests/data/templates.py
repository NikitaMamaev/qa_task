"""
Templates data for tests
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Template:
    """
    Template parameters
    """

    tmpl_id: Optional[str] = None
    tmpl_data: Optional[list] = None
    filename: Optional[str] = None


empty = Template()

google = Template(
    tmpl_id="google",
    tmpl_data=[{
        'id':'google',
        'label':'google.com',
        'link':'https://google.com/'
    }],
    filename="google_template.yaml"
)

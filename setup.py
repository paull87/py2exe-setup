from distutils.core import setup
import py2exe

class Target:
    def __init__(self, **kw):
        self.__dict__.update(kw)
        # for the version info resources (Properties -- Version)
        self.version = "1.0"
        self.company_name = "Paul Lucas"
        self.copyright = "© 2016, Paul Lucas"
        self.product_name = "SSIS Deployment Check"
        self.author = "Paul Lucas"

console_exe = Target(
    description = "Checks the deployed solution against the local version",
    script = 'DeployCheck.py',
    icon_resources= [(1,'compare.ico')])

setup(
    name = 'Deploy Check',
    description = 'Checks the deployed solution against the local version',
    console=[console_exe],#[{'script':'DeployCheck.py'}],
    zipfile = None,
    #windows=['URLshortener.py'],
    options = {
        "py2exe":{
        "bundle_files": 1,
        "compressed":True,
            "includes":
                ["decimal",
                "lxml.etree",
                "collections.abc",
                "lxml._elementpath"
                ]
            }
        }
    #options = {"py2exe":{"includes":["requests","queue","pyperclip"]}}
    )

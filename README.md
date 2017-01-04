# py2exe-setup

This is the setup script that is run for py2exe to create an executable that can be run on machines without a Python IDE.

# Contents

## Target Class
This class contains the file property details that will be used when the exe is created. It contains the following items -
* Version
* Company Name
* Copyright
* Product Name
* Author

The class also takes key word arguments for the description, script and icon_resources. The script will be the main python script to create the .exe against.

NOTE: Icon resources are limited by what py2exe is able to handle. You can get icons from http://www.iconarchive.com/.

## Setup
This is the main setup that py2exe will use to create the .exe. It contains the following
* Console/Windows - decides whether the executable will be a window or console application.
* Zipfile - The name of the zip for the relevant files required by the executable. Setting this to None means the files are built into the .exe.
* Options - We set ```bundle_files = 1``` and ```compressed = True``` so that the .exe is created as a single file with no dependancies. We also include the methods that are required.

# Running
To create the .exe this setup needs to be saved in the python working directory and the following run in the command line.

```cmd
Python setup.py py2exe
```

The .exe will be saved in the dist folder of the python IDE.

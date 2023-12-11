---
weight: 100
date: "2023-12-11T15:04:38+01:00"
draft: false
author: "Andres Mendez"
title: "Custom Delete"
icon: "code"
toc: true
description: "Small Command Line Utility to delete files and folders"
publishdate: "2023-12-11T15:04:38+01:00"
tags: ["python","delete","files","filetype"]
---
## Libraries used
    
* **os**
* **argparse**
* **shutil**

## Parameters

{{< table "table-hover" >}}
| Parameter Name | Abbreviation | Type | Description
|--------------|------|-----------|-------------------------------|
|**ROOT_PATH** | None |  positional | Root directory in which we want to delete things
| `--file-type` | `-f` | keyword [optional] | String chain indicating the type of files inside the **root_path** to be deleted
| `--dirs` | `-d` | keyword [optional] | String chain indigating the folder name of directories inside the **root path** to be deleted
{{< /table >}}

## Usage

To delete all '.md' files inside a project folder:

```bash
python3 custom_delete.py /home/username/project -f .md
```

To delete all folders named '.mayaSwatches' inside a project folder

```bash
python3 custom_delete.py /home/username/project -d .mayaSwatches
```

[Source File](https://github.com/Amenrio/my-docs/content/scripts/python/custom_delete.py/) 
```python
#!/usr/bin/env python# -*- coding: utf-8 -*-
# Copyright (C) 2023 Antaruxa S.L - All Rights Reserved
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential
# Written by Andres Mendez <andres.mendez@antaruxa.com>, 2023

import os
import argparse
import shutil

def run(file_path, file_type, dir_name):
    for root, dirs, files in os.walk(file_path):
        if file_type:
            for file in files:
                if file.endswith(file_type):
                    print(f"Removing {file}")
                    os.remove(os.path.join(root,file))
        if dir_name:
            for dir in dirs:
                if dir == dir_name:
                    print(f"Removing {dir}")
                    shutil.rmtree(os.path.join(root,dir))

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('root_path')
    parser.add_argument('-f', '--fileType',type=str)
    parser.add_argument("-d","--dirs",type=str)
    args = parser.parse_args()

    run(args.root_path, args.fileType,args.dirs)
```
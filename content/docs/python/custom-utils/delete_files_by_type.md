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

[Raw File](https://raw.githubusercontent.com/Amenrio/docs/main/content/scripts/python/custom_delete.py) 
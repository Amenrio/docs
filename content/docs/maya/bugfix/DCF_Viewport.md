---
weight: 999
title: "BugFix - DCF Update Viewport List"
description: "Solution to DCF_UpdateViewportList bug"
icon: "bug_report"
date: "2023-12-11T15:44:35+01:00"
lastmod: "2023-12-11T15:44:35+01:00"
draft: false
toc: true
tags: ["bug","maya","dcf_updateviewportlist"]
--- 

### Error:

When opening the scene, or every *n* second, a error message window opens with the title ***DCF_UpdateViewportList;***

### Cause:

Some preferences of **ngSkinTools** scripts get stored inside your version folder. I moved the scripts to another folder where they wouldn't automatically be loaded and deleted the whole maya version folder. 

In the end, the file has a residual script_node instruction called ***DCF_UpdateViewportList;***, which needs to be manually deleted from the scene file (always saved in .ma)

### Solucion:

Run a little script that searches the scene and deletes the script_node

```python
import maya.cmds as mc
import re

def cleanup_uiconfig():
    for script_node in mc.ls(type='script'):
        bs = mc.scriptNode(script_node, q=True, bs=True)
        if bs:
            bs = re.sub(r'DCF_updateViewportList;', '', bs)
            mc.scriptNode(script_node, e=True, bs=bs)
            mc.scriptNode(script_node, eb=True)

cleanup_uiconfig()
```

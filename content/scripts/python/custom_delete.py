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
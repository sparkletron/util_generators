#!/usr/bin/python3
from fusesoc.capi2.generator import Generator
import os
import yaml
import subprocess
import pathlib

################################################################################
## vpilibmake
# @file   vpilibmake.py
# @author Jay Convertino(johnathan.convertino.1@us.af.mil)
# @date   23.01.01
# @brief  build libraries using make.
#
# @license MIT
# Copyright 2023 Jay Convertino
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to 
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or 
# sell copies of the Software, and to permit persons to whom the Software is 
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in 
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING 
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
################################################################################
class vpilibmake(Generator):
    def run(self):
      #get dirrrs
      src_dir   = self.config.get('src_dir')
      make_args = self.config.get('make_args')
      
      log = open(self.files_root  + '/' + pathlib.Path(src_dir).name + "_build.log", "w")

      try:
        subprocess.run(["make", make_args], stdout=log, stderr=log, cwd=self.files_root + '/' + src_dir)
      except subprocess.CalledProcessError as error_code:
        print("Make error:", error_code.returncode, error_code.output)
        exit(1)

      log.close()
      
g = vpilibmake()
g.run()
g.write()

#!/usr/bin/python3
from fusesoc.capi2.generator import Generator
import os
import yaml
import subprocess

################################################################################
## vpilibcmake
# @file   vpilibcmake.py
# @author Jay Convertino(johnathan.convertino.1@us.af.mil)
# @date   23.01.01
# @brief  Build libraries using cmake for vpi libraries.
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
class vpilibcmake(Generator):
    def run(self):
      #get dirrrs
      src_dir   = self.config.get('src_dir')
      build_dir = self.config.get('build_dir', 'build')
      cmake_args= self.config.get('cmake_args')

      cmake_cmake_args = ["cmake", "../"] + cmake_args

      log = open(self.files_root  + '/' + pathlib.Path(src_dir).name + "_build.log", "w")

      if not os.path.exists(self.files_root + '/' + src_dir + '/' + build_dir):
        os.makedirs(self.files_root + '/' + src_dir + '/' + build_dir)

      try:
        subprocess.run([cmake_cmake_args], stdout=log, stderr=log, cwd=self.files_root + '/' + src_dir + '/' + build_dir)
      except subprocess.CalledProcessError as error_code:
        print("cmake error:", error_code.returncode, error_code.output)
        exit(1)

      try:
        subprocess.run(["make"], stdout=log, stderr=log, cwd=self.files_root + '/' + src_dir + '/' + build_dir)
      except subprocess.CalledProcessError as error_code:
        print("make error:", error_code.returncode, error_code.output)
        exit(1)

      log.close()
      
g = vpilibcmake()
g.run()
g.write()

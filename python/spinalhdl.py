#!/usr/bin/python3
from fusesoc.capi2.generator import Generator
import os
import yaml
import subprocess
import pathlib
import shutil
import urllib.request
import zipfile
import tarfile

################################################################################
# @file   spinalhdl.py
# @author Jay Convertino(johnathan.convertino.1@us.af.mil)
# @date   24.01.24
# @brief  build libraries using make.
#
# @license MIT
# Copyright 2024 Jay Convertino
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
class spinalhdl(Generator):
    def run(self):
      #get dirrrs
      src_dir           = self.config.get('src_dir')
      build_args        = self.config.get('build_args')
      sbt_archive_url   = self.config.get('sbt_tgz_archive_url')

      command = [self.files_root + "/tools/sbt/bin/sbt", "sbt"]

      if sbt_archive_url is not None:
        command = [command[0]]

      path = None

      for cmd in command:
        path = shutil.which(cmd)

        command = [cmd]

        if path is not None:
          print("INFO: Command, " + cmd + " found.")
          break


      #if none, download tar, extract, and change path to it.
      if path is None:
        if sbt_archive_url is None:
          print("ERROR: Command sbt not found, no url to download archives for install")
          exit(1)

        print("INFO: Command sbt not found, downloading archives and installing locally")

        if os.path.isdir(self.files_root + "/archives"):
          shutil.rmtree(self.files_root + "/archives")

        if os.path.isdir(self.files_root + "/tools"):
          shutil.rmtree(self.files_root + "/tools")

        os.makedirs(self.files_root + "/archives", exist_ok=True)
        os.makedirs(self.files_root + "/archives/sbt/", exist_ok=True)

        urllib.request.urlretrieve(sbt_archive_url, self.files_root + "/archives/sbt/sbt.tar.gz")

        with tarfile.open(self.files_root + "/archives/sbt/sbt.tar.gz","r") as tar_archive:
          tar_archive.extractall(self.files_root + "/tools/")

        # os.makedirs(self.files_root + "/archives/jre/")
        #
        # urllib.request.urlretrieve(java_archive_url, self.files_root + "/archives/jre/jre.tar.gz")
        #
        # with tarfile.open(self.files_root + "/archives/jre/jre.tar.gz","r") as tar_archive:
        #   tar_archive.extractall(self.files_root + "/tools/")
        #
        # jre_folder = [i for i in (next(os.walk(self.files_root + "/tools/"))[1]) if i.startswith('jdk')]
        #
        # os.rename(self.files_root + "/tools/" + jre_folder[0], self.files_root + "/tools/jre")


      command_with_args = command + [" ".join(build_args)]

      log = open(self.files_root  + '/' + pathlib.Path(src_dir).name + "_gen.log", "w")

      log.write("COMMAND: " + " ".join(command_with_args) + "\n")

      log.flush()

      try:
        subprocess.check_call(command_with_args, universal_newlines=True, stdout=log, stderr=log, cwd=self.files_root + '/' + src_dir)
      except subprocess.CalledProcessError as error_code:
        print("ERROR: ", error_code.returncode)
        print("ERROR: TIP JAVA JRE 17 REQUIRED. Set JAVA_HOME to the correct path, if local jre install will be used.")
        exit(1)

      log.close()
      
g = spinalhdl()
g.run()
g.write()

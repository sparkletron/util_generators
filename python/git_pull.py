#!/usr/bin/python3
from fusesoc.capi2.generator import Generator
import os
import yaml
import subprocess
import git
import shutil

################################################################################
## git_pull
# @file   git_pull.py
# @author Jay Convertino(johnathan.convertino.1@us.af.mil)
# @date   23.02.28
# @brief  pull git repos
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
class git_pull(Generator):
    def run(self):
      #get dirrrs
      repo_url = self.config.get('repo_url')
      tag      = self.config.get('tag')
      repo_dir = self.config.get('repo_dir')
      
      shutil.rmtree(self.files_root + '/' + repo_dir[0], ignore_errors=True)
      
      try:
        repo_data = git.Repo.clone_from(repo_url[0], self.files_root + '/' + repo_dir[0])
      except Exception as e: 
        print(e)
        exit(1)
        
      try:
        if len(tag) > 0:
          repo_data.git.checkout(tag[0])
      except Exception as e: 
        print(e)
        exit(1)
        
g = git_pull()
g.run()
g.write()

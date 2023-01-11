#!/usr/bin/python3
from fusesoc.capi2.generator import Generator
import os
import yaml
import subprocess

class vpilibgen(Generator):
    def run(self):
      #get dirrrs
      src_dirs   = self.config.get('src_dirs')
      
      for dir_idx in src_dirs:
        subprocess.run(["make"], cwd=self.files_root + '/' + dir_idx)
      
g = vpilibgen()
g.run()
g.write()

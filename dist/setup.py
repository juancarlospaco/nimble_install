import setuptools, subprocess
from setuptools.command.install import install

class InstallCommand(install):
  user_options = install.user_options + [('nimble=', None, "Install Nimble Packages from PIP")]
  nimble = ""

  def finalize_options(self):
    print(subprocess.run("nimble --accept --noColor install " + self.nimble.replace(",", " "), shell=True, check=True))
    install.finalize_options(self)

setuptools.setup(cmdclass = {"install": InstallCommand})

# noqa: INP001
import os
import shutil
import subprocess
from sys import stderr

from hatchling.builders.hooks.plugin.interface import BuildHookInterface


class CustomBuildHook(BuildHookInterface):
    def initialize(self, version, build_data):
        super().initialize(version, build_data)
<<<<<<< HEAD
        stderr.write(">>> Building Version prueba frontend\n")
        npm = shutil.which("npm")
        if npm is None:
            raise RuntimeError(
                "NodeJS `npm` is required for building Version prueba but it was not found"
=======
        stderr.write(">>> Building Version de prueba frontend\n")
        npm = shutil.which("npm")
        if npm is None:
            raise RuntimeError(
                "NodeJS `npm` is required for building Version de prueba but it was not found"
>>>>>>> 1bfc1be0c8a242212d2b3944ec9970f3c9acab24
            )
        stderr.write("### npm install\n")
        subprocess.run([npm, "install"], check=True)  # noqa: S603
        stderr.write("\n### npm run build\n")
        os.environ["APP_BUILD_HASH"] = version
        subprocess.run([npm, "run", "build"], check=True)  # noqa: S603

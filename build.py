from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")

name = "BaseApiService"
default_task = "publish"

@init
def set_properties(project):
    project.build_depends_on("pytest")

    project.set_property("dir_source_main_python", "src/main/python")
    project.set_property("dir_source_unittest_python", "tests/python")
    project.set_property("dir_target", "target")
    project.set_property("unittest_module_glob", "*_test")
    project.set_property("run_unit_tests_propagate_stdout", True)

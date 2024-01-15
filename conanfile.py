from conan import ConanFile
from conan.errors import ConanInvalidConfiguration
from conan.tools.build import check_min_cppstd
from conan.tools.cmake import CMake, CMakeDeps, CMakeToolchain, cmake_layout
from conan.tools.files import apply_conandata_patches, copy, export_conandata_patches, get, replace_in_file, rm, rmdir
from conan.tools.microsoft import check_min_vs, is_msvc, is_msvc_static_runtime
from conan.tools.scm import Git, Version
import os

required_conan_version = ">=2.0.0"


class PackageConan(ConanFile):
    name = "libfranka-common"
    description = "Types and definitions common to libfranka and the Franka Control Interface (FCI)"
    license = "Apache-2.0"
    url = "https://github.com/conan-io/conan-center-index"
    homepage = "https://github.com/frankaemika/libfranka-common"
    topics = ("franka", "robot")
    package_type = "header-library"
    settings = "os", "arch", "compiler", "build_type"

    def source(self):
        git = Git(self)
        git.clone(self.conan_data["sources"][self.version]["url"], target=".")
        git.checkout(self.conan_data["sources"][self.version]["commit"])

    def build(self):
        pass

    def package(self):
        copy(self, "LICENSE", self.source_folder, os.path.join(self.package_folder, "licenses"))
        copy(
            self,
            pattern="*",
            dst=os.path.join(self.package_folder, "include"),
            src=os.path.join(self.source_folder, "include"),
            keep_path=True)

    def package_info(self):
        self.cpp_info.libs = []
        self.cpp_info.libdirs = []

        self.cpp_info.set_property("cmake_file_name", "Franka-Common")
        self.cpp_info.set_property("cmake_target_name", "Franka::Franka-Common")
        self.cpp_info.set_property("cmake_target_aliases", ["libfranka-common"])

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import os

from conans import CMake, ConanFile


class TestPackageConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        if self.options["magnum-integration"].with_eigen:
            cmake.build(target="test-eigen")

    def test(self):
        bin_path = os.path.join("bin", "test-package")
        self.run(bin_path, run_environment=True)
        if self.options["magnum-integration"].with_eigen:            
            self.run(os.path.join("bin", "test-eigen"), run_environment=True)

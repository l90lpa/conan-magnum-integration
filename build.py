#!/usr/bin/env python
# -*- coding: utf-8 -*-
import copy

from cpt.packager import ConanMultiPackager

if __name__ == "__main__":
    builder = ConanMultiPackager()
    builder.add(
        settings={"arch": "x86_64", "build_type": "Release"},
        options={
            "corrade:with_rc": True,
            "magnum:with_sdl2application": False,
            "magnum:with_glfwapplication": True,
            "magum:with_tgaimporter": True,
            "magnum:with_anysceneimporter": True,
            "magnum:with_meshtools": True,
            "magnum-integration:with_imgui": True,
            "magnum-integration:with_bullet": True,
            "bullet3:double_precision": True,
        },
    )
    builder.add(
        settings={"arch": "x86_64", "build_type": "Debug"},
        options={
            "corrade:with_rc": True,
            "magnum:with_sdl2application": False,
            "magnum:with_glfwapplication": True,
            "magum:with_tgaimporter": True,
            "magnum:with_anysceneimporter": True,
            "magnum:with_meshtools": True,
            "magnum-integration:with_imgui": True,
            "magnum-integration:with_bullet": True,
            "bullet3:double_precision": True,
        },
    )

    # add c++17 build configs
    new_builds = []
    for settings, options, env_vars, build_requires, reference in builder.items:
        new_settings = copy.copy(settings)
        new_settings["compiler.cppstd"] = "17"
        new_settings["compiler.libcxx"] = "libstdc++11"
        new_builds.append([settings, options, env_vars, build_requires])
        new_builds.append([new_settings, options, env_vars, build_requires])
    builder.builds = new_builds

    builder.run()

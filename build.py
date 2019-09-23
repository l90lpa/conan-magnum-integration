#!/usr/bin/env python
import copy
from collections import defaultdict

from cpt.packager import ConanMultiPackager

if __name__ == "__main__":
    builder = ConanMultiPackager()
    builder.add_common_builds()

    # add c++17 build configs
    named_builds = defaultdict(list)
    for settings, options, env_vars, build_requires, reference in builder.items:
        settings["compiler.cppstd"] = "17"
        settings["compiler.libcxx"] = "libstdc++11"

        # magnum non-default settings
        options["magnum:with_sdl2application"] = False
        options["magnum:with_glfwapplication"] = True
        options["magnum:with_tgaimporter"] = True
        options["magnum:with_anysceneimporter"] = True
        options["magnum:with_meshtools"] = True

        named_builds[
            f"{settings['build_type']}-"
            f"{'shared' if options['magnum-integration:shared'] else 'static'}"
        ].append([settings, options, env_vars, build_requires, reference])

        imgui_options = copy.copy(options)
        imgui_options["magnum-integration:with_imgui"] = True
        named_builds[
            f"{settings['build_type']}-"
            f"{'shared' if options['magnum-integration:shared'] else 'static'}"
            "-imgui"
        ].append([settings, imgui_options, env_vars, build_requires, reference])

        eigen_options = copy.copy(options)
        eigen_options["magnum-integration:with_eigen"] = True
        named_builds[
            f"{settings['build_type']}-"
            f"{'shared' if options['magnum-integration:shared'] else 'static'}"
            "-eigen"
        ].append([settings, eigen_options, env_vars, build_requires, reference])

        imgui_and_eigen_options = copy.copy(options)
        imgui_and_eigen_options["magnum-integration:with_imgui"] = True
        imgui_and_eigen_options["magnum-integration:with_eigen"] = True
        named_builds[
            f"{settings['build_type']}-"
            f"{'shared' if options['magnum-integration:shared'] else 'static'}"
            "-imgui-eigen"
        ].append(
            [settings, imgui_and_eigen_options, env_vars, build_requires, reference]
        )

    builder.builds = []
    builder.named_builds = named_builds

    builder.run()

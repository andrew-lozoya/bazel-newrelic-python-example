
load("@rules_python//python:defs.bzl", "py_binary", "py_library")
load("@my_deps//:requirements.bzl", "requirement")

py_binary(
    name = "bin",
    srcs = ["bin.py"],
    deps = [":lib",
            ":external",
    ],
)

py_library(
    name = 'external',
    srcs = glob(["**/*.py"]),
    data = glob(["**/*"], exclude=["**/*.py", "**/* *", "BUILD", "WORKSPACE"]),
    # This makes this directory a top-level in the python import
    # search path for anything that depends on this.
    imports = ["."],
    deps = [
        requirement('newrelic'),
        requirement('flask'),
        requirement('Werkzeug'),
        requirement('itsdangerous'),
        requirement('MarkupSafe'),
        requirement('Jinja2'),
    ],
)

py_library(
    name = "lib",
    srcs = ["lib.py"],
)

filegroup(
    name = "srcs",
    srcs = ["BUILD"] + glob(["**/*.py"]),
)

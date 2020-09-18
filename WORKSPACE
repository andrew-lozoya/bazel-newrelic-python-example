# WORKSPACE

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "bazel_federation",
    url = "https://github.com/bazelbuild/bazel-federation/releases/download/0.0.2/bazel_federation-0.0.2.tar.gz",
    sha256 = "b10529fcf8a464591e845588348533981e948315b706183481e0d076afe2fa3c",
)

load("@bazel_federation//:repositories.bzl",
     "rules_python",
    )

rules_python()

load(
    "@bazel_federation//setup:rules_python.bzl",
    "rules_python_setup"
)
rules_python_setup(use_pip = True)

load(
    "@rules_python//python:pip.bzl",
    "pip_import"
)

# Create a central repo that knows about the dependencies needed for
# requirements.txt.
pip_import(   # or pip3_import
   name = "my_deps",
   requirements = "//:requirements.txt",
)

# Load the central repo's install function from its `//:requirements.bzl` file,
# and call it.
load(
    "@my_deps//:requirements.bzl",
    "pip_install"
)

pip_install()
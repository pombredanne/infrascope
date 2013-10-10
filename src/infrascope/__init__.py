# -*- coding: utf-8 -*-
""" Tools for Infrastructure Transparency.

    infrascope closes the feedback loop for data generated by your
    Infrastructure as Code, and delivery pipelines. It generates
    visibility for the  actual state of your deployments, like versions
    of artifacts in your repositories and runtime environments.

    For more, read the manual at http://1and1.github.io/infrascope/.

    Copyright © 2013 1&1 Internet AG

    Licensed under the Apache License, Version 2.0
"""
# Copyright © 2013 1&1 Internet AG
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

def pkg_info():
    """Return project information for setuptools."""
    try:
        doc = __doc__.decode("UTF-8")
    except (AttributeError, UnicodeError):
        doc = __doc__ # Python3, or some strangeness

    return dict(
        # project data & layout
        name = __name__.split('.')[0],
        ## TODO: version = re.search(r"(?<=\()[^)]+(?=\))", changelog).group(),
        package_dir = {"": "src"},
        ## TODO: packages = find_packages(projectdir / "src", exclude=["tests"]),
        test_suite = "nose.collector",
        zip_safe = True,
        include_package_data = True,
        data_files = [
            ("EGG-INFO", [
                "README.md", "LICENSE", "debian/changelog",
            ]),
        ],

        # dependency management
        install_requires = [
        ],
        setup_requires = [
            "docutils",
            "Sphinx",
        ],
        extras_require = {
        },

        # PyPI
        url = "https://github.com/1and1/infrascope",
        license = "Apache License Version 2.0",
        keywords = "python tool automation continuous.integration continuous.delivery devops reporting visualops",
        author = u"Jürgen Hermann",
        author_email = "jh@web.de",
        description = doc.split('.')[0].strip(),
        long_description = doc.split('.', 1)[1].strip(),
        classifiers = [
            # values at http://pypi.python.org/pypi?:action=list_classifiers
            "Development Status :: 3 - Alpha",
            #"Development Status :: 4 - Beta",
            #"Development Status :: 5 - Production/Stable",
            "Operating System :: OS Independent",
            "Environment :: Console",
            "Intended Audience :: Developers",
            "Intended Audience :: Information Technology",
            "Intended Audience :: System Administrators",
            "License :: OSI Approved :: Apache Software License",
            "Natural Language :: English",
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 2.7",
            "Topic :: Documentation",
            "Topic :: System :: Software Distribution",
            "Topic :: Utilities",
        ],
    )

from setuptools import setup

# this is a workaround for an issue in pip that prevents editable installs
# with --user, see https://github.com/pypa/pip/issues/7953
import site, sys; site.ENABLE_USER_SITE = "--user" in sys.argv[1:]

setup()

import os
import shutil
import urllib2
import urlparse

from hurry.resource import generate_code, ResourceInclusion, Library

VERSION = '1.4.3'
BASEURL = "http://github.com/DmitryBaranovskiy/raphael/raw/v%s/" % VERSION
MINIFIED = "raphael-min.js"
FULL = "raphael.js"


def prepare_raphael():
    package_dir = os.path.dirname(__file__)
    raphael_dest_path = os.path.join(package_dir, 'raphael-build')

    # remove previous raphael library build
    print 'recursivly removing "%s"' % raphael_dest_path
    shutil.rmtree(raphael_dest_path, ignore_errors=True)
    print 'create new "%s"' % raphael_dest_path
    os.mkdir(raphael_dest_path)

    for filename in [MINIFIED, FULL]:
        url = urlparse.urljoin(BASEURL, filename)
        print 'downloading "%s"' % url
        f = urllib2.urlopen(url)
        file_data = f.read()
        f.close()
        dest_filename = os.path.join(raphael_dest_path, filename)
        dest = open(dest_filename, 'wb')
        print 'writing data to "%s"' % dest_filename
        dest.write(file_data)
        dest.close()

    py_path = os.path.join(package_dir, '_lib.py')
    print 'Generating inclusion module "%s"' % py_path

    library = Library('raphael')
    inclusion_map = {}
    inclusion = inclusion_map['raphael'] = ResourceInclusion(library, FULL)
    inclusion.modes['minified'] = ResourceInclusion(library, MINIFIED)
    code = generate_code(**inclusion_map)
    module = open(py_path, 'w')
    module.write(code)
    module.close()


def main():
    # Commandline tool
    prepare_raphael()


def entrypoint(data):
    """Entry point for zest.releaser's prerelease script"""
    # We could grab data['new_version'] and omit the .1 suffix from it to get
    # the raphael version.  Could do away with a bit of version number
    # duplication.
    # And grab the tagdir or workingdir as base, perhaps.
    prepare_raphael()

from os.path import dirname, basename, isfile, join
import glob

# This code dynamically iterates through the blog posts we have in the writing folder and gets the file names
modules = glob.glob(join(dirname("blog/writing/"), "*.py"))
modules = [ basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]

# This code takes a file, imports it, and then runs the app() method
def run_writing_app(file_name):
    mod = __import__("writing.%s" % (file_name), fromlist=["main"])
    # mod.test()
    mod.app()
import os, re
from glob import glob
from os.path import isdir, join, basename, exists


class Barron:
    def __init__(self, resource_dir='res', extension='txt'):
        self.resource_dir = resource_dir

        # Add . to extension
        if extension and not extension.startswith('.'):
            self.extension = '.' + extension
        else:
            self.extension = extension

        self.word_lists = dict()

        # Load the file names from resource directory
        self.reload_files()


    def reload_files(self):
        # if the directory does not exist then do nothing
        if not exists(self.resource_dir) or not isdir(self.resource_dir):
            return
        # Filter files according to name and extension
        files = glob(join(self.resource_dir, '*%s' % self.extension))

        # Read the file name according to pattern
        for f in files:
            ptn = re.compile(r'^(.+)_(\d+)%s$' % self.extension.replace('.', r'\.'))
            base = basename(f)

            # Match the basename
            match = ptn.match(base)
            if match:
                bundle_name = match.group(1)
                bundle_unit = int(match.group(2))

                # Map the bundle name to actual file name
                if bundle_name not in self.word_lists:
                    self.word_lists[bundle_name] = dict()
                self.word_lists[bundle_name][bundle_unit] = base

    # List bundles and units
    def list_bundles(self):
        return sorted(self.word_lists.keys())

    def list_units(self, name):
        self.__valid_name(name)
        return sorted(self.word_lists[name].keys())

    # Load the words according to range
    def load_words(self, name, units):
        self.__valid_name(name)

        words = dict()
        for i in units:
            with open(self.__get_path(name, i)) as f:
                for line in f:
                    elements = line.split('|')
                    words[elements[0]] = elements[1:]

        return words

    def mkdir(self):
        if not isdir(self.resource_dir) and not exists(self.resource_dir):
            os.makedirs(self.resource_dir)

    # Helper methods
    def __get_path(self, name, unit):
        return join(self.resource_dir, self.word_lists[name][unit])

    def __valid_name(self, name):
        if name not in self.word_lists:
            raise ValueError('The bundle does not exist!')

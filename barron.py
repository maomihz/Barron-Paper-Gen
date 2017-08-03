import os
import re, glob


class Barron:
    def __init__(self, resource_dir='res', extension='txt'):
        if not os.path.isdir(resource_dir):
            raise ValueError('Resource directory does not exist!')
        self.resource_dir = resource_dir
        self.extension = extension
        self.word_lists = dict()

        # Load the file names from resource directory
        self.reload_files()


    def reload_files(self):
        # Filter files
        files = glob.glob(os.path.join(self.resource_dir, '*.%s' % self.extension))

        # Read the file name according to pattern
        for f in files:
            ptn = re.compile(r'^(.+)_(\d+)\.%s$' % self.extension)
            base = os.path.basename(f)

            match = ptn.match(base)
            if match:
                bundle_name = match.group(1)
                bundle_unit = match.group(2)

                if bundle_name not in self.word_lists:
                    self.word_lists[bundle_name] = dict()
                self.word_lists[bundle_name][int(bundle_unit)] = base

    # List bundles and units
    def list_bundles(self):
        return sorted(self.word_lists.keys())

    def list_units(self, name):
        self.__valid_name(name)
        return sorted(self.word_lists[name].keys())


    # Helper methods
    def __get_path(self, name, unit):
        return os.path.join(self.resource_dir, self.word_lists[name][unit])

    def __valid_name(self, name):
        if name not in self.word_lists:
            raise ValueError('The bundle does not exist!')

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

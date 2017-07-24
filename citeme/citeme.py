import functools
from six import iteritems

# Singleton!
class CiteMe(object):
    # Class variable!
    __instance = None
    __check_fields = True
    __pedantic = False

    # Override new to make this a singleton class
    # taken from http://python-3-patterns-idioms-test.readthedocs.io/en/latest/Singleton.html#id5
    def __new__(cls):
        if CiteMe.__instance is None:
            CiteMe.__instance = object.__new__(cls)
            # Initialization of class here, because
            # __init__ gets called multiple times
            CiteMe.__instance.references = {}
        return CiteMe.__instance

    def add_reference(self, citation):
        if CiteMe.__check_fields:
            citation.checkFields(CiteMe.__pedantic)

        if citation.type not in self.references:
            self.references[citation.type] = {}

        if citation.handle not in self.references[citation.type]:
            self.references[citation.type][citation.handle] = citation.description

    def print_references(self):
        for ref_type in self.references:
            for handle, description in iteritems(self.references[ref_type]):
                print(ref_type, handle, description)

    def references_by_type(self, ref_type):
        if ref_type in self.references:
            return self.references['ref_type']
        else:
            return []

    @staticmethod
    def set_pedantic(value):
        CiteMe.__pedantic = value

    @staticmethod
    def set_check_fields(value):
        CiteMe.__check_fields = value


class Citation(object):
    def __init__(self, handle, description, the_type):
        self.handle = handle
        self.description = description
        self.type = the_type

        # optional and required field
        # from https://en.wikipedia.org/wiki/BibTeX
        self._required = []
        self._optional = []
        self._general_options = ['url', 'doi']

    def __call__(self, f):
        def wrapped_f(*args):
            CiteMe().add_reference(self)
            f(*args)
        return wrapped_f

    def checkFields(self, pedantic):
        missing = []
        too_many = []
        if self._required:
            for field in self._required:
                if isinstance(field, tuple):
                    if not any(f in self.description for f in field):
                        missing.append(field)
                elif field not in self.description:
                    missing.append(field)

        if pedantic and self._optional:
            self._optional.extend(self._general_options)
            for field in self.description:
                found = False
                for option in self._optional:
                    if isinstance(option, tuple):
                        if field == option[0] or field == option[1]:
                            found = True
                    elif field == option:
                        found = True
                for option in self._required:
                    if isinstance(option, tuple):
                        if field == option[0] or field == option[1]:
                            found = True
                    elif field == option:
                        found = True
                if not found:
                    too_many.append(field)

        if missing or too_many:
            raise Exception("Fields for citation of type {0} is not correct:\n"
                            "required fields: {1}\n"
                            "optional fields: {2}\n\n"
                            "missing fields: {3}\n"
                            "non supported fields: {4}\n\n"
                            "found fields: {5}".format(
                                self.type, self._required, self._optional,
                                missing, too_many,
                                self.description.keys()
                            ))

class article(Citation):
    def __init__(self, handle, description):
        super(article, self).__init__(handle, description,
                                      'article')
        self._required = ['author', 'title', 'journal', 'year', 'volume']
        self._optional = ['number', 'pages', 'month', 'note', 'key']

class book(Citation):
    def __init__(self, handle, description):
        super(book, self).__init__(handle, description,
                                   'book')
        self._required = [('author', 'editor'), 'title', 'publisher', 'year']
        self._optional = [('volume', 'number'), 'series', 'address', 'edition', 'month', 'note', 'key']

class booklet(Citation):
    def __init__(self, handle, description):
        super(booklet, self).__init__(handle, description,
                                      'booklet')
        self._required = ['title']
        self._optional = ['author', 'howpublished', 'address', 'month', 'year', 'note', 'key']

class inbook(Citation):
    def __init__(self, handle, description):
        super(inbook, self).__init__(handle, description,
                                     'inbook')
        self._required = [('author', 'editor'), 'title', ('chapter', 'pages'), 'publisher', 'year']
        self._optional = [('volume', 'number'), 'series', 'type', 'address', 'edition', 'month', 'note', 'key']

class incollection(Citation):
    def __init__(self, handle, description):
        super(incollection, self).__init__(handle, description,
                                           'incollection')
        self._required = ['author', 'title', 'booktitle', 'publisher', 'year']
        self._optional = ['editor', ('volume', 'number'), 'series', 'type', 'chapter', 'pages', 'address', 'edition', 'month', 'note', 'key']

class inproceedings(Citation):
    def __init__(self, handle, description):
        super(inproceedings, self).__init__(handle, description,
                                            'inproceedings')
        self._required = ['author', 'title', 'booktitle', 'year']
        self._optional = ['editor', ('volume', 'number'), 'series', 'pages', 'address', 'month', 'organization', 'publisher', 'note', 'key']

# conference has the same fields as inproceedings
class conference(inproceedings):
    def __init__(self, handle, description):
        super(conference, self).__init__(handle, description,
                                         'conference')

class manual(Citation):
    def __init__(self, handle, description):
        super(manual, self).__init__(handle, description,
                                     'manual')
        self._required = ['title']
        self._optional = ['author', 'organization', 'address', 'edition', 'month', 'year', 'note', 'key']

class mastersthesis(Citation):
    def __init__(self, handle, description):
        super(mastersthesis, self).__init__(handle, description,
                                            'mastersthesis')
        self._required = ['author', 'title', 'school', 'year']
        self._optional = ['type', 'address', 'month', 'note', 'key']

class misc(Citation):
    def __init__(self, handle, description):
        super(misc, self).__init__(handle, description,
                                     'misc')
        self._optional = ['author', 'title', 'howpublished', 'month', 'year', 'note', 'key']

class phdthesis(Citation):
    def __init__(self, handle, description):
        super(phdthesis, self).__init__(handle, description,
                                        'phdthesis')
        self._required = ['author', 'title', 'school', 'year']
        self._optional = ['type', 'address', 'month', 'note', 'key']

class proceedings(Citation):
    def __init__(self, handle, description):
        super(proceedings, self).__init__(handle, description,
                                          'proceedings')
        self._required = ['title', 'year']
        self._optional = ['editor', ('volume', 'number'), 'series', 'address', 'month', 'publisher', 'organization', 'note', 'key']

class techreport(Citation):
    def __init__(self, handle, description):
        super(techreport, self).__init__(handle, description,
                                         'techreport')
        self._required = ['author', 'title', 'institution', 'year']
        self._optional = ['type', 'number', 'address', 'month', 'note', 'key']

class unpublished(Citation):
    def __init__(self, handle, description):
        super(unpublished, self).__init__(handle, description,
                                          'unpublished')
        self._required = ['author', 'title', 'note']
        self._optional = ['month', 'year', 'key']

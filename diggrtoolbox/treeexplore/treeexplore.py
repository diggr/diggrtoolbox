#!/usr/bin/env python3
"""
Getting data structures to work with, sometimes is hard, especially, when you
need to find specific information in nested jsons and no schema is provided,
or the data and its changing fast.

Author: F. Rämisch <raemisch@ub.uni-leipzig.de>
Copyright: 2018, Universitätsbibliothek Leipzig
License: GNU General Public License v3
"""

TAB_SYMBOL = "  "


class TreeExplore:

    def __init__(self, tree, tab_symbol=TAB_SYMBOL):

        if isinstance(tree, dict) or isinstance(tree, list):
            self.tree = tree
            self.tab_symbol = tab_symbol
        else:
            raise TypeError("This only makes sense for lists and dicts.")

    def display(self, value, indent):
        print("".join([self.tab_symbol for i in range(indent)]), value)

    def show(self, tree=None, indent=0):
        if not tree:
            tree = self.tree
        if isinstance(tree, dict):
            for key, value in tree.items():
                self.display(key, indent)
                if isinstance(value, dict) or isinstance(value, list):
                    self.show(value, indent+1)
        elif isinstance(tree, list):
            self.display(len(tree), indent)
        else:
            raise TypeError("Object to must be an instance of dict or list")

    def show_search_result(self, result):
        """
        Displays a search result together with its embedding and path
        """
        print("Search-Term: {}".format(result['term']))

        print("Route: ", end="")
        for step in result['route']:
            print(step, end=", ")
        print()

        if 'embedding' in result.keys():
            print("Embedding: '{}' ".format(result['embedding']), end="")
            if result['unique_in_embedding']:
                print('(unique)')
            else:
                print()


    def prepare_search_result(self,
                              term,
                              route,
                              results,
                              embedding=None,
                              show_result=True):
        """
        Prepares the search, appends it to the results list and organizes the
        printing.
        """
        result = {'term': term,
                  'route' : route}
        if embedding:
            unique_in_embedding = False
            embedding_length = len(embedding)
            l_occur = 0
            r_occur = embedding_length
            if embedding_length > 50:
                l_occur = embedding.find(term)
                r_occur = embedding.rfind(term)

                if l_occur == r_occur:
                    unique_in_embedding = True

                if l_occur - 10 < 0:
                    l_occur = 0
                else:
                    l_occur -= 10

                if r_occur + 10 > embedding_length:
                    r_occur = embedding_length
                else:
                    r_occur += 10

            result['embedding'] = embedding[l_occur:r_occur]
            result['unique_in_embedding'] = unique_in_embedding
        results.append(result)
        if show_result:
            self.show_search_result(result)
        return results

    def search(self, term, tree=None, route=None, results=None):
        """
        This function provides full text search for nested dicts/lists/both.
        It will return the path to every occasion of the term.
        """
        if tree is None:
            tree = self.tree

        if results is None:
            results = []

        if route is None:
            route = []
        else:
            route = route.copy()

        if isinstance(tree, dict):
            for key, value in tree.items():
                if isinstance(value, dict) or isinstance(value, list):
                    self.search(term, value, route+[key], results)
                if isinstance(term, int) or isinstance(term, float):
                    if term == key:
                        results = self.prepare_search_result(term,
                                                   route+[key],
                                                   results)
                        continue
                elif isinstance(term, str):
                    for element in [key, value]:
                        if isinstance(element, str):
                            if term in element:
                                results = self.prepare_search_result(term,
                                                                     route+[key],
                                                                     results,
                                                                     value)
                    continue
                else:
                    raise TypeError("Encountered unsupported type at {}".format(route))

        elif isinstance(tree, list):
            for e, element in enumerate(tree):
                if isinstance(element, dict) or isinstance(element, list):
                    self.search(term, element, route+[e], results)
                elif isinstance(element, int) or isinstance(element, float):
                    if term == element:
                        results = self.prepare_search_result(term,
                                                   route+[e],
                                                   results)
                        continue
                elif isinstance(term, str) and isinstance(element, str):
                    if term in element:
                        results = self.prepare_search_result(term,
                                                   route+[e],
                                                   results,
                                                   element)
                        continue
                elif isinstance(term, float) or isinstance(term, int):
                    continue
                elif element is None:
                    continue
                else:
                    raise TypeError("Encountered unsupported type at {}".format(route))
        else:
            raise TypeError("Not a valid tree to search in.")

        # # if len(results) == 0:
        # #     raise KeyError("Term '{}' was not found in the tree.".format(term))
        # else:
        return results

    def find(self, term):
        pass

    def find_key(self, key):
        """
        find_key
        """
        pass

    def find_value(self, value):
        pass

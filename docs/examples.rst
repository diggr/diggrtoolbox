========
Examples
========

To demonstrate possible applications of the tools of the toolbox, this page will contain example use cases.

ZipSingleAccess
---------------

TreeExplore
-----------

The TreeExplore class provides easy access to nested dicts/list or combinations of both::

    >>> import diggrtoolbox as dt
    >>> test_dict = {'id' : 123456789,
    >>>              'data' : {'name' : 'diggr project',
    >>>                        'city' : 'Leipzig',
    >>>                        'field': 'Video Game Culture'},
    >>>              'references':[{'url' : 'http://diggr.link',
    >>>                             'name' : 'diggr website'},
    >>>                             {'url' : 'http://ub.uni-leipzig.de',
    >>>                              'name' : 'UBL website'}]}
    >>> tree = dt.TreeExplore(test_dict)
    >>> results = tree.search("leipzig")
    Search-Term: leipzig
    Route: references, 1, url,
    Embedding: 'http://ub.uni-leipzig.de'
    >>> print(results)
    [{'embedding': 'http://ub.uni-leipzig.de',
      'route': ['references', 1, 'url'],
      'unique_in_embedding': False,
      'term': 'leipzig'}]

treehash
--------

Imagine you have a datastructure, which you use as a reference at some point in your workflow. It is provided as a JSON-file at some point online, e.g. the diggr platform mapping for the `MediaartsDB <https://diggr.github.io/platform_mapping/mediaartdb.json>`_.

This file is updated frequently. You write a program to check if the contents of the file change, compared with the version you have locally::

    import requests
    import diggrtoolbox as dt

    URL = 'https://diggr.github.io/platform_mapping/mediaartdb.json'

If the hashes turn out to be different, and you'd like to investigate the differences in more detail, we recommend using a diff-tool like `dictdiffer <https://github.com/inveniosoftware/dictdiffer>`_.

deepget
-------

The deepget function can be used easy with the results object of the TreeExplore search function, as demonstrated below::

    >>> import diggrtoolbox as dt
    >>> test_dict = {'id' : 123456789,
                     'data' : {'name' : 'diggr project',
                               'city' : 'Leipzig',
                               'field': 'Video Game Culture'},
                     'references':[{'url' : 'http://diggr.link',
                                    'name' : 'diggr website'},
                                   {'url' : 'http://ub.uni-leipzig.de',
                                    'name' : 'UBL website'}]}
    >>> tree = dt.TreeExplore(test_dict)
    >>> results = tree.quiet_search("leipzig")
    >>> for result in results:
            print(dt.deepget(test_dict, result['route']))
    http://ub.uni-leipzig.de

The *TreeExplore* class itself also provides an easy method for accessing nested objects. Either a key, index, result dict or route can be used::

    >>> print(tree[result])
    http://ub.uni-leipzig.de
    >>> print(tree[result['route']])
    http://ub.uni-leipzig.de
    >>> print(tree['references'][1]['url'])
    http://ub.uni-leipzig.de

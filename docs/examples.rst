========
Examples
========

To demonstrate possible applications of the tools of the toolbox, this page will contain example use cases.

UnifiedAPI / DiggrAPI
---------------------

This is the latest addition to the toolbox. It allows the user to have an easier access to the unifiedAPI without having to memorize addresses. You can set filters, select datasets, etc.

The following will create an instance, and select the dataset mobygames. 


    >>> from diggrtoolbox.unified_api import DiggrAPI
    >>> d = DiggrAPI("http://localhost:6660).dataset("mobygames")

If you now get() this, you will get a list of all ids.

    >>> ids = d.get()

Let's suppose you are interested in links. Apply a filter, and then iterate over all ids, and run your process

    >>> d.filter("links")
    >>> for id_ in ids:
    >>>     data = d.item(id_).get()
    >>>     # further processing

To clean up the code a bit, you can get the result immediately after setting an item id (or slug), by initializing DiggrAPI with `get_on_item=True`. If the "magic" (i.e. filtering the content of the request instead of returning the raw response) does not fit your needs, you can also set `raw=True`.

    >>> d = DiggrAPI("http://localhost:6660", get_on_item=True, raw=True)
    >>> d.dataset("mobygames").filter("links")
    >>> raw_data = d.item("id_")


ZipSingleAccess
---------------

Imagine you have a lot of data stored in one JSON-file. Often these files can be compressed to take a lot less space on your harddrive. When you want to work with the content of these files, of course you don't want to upack them first::

    >>> import diggrtoolbox as dt
    >>> z = ZipSingleAccess("data/compressed_file.zip")
    >>> j = z.json()
    >>> isinstance(j, dict)
    True
    >>> print(j.keys())
    dict_keys(['id', 'data', 'raw'])

ZipMultiAccess
--------------


Sometimes the data, you want so load from a file, which is bigger than the RAM you have. This is a problem, as it makes it impossible to work with files of this size without some tricks.

In the natural sciences this problem is tackled by using HDF5, a special file format, allowing to partially load the file, and only serve the parts needed for the next computation step. Unfortunately, this file is not quite made to store tree like structures like nested dicts/lists.

With ZipMultiAccess we make the first step into this direction. You save subtrees of your data in a subfolder, and then load it from the ZIP when you need it::

    >>> import diggrtoolbox as dt
    >>> z = ZipMultiAccess("data/compressed_files.zip")
    >>> j = z.json()
    >>> isinstance(j, list)
    True
    >>> len(j)
    38386
    >>> isinstance(j[0], dict)
    True
    >>> print(j[0].keys())
    dict_keys(['id', 'data', 'raw', 'matches'])
    >>> print(j[0]['matches'])
    {'n_matches': 3}
    >>> m1 = z.get(j[0]['id'])
    >>> isinstance(m, list)
    True
    >>> len(m)
    3

In the above example we have a list of 38386 which we matched with other games from another database. The match data is huge, so putting all data into one file resulted in a big freeze, as the amount of memory required to hold put all information into one Python object was larger, than the amount the machine had available.

All match data was put into separate files, in a subfolder *matches* and then referenced with the id in the filename. The name of the subfolder can be chosen arbitrarily.

There are multiple ways of accessing the additional files::

    >>> z[j[0]['id']] == z.get(j[0]['id'])
    True

TreeExplore
-----------

The TreeExplore class provides easy access to nested dicts/list or combinations of both::

    >>> import diggrtoolbox as dt
    >>> test_dict = {'id' : 123456789,
    >>>              'data' : {'name': 'diggr project',
    >>>                        'city': 'Leipzig',
    >>>                        'field': 'Video Game Culture'},
    >>>              'references':[{'url': 'http://diggr.link',
    >>>                             'name': 'diggr website'},
    >>>                             {'url': 'http://ub.uni-leipzig.de',
    >>>                              'name': 'UBL website'}]}
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

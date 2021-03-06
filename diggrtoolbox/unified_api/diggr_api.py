import requests

from collections import OrderedDict
from requests.compat import urljoin

MOBYGAMES = "mobygames"
GAMEFAQS = "gamefaqs"
MEDIAARTDB = "mediaartdb"

class DiggrAPI:
    """
    This class provides easy access to the diggr unified API.
    On initialization you have to provide the address of your desired unified API endpoint.
    You can now set the dataset and filters, which are persistent until reset.
    This allows you to iterate over a dataset without having to apply a filter each time.

    The get() method will do some magic to determine the correct way of creating the directory
    string depending on the content and dataset selected. I.e. prepend a "/slug", if the identifier
    is a slug and not an id, or replace slashes in gamefaqs ids.

        :Example:

        >>> d = DiggrAPI("http://localhost:6660").dataset("mobygames").filter("companies")
        >>> result = d.item("1").get()

        For the sake of readability you may want to execute the query immediately after the item is set.

        >>> d = DiggrAPI("http://localhost:6660", get_on_item=True)
        >>> d.dataset("mobygames").filter("companies")
        >>> results = []
        >>> for i in range(10):
        >>>     results.append(d.item(i))
    """

    DATASETS = (MOBYGAMES, GAMEFAQS, MEDIAARTDB)
    FILTERS = ("companies", "links", "cluster")

    def __init__(self, base_url, get_on_item=False, raw=False):
        self.base_url = base_url
        self.get_on_item = get_on_item
        self.raw = raw
        self.session = requests.Session()
        self.query = OrderedDict([
            ("dataset", None),
            ("item", ""),
            ("filter", ""),
        ])

    def get(self):
        """
        Runs the query and returns the result.
        """
        result = self.session.get(urljoin(self.base_url, self.directory))
        if result.ok:
            data = result.json()

            if self.raw:
                return data

            if not self.query["item"]:
                return data["ids"]
            else:
                if self.query["filter"] == "links":
                    return data["links"]
                else:
                    return data.get("entry", None)
        else:
            raise RuntimeError("Malformed Request")

    def dataset(self, dataset):
        """
        Selects a dataset.
        """
        if dataset not in self.DATASETS:
            raise ValueError("{dataset} must be in {d for d in self.DATASETS}")
        self.query["dataset"] = dataset
        return self

    def item(self, id_or_slug):
        """
        Selects an item, can be given a numeric id or a slug.
        Returns self or the result of the query if get_on_item is set.
        """
        if isinstance(id_or_slug, int):
            self.query["item"] = str(id_or_slug)
        elif id_or_slug.isdigit():
            self.query["item"] = id_or_slug
        else:
            if self.query["dataset"] == MOBYGAMES:
                self.query["item"] = f"slug/{id_or_slug}"
            if self.query["dataset"] == GAMEFAQS:
                self.query["item"] = id_or_slug.replace("/", "__")
            else:
                self.query["item"] = id_or_slug
        if self.get_on_item:
            return self.get()
        else:
            return self

    def filter(self, filterstring):
        """
        Applies a filter. Must be in self.FILTERS.
        """
        if filterstring not in self.FILTERS:
            raise ValueError("{dataset} must be in {d for d in self.DATASETS}")
        self.query["filter"] = filterstring
        return self

    @property
    def directory(self):
        """
        Returns the directory string from self.query.
        Raises ValueError if no dataset or item is set.
        """
        if not self.query["dataset"]:
            raise ValueError("At least a dataset must be selected")
        if not self.query["filter"]:
            if self.query["item"]:
                return "{}/{}".format(self.query["dataset"], self.query["item"])
            else:
                return self.query["dataset"]
        else:
            if not self.query["item"]:
                raise ValueError("You cannot set a filter without selecting an item")
            else:
                return "{}/{}/{}".format(*self.query.values())

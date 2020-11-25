class Presenter():
    """This class controls the console view
    author: V. Van den Schrieck
    date: November 2020
    """
    def __init__(self, sites):
        self.__sites = sites
        self.__view = None

    def set_view(self, view_instance):
        self.__view = view_instance

    def test_all(self):
        """Called by the view, to be applied to the model"""
        for site in self.__sites:
            site.test()
            self.__view.refresh()

    def sites(self):
        """Returns a representation of the sites for the view"""
        view_sites = {}
        for site in self.__sites :
            view_sites[site.name] = site.status
        return view_sites

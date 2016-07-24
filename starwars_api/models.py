from starwars_api.client import SWAPIClient 
from starwars_api.exceptions import SWAPIClientError

api_client = SWAPIClient()


class BaseModel(object):
    global RESOURCE_NAME
    def __init__(self, json_data):
        """
        Dynamically assign all attributes in `json_data` as instance
        attributes of the Model.
        """
        for key in json_data:
            setattr(self,str(key),json_data[key])

    @classmethod
    def get(cls, resource_id):
        """
        Returns an object of current Model requesting data to SWAPI using
        the api_client.
        """
        getter = "api_client.get_" + RESOURCE_NAME + "(" + str(resource_id) + ")"
        actual_getter = eval(getter)
        based_get_data = cls(actual_getter)
        return based_get_data

    @classmethod
    def all(cls):
        """
        Returns an iterable QuerySet of current Model. The QuerySet will be
        later in charge of performing requests to SWAPI for each of the
        pages while looping.
        """
        aller = "api_client.get_" + RESOURCE_NAME + "()"
        actual_aller = eval(aller)
        based_all_data = cls(actual_aller)
        return BaseQuerySet(based_all_data)
        # if based_all_data["results"]:
        #     cls.results_only = based_all_data["results"]
        # else:
        #     raise AssertionError
        # return cls.results_only
        
class BaseQuerySet(object):

    def __init__(self,results):
        self.results = results["results"]

    def __iter__(self):
        self.counter = 0
        self.gen = (self.results[i] for i in self.results)
        return self

    def __next__(self):
        """
        Must handle requests to next pages in SWAPI when objects in the current
        page were all consumed.
        """
        pass

    next = __next__

    def count(self):
        """
        Returns the total count of objects of current model.
        If the counter is not persisted as a QuerySet instance attr,
        a new request is performed to the API in order to get it.
        """
        pass


class People(BaseModel,BaseQuerySet):
    """Representing a single person"""
    global RESOURCE_NAME
    RESOURCE_NAME = 'people'

    def __init__(self, json_data):
        super(People, self).__init__(json_data)

    def __repr__(self):
        return 'Person: {0}'.format(self.name)


# class Films(BaseModel):
#     global RESOURCE_NAME
#     RESOURCE_NAME = 'films'

#     def __init__(self, json_data):
#         super(Films, self).__init__(json_data)

#     def __repr__(self):
#         return 'Film: {0}'.format(self.title)


# class BaseQuerySet(object):

#     # def __init__(self):
#     #     pass

#     def __iter__(self):
#         self.counter = 0
#         return self

#     def __next__(self):
#         """
#         Must handle requests to next pages in SWAPI when objects in the current
#         page were all consumed.
#         """
#         if self.counter > count(self):
#             raise StopIteration
#         else:
#             pass
            

#     next = __next__

#     def count(self):
#         """
#         Returns the total count of objects of current model.
#         If the counter is not persisted as a QuerySet instance attr,
#         a new request is performed to the API in order to get it.
#         """
#         pass


# class PeopleQuerySet(BaseQuerySet):
#     RESOURCE_NAME = 'people'

#     def __init__(self):
#         super(PeopleQuerySet, self).__init__()

#     def __repr__(self):
#         return 'PeopleQuerySet: {0} objects'.format(str(len(self.objects)))


# class FilmsQuerySet(BaseQuerySet):
#     RESOURCE_NAME = 'films'

#     def __init__(self):
#         super(FilmsQuerySet, self).__init__()

#     def __repr__(self):
#         return 'FilmsQuerySet: {0} objects'.format(str(len(self.objects)))


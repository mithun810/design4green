import models

def get_data():
    print("Total number of records is", models.data_indexed.query.count())


def get_filters(region=null):
    print("Total number of records is", models.data_indexed.query.count())
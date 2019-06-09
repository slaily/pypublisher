from djongo import models


class Base(models.Model):
    # Using the ObjectIdField avoid calling Django migrations
    # every time on creating a new model.
    _id = models.ObjectIdField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    # It gives access to the complete pymongo collection API.
    # You can directly access any pymongo command by prefixing
    # mongo_ to the command name.
    # Example : aggregate function name becomes mongo_aggregate
    objects = models.fields.DjongoManager()

    class Meta:
        abstract = True

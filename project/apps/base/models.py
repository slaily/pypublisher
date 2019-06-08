from django.db import models
from djongo.models.fields import DjongoManager


class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    # It gives access to the complete pymongo collection API.
    # You can directly access any pymongo command by prefixing
    # mongo_ to the command name.
    # Example : aggregate function name becomes mongo_aggregate
    objects = DjongoManager()

    class Meta:
        abstract = True

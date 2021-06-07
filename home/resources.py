from import_export import resources
from .models import Msmes

class MsmesResource(resources.ModelResource):
    class Meta:
        model = Msmes
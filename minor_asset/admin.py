from django.contrib import admin
from .models import *

admin.site.register(Machine)
admin.site.register(Adresse)
admin.site.register(Agent)
admin.site.register(Client)
admin.site.register(Provider)
admin.site.register(Location)
admin.site.register(CategoryInventory)
admin.site.register(Inventory)
admin.site.register(InventoryInto)
admin.site.register(InventoryOut)
admin.site.register(Team)
admin.site.register(CategoriePanne)
admin.site.register(CodePanne)
admin.site.register(WorkOrder)
admin.site.register(Diagnostics)
admin.site.register(TrackingPieces)
admin.site.register(PlanifierMaintenance)
admin.site.register(Remind)
# Register your models here.

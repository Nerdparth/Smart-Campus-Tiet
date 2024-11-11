from ninja import ModelSchema
from .models import books_to_be_bought,Inventory,Books


class BuyingSchema(ModelSchema):
    class Meta:
        model = books_to_be_bought
        fields = '__all__'

class GetBudget(ModelSchema):
    class Meta:
        model = Inventory
        fields = ['Budget']

class BoughtSchema(ModelSchema):
    class Meta:
        model = Books
        fields = '__all__'
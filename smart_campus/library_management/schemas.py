from ninja import ModelSchema, Schema
from .models import books_to_be_bought, Inventory, Books


class BuyingSchema(ModelSchema):
    class Meta:
        model = books_to_be_bought
        fields = "__all__"


class GetBudget(ModelSchema):
    class Meta:
        model = Inventory
        fields = ["Budget"]


class BoughtSchema(ModelSchema):
    class Meta:
        model = Books
        fields = "__all__"


class DeleteBookSchema(Schema):
    book_name: str
    author: str


class BookCountSchema(Schema):
    book_count: int
    requests_count: int

class UpdateStatusSchema(Schema):
    status : str

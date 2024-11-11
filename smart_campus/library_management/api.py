from ninja import NinjaAPI
from .models import books_to_be_bought, Inventory, Books
from .schemas import BuyingSchema,GetBudget,BoughtSchema
from django.http import JsonResponse


app = NinjaAPI()


@app.post("/add-item", response=BuyingSchema)
def add_item(request, details:BuyingSchema):
    budget_getter = Inventory.objects.get(id=1) #to get the budget
    budget = budget_getter.Budget

    if details.price <= budget:
        book_name = details.book_name
        quantity = details.quantity
        price = details.price
        author = details.author
        remarks = details.remarks
        added_item = books_to_be_bought.objects.create(book_name=book_name, quantity=quantity, author=author, price=price, remarks=remarks)
        update_budget = Inventory.objects.filter(id=1).update(Budget = budget - price)
        return JsonResponse({"message": "item added to inventory"})
    else:
        return JsonResponse({"message" : "price exceeds budget"})
    

@app.get("get-budget", response=GetBudget)
def get_budget(request):
    budget = Inventory.objects.get(id=1)
    return budget

@app.post("edit-budget", response=GetBudget)
def edit_budget(request, details:GetBudget):
    updated_budget = details.Budget
    update_budget = Inventory.objects.filter(id=1).update(Budget = updated_budget)
    return JsonResponse({"message": "updated the budget"})

@app.post("/add-bought-item", response=BoughtSchema)
def add_item(request, details:BoughtSchema):

    book_name = details.book_name
    quantity = details.quantity
    author = details.author
    added_item = Books.objects.create(book_name = book_name,quantity=quantity, author=author)
    return JsonResponse({"message": "item added to bought items"})

@app.get("/get-all-books")
def get_books(request):
    books = Books.objects.all()
    data = []
    for book in books:
        data.append({
            "book_name" : book.book_name,
            "quantity" : book.quantity,
            "author" : book.author
        })
    return data

@app.get("/get-all-future-books")
def get_books(request):
    books = books_to_be_bought.objects.all()
    data = []
    for book in books:
        data.append({
            "book_name" : book.book_name,
            "quantity" : book.quantity,
            "author" : book.author,
            "price" : book.price,
            "remarks" : book.remarks
        })
    return data


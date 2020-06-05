import pytest

from essentials_kit_management.models import (
    User, Brand, Item, Order, Section, Form
)

from essentials_kit_management.interactors.storages.dtos import (
    OrderDto
    
    )


users_list = [
    {
        "name": "sulthan",
        "username": 9876543213,
        "password": "sulthan123"},
    {
        "name": "anjali ameer",
        "username": 9876543214,
        "password": "anju123"},
    {
        "name": "dulkar",
        "username": 9876543215,
        "password": "dulkar123"}
    ]


brand_list = [
    {"name": "brand1", "min_quantity": 1, "max_quantity": 5, "price_per_item": 100},
    {"name": "brand2", "min_quantity": 2, "max_quantity": 8, "price_per_item": 200},
    {"name": "brand3", "min_quantity": 3, "max_quantity": 9, "price_per_item": 300},
    {"name": "brand4", "min_quantity": 4, "max_quantity": 9, "price_per_item": 400}
    ]

item_list = [
    {"name": "item1", "description": "item1"},
    {"name": "item2", "description": "item2"},
    {"name": "item3", "description": "item3"}
    ]


section_list = [
    {"name": "section1", "description": "section1"},
    {"name": "section2", "description": "section2"},
    {"name": "section3", "description": "section3"}
    ]


form_list = [
    {
        "name": "form1",
        "description": "form1",
        "close_date": "2020-10-10",
        "expected_delivery_date": "2020-10-10",
        "status": "LIVE" },
    {
        "name": "form2",
        "description": "form2",
        "close_date": "2020-10-10",
        "expected_delivery_date": "2020-10-10",
        "status": "CLOSED" },
    {
        "name": "form3",
        "description": "form3",
        "close_date": "2020-10-10",
        "expected_delivery_date": "2020-10-10",
        "status": "DONE" }
    ]



order_list = [
     {
         "user_id":1,
         "item_id": 1,
         "brand_id": 1,
         "form_id": 1,
         "section_id": 1,
         "count": 10,
         "pending_count": 5,
         "out_of_stock": 0
     },
     {
         "user_id":1,
         "item_id": 2,
         "brand_id": 2,
         "form_id": 2,
         "section_id": 1,
         "count": 10,
         "pending_count": 5,
         "out_of_stock": 0},
    {
         "user_id":2,
         "item_id": 3,
         "brand_id": 4,
         "form_id": 3,
         "section_id": 1,
         "count": 10,
         "pending_count": 5,
         "out_of_stock": 0
     }
]



@pytest.fixture()
def create_sections():
    obj_list = []
    for section in section_list:
        obj = Section.objects.create(name=section["name"],
                    description=section["description"])
        obj_list.append(obj)

    return obj_list

@pytest.fixture()
def create_items():
    obj_list = []
    for item in item_list:
        obj = Item.objects.create(name=item["name"],
                 description=item["description"])
        obj_list.append(obj)

    return obj_list

@pytest.fixture()
def create_orders():
    obj_list = []
    for order in order_list:
        obj = Order.objects.create(
                user_id=order["user_id"],
                item_id=order["item_id"],
                brand_id=order["brand_id"],
                form_id=order["form_id"],
                section_id=order["section_id"],
                count=order["count"],
                pending_count=order["pending_count"],
                out_of_stock=order["out_of_stock"])
        obj_list.append(obj)
    return obj_list

@pytest.fixture()
def create_forms():
    obj_list = []
    for form in form_list:
        obj = Form.objects.create(
                 name=form["name"],
                 description=form["description"],
                 close_date=form["close_date"],
                 expected_delivery_date=form["expected_delivery_date"],
                 status=form["status"])
        obj_list.append(obj)
    return obj_list

@pytest.fixture()
def create_brands():
    obj_list = []
    for brand in brand_list:
        obj = Brand.objects.create(
                  name=brand["name"],
                  min_quantity=brand["min_quantity"],
                  max_quantity=brand["max_quantity"],
                  price_per_item=brand["price_per_item"])
        obj_list.append(obj)
    return obj_list

@pytest.fixture()
def create_users():
    obj_list = []
    for user in users_list:
        obj = User.objects.create(
                 name=user["name"],
                 username=user["username"],
                 password=user["password"])
        obj_list.append(obj)
    return obj_list



@pytest.fixture()
def add_multiple_sections_to_form(create_sections, create_forms):
    create_forms[0].sections.add(
        create_sections[1]
        )


@pytest.fixture()
def add_multiple_items_to_section(create_items, create_sections):
       create_sections[0].items.add(
        create_items[1], create_items[2]
    )
    

@pytest.fixture()
def adding_brands_to_items(create_brands, create_items):
    create_items[0].brand.add(
        create_brands[-1],
        create_brands[-2]
    )


@pytest.fixture()
def populate_data(create_users,
                  create_brands,
                  create_items,
                  create_sections,
                  create_forms,
                  create_orders,
                  adding_brands_to_items,
                  add_multiple_items_to_section,
                  add_multiple_sections_to_form):
    
    data = (create_brands,
    create_forms,
    create_items,
    create_orders,
    create_users,
    create_sections,
    add_multiple_items_to_section,
    add_multiple_sections_to_form,
    adding_brands_to_items)

    return data


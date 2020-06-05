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
    {"name": "brand4", "min_quantity": 4, "max_quantity": 9, "price_per_item": 400},
    ]

item_list = [
    {"name": "item1", "description": "item1"},
    {"name": "item2", "description": "item2"},
    {"name": "item3", "description": "item3"}
    ]

section_list = [
    {"name": "section1", "description": "section1"},
    {"name": "section2", "description": "section2"},
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

    section_objs = [
            Section.objects.create(name=section["name"],
                    description=section["description"])
            for section in section_list
            ]

    return section_objs


@pytest.fixture()
def add_multiple_sections_to_form(create_sections, create_forms):
    create_forms[0].sections.add(create_sections[0],
                                 create_sections[1])

@pytest.fixture()
def add_multiple_items_to_section(create_items, create_sections):
    create_sections[0].items.add(create_items[0],
                                 create_items[1])
    create_sections[1].items.add(create_items[2])


@pytest.fixture()
def create_items():

    item_objs = [   
            Item.objects.create(name=item["name"],
                 description=item["description"])
            for item in item_list
            ]
    return item_objs


@pytest.fixture()
def adding_brands_to_items(create_brands, create_items):
    create_items[0].brand.add(create_brands[0],
                                  create_brands[1])
    create_items[1].brand.add(create_brands[2])
    create_items[2].brand.add(create_brands[3])

@pytest.fixture()
def create_orders():
    order_objs = [
            Order.objects.create(user_id=order["user_id"],
                  item_id=order["item_id"],
                  brand_id=order["brand_id"],
                  form_id=order["form_id"],
                  section_id=order["section_id"],
                  count=order["count"],
                  pending_count=order["pending_count"],
                  out_of_stock=order["out_of_stock"]
                )
            for order in order_list
            ]
    return order_objs



@pytest.fixture()
def create_forms():

    form_objs = [
            Form.objects.create(name=form["name"],
                 description=form["description"],
                 close_date=form["close_date"],
                 expected_delivery_date=form["expected_delivery_date"],
                 status=form["status"])
            for form in form_list
            ]
    return form_objs


@pytest.fixture()
def create_brands():

    brand_objs = [
            Brand.objects.create(
                name=brand["name"],
                min_quantity=brand["min_quantity"],
                max_quantity=brand["max_quantity"],
                price_per_item=brand["price_per_item"])
            for brand in brand_list
            ]
    return brand_objs


@pytest.fixture()
def create_users():

    user_objs = [
            User.objects.create(
                name=user["name"],
                username=user["username"],
                password=user["password"])
            for user in users_list
        ]
    return user_objs

@pytest.fixture()
def populate_data(create_users,
                  create_brands,
                  create_items,
                  create_sections,
                  create_forms,
                  create_orders,
                  add_multiple_items_to_section,
                  add_multiple_sections_to_form,
                  adding_brands_to_items):
    
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




order1 = OrderDto(
        order_id=1,
        user_id=1,
        item_id=1,
        brand_id=1,
        form_id=1,
        section_id= 1,
        count=10,
        pending_count=5,
        out_of_stock=0)
order2 = OrderDto(
        order_id=1,
        user_id=1,
        item_id=2,
        brand_id=2,
        form_id=2,
        section_id= 1,
        count=10,
        pending_count=5,
        out_of_stock=0)
   
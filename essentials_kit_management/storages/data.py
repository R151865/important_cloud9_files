# from essentials_kit_management.constants.enums import (
#     TransactionStatusEnum, TransactionTypeEnum
#     )

# from essentials_kit_management.models import (
#     User, Brand, Item, Order, Section, Form, Transaction, Account
# )


# users_list = [
#     {
#         "name": "sulthan",
#         "username": 9876543213,
#         "password": "sulthan123",
#         "is_admin": False
#     },
#     {
#         "name": "anjali ameer",
#         "username": 9876543214,
#         "password": "anju123",
#         "is_admin": False
#     },
#     {
#         "name": "prudhvi",
#         "username": 12345,
#         "password": "12345",
#         "is_admin": False
#     },
#     {
#         "name": "Admin1",
#         "username": 111111111,
#         "password": "11111111",
#         "is_admin": True
#     },
#     {
#         "name": "Admin2",
#         "username": "22222222",
#         "password": "anju123",
#         "is_admin": True
#     }

#     ]


# brand_list = [
#     {
#         "name": "brand1",
#         "min_quantity": 1,
#         "max_quantity": 5,
#         "price_per_item": 100
#     },
#     {
#         "name": "brand2",
#         "min_quantity": 2,
#         "max_quantity": 8,
#         "price_per_item": 200
#     },
#     {
#         "name": "brand3",
#         "min_quantity": 3,
#         "max_quantity": 9,
#         "price_per_item": 300
#     },
#     {
#         "name": "brand4",
#         "min_quantity": 1,
#         "max_quantity": 9,
#         "price_per_item": 400
#     },
#     {
#         "name": "brand5",
#         "min_quantity": 2,
#         "max_quantity": 9,
#         "price_per_item": 700
#     },
#     {
#         "name": "brand6",
#         "min_quantity": 4,
#         "max_quantity": 9,
#         "price_per_item": 600
#     },
#     {
#         "name": "brand7",
#         "min_quantity": 4,
#         "max_quantity": 9,
#         "price_per_item": 500
#     }
# ]

# item_list = [
#     {
#         "name": "item1",
#         "description": "item1"
#     },
#     {
#         "name": "item2",
#         "description": "item2"
#     },
#     {
#         "name": "item3",
#         "description": "item3"
#     },
#     {
#         "name": "item4",
#         "description": "item4"
#     },
#     {
#         "name": "item5",
#         "description": "item5"
#     }
# ]

# section_list = [
#     {
#         "name": "section1",
#         "description": "section1"
#     },
#     {
#         "name": "section2",
#         "description": "section2"
#     },
#     {
#         "name": "section3",
#         "description": "section3"
#     },
#     {
#         "name": "section4",
#         "description": "section4"
#     },
# ]


# form_list = [
#     {
#         "name": "form1",
#         "description": "form1",
#         "close_date": "2020-10-10",
#         "expected_delivery_date": "2020-10-10",
#         "status": "LIVE" },
#     {
#         "name": "form2",
#         "description": "form2",
#         "close_date": "2020-10-10",
#         "expected_delivery_date": "2020-10-10",
#         "status": "CLOSED" },
#     {
#         "name": "form3",
#         "description": "form3",
#         "close_date": "2020-10-10",
#         "expected_delivery_date": "2020-10-10",
#         "status": "DONE" },
#     {
#         "name": "form1",
#         "description": "form1",
#         "close_date": "2020-10-10",
#         "expected_delivery_date": "2020-10-10",
#         "status": "LIVE" },
#     {
#         "name": "form2",
#         "description": "form2",
#         "close_date": "2020-10-10",
#         "expected_delivery_date": "2020-10-10",
#         "status": "CLOSED" },
#     {
#         "name": "form3",
#         "description": "form3",
#         "close_date": "2020-10-10",
#         "expected_delivery_date": "2020-10-10",
#         "status": "DONE" },
#     {
#         "name": "form1",
#         "description": "form1",
#         "close_date": "2020-10-10",
#         "expected_delivery_date": "2020-10-10",
#         "status": "LIVE" },
#     {
#         "name": "form2",
#         "description": "form2",
#         "close_date": "2020-10-10",
#         "expected_delivery_date": "2020-10-10",
#         "status": "CLOSED" },
#     {
#         "name": "form3",
#         "description": "form3",
#         "close_date": "2020-10-10",
#         "expected_delivery_date": "2020-10-10",
#         "status": "DONE" },
#     {
#         "name": "form1",
#         "description": "form1",
#         "close_date": "2020-10-10",
#         "expected_delivery_date": "2020-10-10",
#         "status": "LIVE" }


#     ]


# order_list = [
#      {
#          "user_id":1,
#          "item_id": 1,
#          "brand_id": 1,
#          "form_id": 1,
#          "section_id": 1,
#          "count": 10,
#          "pending_count": 5,
#          "out_of_stock": 0
#      },
#      {
#          "user_id":2,
#          "item_id": 1,
#          "brand_id": 2,
#          "form_id": 1,
#          "section_id": 1,
#          "count": 10,
#          "pending_count": 5,
#          "out_of_stock": 3
#      },
#      {
#          "user_id":1,
#          "item_id": 3,
#          "brand_id": 3,
#          "form_id": 1,
#          "section_id": 2,
#          "count": 10,
#          "pending_count": 5,
#          "out_of_stock": 0},
#     {
#          "user_id":2,
#          "item_id": 3,
#          "brand_id": 3,
#          "form_id": 1,
#          "section_id": 2,
#          "count": 10,
#          "pending_count": 5,
#          "out_of_stock": 0
#      },
#      {
#          "user_id":1,
#          "item_id": 4,
#          "brand_id": 5,
#          "form_id": 2,
#          "section_id": 1,
#          "count": 10,
#          "pending_count": 5,
#          "out_of_stock": 0
#      }
# ]


# transaction_list = [
#     {
#         "transaction_id": 111111,
#         "user_id": 1,
#         "amount": 1000,
#         "status": TransactionStatusEnum.APPROVED.value,
#         "transaction_type": TransactionTypeEnum.PHONE_PAY.value,
#         "screen_shot": "12/12",
#         "remark": "wallet"
#     },
#     {
#         "transaction_id": 111112,
#         "user_id": 1,
#         "amount": -500,
#         "status": TransactionStatusEnum.APPROVED.value,
#         "transaction_type": "",
#         "screen_shot": "12/12",
#         "remark": "Snack form"
#     },
#     {
#         "transaction_id": 111113,
#         "user_id": 1,
#         "amount": 100,
#         "status": TransactionStatusEnum.REJECTED.value,
#         "transaction_type": TransactionTypeEnum.PHONE_PAY.value,
#         "screen_shot": "12/12",
#         "remark": "wallet"
#     },
#     {
#         "transaction_id": 111114,
#         "user_id": 1,
#         "amount": -200,
#         "status": "",
#         "transaction_type": "",
#         "screen_shot": "12/12",
#         "remark": "Fruits form"
#     },
#     {
#         "transaction_id": 111115,
#         "user_id": 2,
#         "amount": 200,
#         "status": TransactionStatusEnum.PENDING.value,
#         "transaction_type": TransactionTypeEnum.GOOGLE_PAY.value,
#         "screen_shot": "12/12",
#         "remark": "Fruits form"
#     }
# ]


# account_list = [
#     {
#         "upi_id": "1234567890@SBI"
#     }
# ]



# def create_sections():

#     section_objs = [
#             Section.objects.create(name=section["name"],
#                     description=section["description"])
#             for section in section_list
#             ]

#     return section_objs


# def add_multiple_sections_to_form(create_sections, create_forms):
#     create_forms[0].sections.add(create_sections[0],
#                                  create_sections[1])
#     create_forms[1].sections.add(create_sections[2])
#     create_forms[2].sections.add(create_sections[3])
#     return create_forms

# def add_multiple_items_to_section(create_items, create_sections):
#     create_sections[0].items.add(create_items[0],
#                                  create_items[1])
#     create_sections[1].items.add(create_items[2])
#     create_sections[2].items.add(create_items[3])
#     create_sections[3].items.add(create_items[4])
#     return create_sections

# def adding_brands_to_items(create_brands, create_items):
#     create_items[0].brand.add(create_brands[0],
#                               create_brands[1])
#     create_items[1].brand.add(create_brands[2],
#                               create_brands[3])
#     create_items[2].brand.add(create_brands[4])
#     create_items[3].brand.add(create_brands[5])
#     create_items[4].brand.add(create_brands[6])
#     return create_items


# def create_items():

#     item_objs = [   
#             Item.objects.create(name=item["name"],
#                  description=item["description"])
#             for item in item_list
#             ]
#     return item_objs


    
# def create_orders():
#     order_objs = [
#             Order.objects.create(user_id=order["user_id"],
#                   item_id=order["item_id"],
#                   brand_id=order["brand_id"],
#                   form_id=order["form_id"],
#                   section_id=order["section_id"],
#                   count=order["count"],
#                   pending_count=order["pending_count"],
#                   out_of_stock=order["out_of_stock"]
#                 )
#             for order in order_list
#             ]
#     return order_objs


# def create_forms():

#     form_objs = [
#             Form.objects.create(name=form["name"],
#                  description=form["description"],
#                  close_date=form["close_date"],
#                  expected_delivery_date=form["expected_delivery_date"],
#                  status=form["status"])
#             for form in form_list
#             ]
#     return form_objs


# def create_brands():

#     brand_objs = [
#             Brand.objects.create(
#                 name=brand["name"],
#                 min_quantity=brand["min_quantity"],
#                 max_quantity=brand["max_quantity"],
#                 price_per_item=brand["price_per_item"])
#             for brand in brand_list
#             ]
#     return brand_objs


# def create_users():

#     user_objs = [
#             User.objects.create(
#                 name=user["name"],
#                 username=user["username"],
#                 password=user["password"],
#                 is_admin=user["is_admin"])
#             for user in users_list
#         ]
#     return user_objs


# def create_transactions():

#     for transaction in transaction_list:
#         Transaction.objects.create(
#             transaction_id=transaction['transaction_id'],
#             user_id=transaction['user_id'],
#             amount=transaction['amount'],
#             status=transaction['status'],
#             transaction_type=transaction["transaction_type"],
#             screen_shot=transaction["screen_shot"],
#             remark=transaction["remark"])


# def create_account():
#     for account in account_list:
#         Account.objects.create(upi_id=account["upi_id"])


# def data_populate():

#     create_users1 = create_users()
#     create_brands1 = create_brands()
#     create_items1 = create_items()
#     create_sections1 = create_sections()
#     create_forms1 = create_forms()
#     create_orders1 = create_orders()
#     create_account()
#     create_transactions()
#     print("Models Created .........!")
#     adding_brands_to_items1 = adding_brands_to_items(
#         create_items=create_items1,
#         create_brands=create_brands1)

#     add_multiple_items_to_section1 = add_multiple_items_to_section(
#         create_items=create_items1,
#         create_sections=create_sections1)

#     add_multiple_sections_to_form1 = add_multiple_sections_to_form(
#         create_forms=create_forms1,
#         create_sections=create_sections1)
#     print("Relatons created ..........!")
    
#     return "Data populated successfully......! Hurrah.."



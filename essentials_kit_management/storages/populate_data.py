import datetime


from essentials_kit_management.models import (
    User, Item, Brand, Section, Form, Transaction, Order, Account
    )


users_list = [
    {
        "name": "prudhvi",
        "username": "prudhvi",
        "password": "prudhvi123",
        "is_admin": False
    },
    {
        "name": "sulthan",
        "username": "12345",
        "password": "12345",
        "is_admin": False
    },
    {
        "name": "johncena",
        "username": "johncena",
        "password": "johncena123",
        "is_admin": False
    },
    
    {
        "name": "che guevara",
        "username": "che",
        "password": "che123",
        "is_admin": False
    },
    {
        "name": "Admin1",
        "username": "admin1123",
        "password": "admin1@",
        "is_admin": True
    },
    {
        "name": "Admin2",
        "username": "admin2123",
        "password": "admin2@",
        "is_admin": True
    }

    ]

def create_users():
    for user in users_list:
        User.objects.create(name=user["name"],
                           username=user["username"],
                           password=user["password"],
                           is_admin=user["is_admin"])



account_list = [
    {
        "upi_id": "1234567890@SBI"
    }
]

def create_account():
    for account in account_list:
        Account.objects.create(upi_id=account["upi_id"])




def populate_data():

    create_users()
    print("users created")
    create_account()
    print("accounts created")

    for form in new_forms_list:
        form_obj = Form.objects.create(name=form["name"], status=form["status"],
                                       description=form["description"],
                                       close_date=form["close_date"],
                                       expected_delivery_date=form["expected_delivery_date"])

        for section in form["sections"]:
            section_obj = Section.objects.create(name=section["name"],
                                                 description=section["description"])
            form_obj.sections.add(section_obj)

            for item in section["items"]:
                item_obj = Item.objects.create(name=item["name"],
                                               description=item["description"])
                section_obj.items.add(item_obj)

                for brand in item["brands"]:
                    brand_obj = Brand.objects.create(name=brand["name"],
                                                     min_quantity=brand["min_quantity"],
                                                     max_quantity=brand["max_quantity"],
                                                     price_per_item=brand["price_per_item"])
                    item_obj.brand.add(brand_obj)


    print("forms data created")
    create_transactions()
    print("transactions  created")
    

    create_orders()
    print("orders created")
    print("data populated successfully Hurrah!.......")


def create_orders():
    for order in new_orders_list:
        Order.objects.create(
              user_id=order["user_id"],
              item_id=order["item_id"],
              brand_id=order["brand_id"],
              form_id=order["form_id"],
              section_id=order["section_id"],
              count=order["count"],
              pending_count=order["pending_count"],
              out_of_stock=order["out_of_stock"]
        )



transaction_list = [
    # user 1 transactions
    {
        "transaction_id": 1,
        "user_id": 1,
        "amount": 1000,
        "status": "APPROVED",
        "payment_type": "PHONE_PAY",
        "screen_shot": "screen_shot/payment.png",
        "remark": "wallet"
    },
    {
        "transaction_id": 2,
        "user_id": 1,
        "amount": 300,
        "status": "APPROVED",
        "payment_type": "GOOGLE_PAY",
        "screen_shot": "screen_shot/payment.png",
        "remark": "wallet"
    },
    {
        "transaction_id": 3,
        "user_id": 1,
        "amount": -100,
        "status": "APPROVED",
        "payment_type": "PHONE_PAY",
        "screen_shot": "",
        "remark": "form1"
    },
    {
        "transaction_id": 4,
        "user_id": 1,
        "amount": -600,
        "status": "APPROVED",
        "payment_type": "PHONE_PAY",
        "screen_shot": "screen_shot/payment.png",
        "remark": "form2"
    },
    {
        "transaction_id": 5,
        "user_id": 1,
        "amount": 700,
        "status": "PENDING",
        "payment_type": "PHONE_PAY",
        "screen_shot": "screen_shot/payment.png",
        "remark": "wallet"
    },
     {
        "transaction_id": 6,
        "user_id": 1,
        "amount": 500,
        "status": "PENDING",
        "payment_type": "GOOGLE_PAY",
        "screen_shot": "screen_shot/payment.png",
        "remark": "wallet"
    },
     {
        "transaction_id": 7,
        "user_id": 1,
        "amount": 1000,
        "status": "REJECTED",
        "payment_type": "PHONE_PAY",
        "screen_shot": "screen_shot/payment.png",
        "remark": "wallet"
    },
    {
        "transaction_id": 8,
        "user_id": 1,
        "amount": 700,
        "status": "REJECTED",
        "payment_type": "PAYTM",
        "screen_shot": "screen_shot/payment.png",
        "remark": "wallet"
    },
# user 2 transactions
    {
        "transaction_id": 9,
        "user_id": 2,
        "amount": 900,
        "status": "APPROVED",
        "payment_type": "PHONE_PAY",
        "screen_shot": "screen_shot/payment.png",
        "remark": "wallet"
    },
    {
        "transaction_id": 10,
        "user_id": 2,
        "amount": 600,
        "status": "APPROVED",
        "payment_type": "GOOGLE_PAY",
        "screen_shot": "screen_shot/payment.png",
        "remark": "wallet"
    },
    {
        "transaction_id": 11,
        "user_id": 2,
        "amount": -400,
        "status": "APPROVED",
        "payment_type": "PHONE_PAY",
        "screen_shot": "",
        "remark": "form1"
    },
    {
        "transaction_id": 12,
        "user_id": 2,
        "amount": -300,
        "status": "APPROVED",
        "payment_type": "PHONE_PAY",
        "screen_shot": "screen_shot/payment.png",
        "remark": "form2"
    },
    {
        "transaction_id": 13,
        "user_id": 2,
        "amount": 700,
        "status": "PENDING",
        "payment_type": "PHONE_PAY",
        "screen_shot": "screen_shot/payment.png",
        "remark": "wallet"
    },
     {
        "transaction_id": 14,
        "user_id": 2,
        "amount": 500,
        "status": "PENDING",
        "payment_type": "GOOGLE_PAY",
        "screen_shot": "screen_shot/payment.png",
        "remark": "wallet"
    },
     {
        "transaction_id": 15,
        "user_id": 2,
        "amount": 900,
        "status": "REJECTED",
        "payment_type": "PHONE_PAY",
        "screen_shot": "screen_shot/payment.png",
        "remark": "wallet"
    },
    {
        "transaction_id": 16,
        "user_id": 2,
        "amount": 700,
        "status": "REJECTED",
        "payment_type": "PAYTM",
        "screen_shot": "screen_shot/payment.png",
        "remark": "wallet"
    },

# user 3 transactions
    {
        "transaction_id": 17,
        "user_id": 3,
        "amount": 1100,
        "status": "APPROVED",
        "payment_type": "PHONE_PAY",
        "screen_shot": "screen_shot/payment.png",
        "remark": "wallet"
    },
    {
        "transaction_id": 18,
        "user_id": 3,
        "amount": 200,
        "status": "APPROVED",
        "payment_type": "GOOGLE_PAY",
        "screen_shot": "screen_shot/payment.png",
        "remark": "wallet"
    },
    {
        "transaction_id": 19,
        "user_id": 3,
        "amount": -300,
        "status": "APPROVED",
        "payment_type": "PHONE_PAY",
        "screen_shot": "",
        "remark": "form1"
    },
    {
        "transaction_id": 20,
        "user_id": 3,
        "amount": -400,
        "status": "APPROVED",
        "payment_type": "PHONE_PAY",
        "screen_shot": "screen_shot/payment.png",
        "remark": "form2"
    },
    {
        "transaction_id": 21,
        "user_id": 3,
        "amount": 800,
        "status": "PENDING",
        "payment_type": "PHONE_PAY",
        "screen_shot": "screen_shot/payment.png",
        "remark": "wallet"
    },
     {
        "transaction_id": 22,
        "user_id": 3,
        "amount": 500,
        "status": "PENDING",
        "payment_type": "GOOGLE_PAY",
        "screen_shot": "screen_shot/payment.png",
        "remark": "wallet"
    },
     {
        "transaction_id": 23,
        "user_id": 3,
        "amount": 800,
        "status": "REJECTED",
        "payment_type": "PHONE_PAY",
        "screen_shot": "screen_shot/payment.png",
        "remark": "wallet"
    },
    {
        "transaction_id": 24,
        "user_id": 3,
        "amount": 700,
        "status": "REJECTED",
        "payment_type": "PAYTM",
        "screen_shot": "screen_shot/payment.png",
        "remark": "wallet"
    }



]


def create_transactions():

    for transaction in transaction_list:
        Transaction.objects.create(
            transaction_id=transaction['transaction_id'],
            user_id=transaction['user_id'],
            amount=transaction['amount'],
            status=transaction['status'],
            payment_type=transaction["payment_type"],
            screen_shot=transaction["screen_shot"],
            remark=transaction["remark"])




new_forms_list = [
    {
        "name": "Snack form 1",
        "description": "Snack form 1  description",
        "close_date": datetime.datetime(2020, 6, 1, 0, 0, 0),
        "expected_delivery_date": datetime.datetime(2020, 6, 10, 0, 0, 0),
        "status": "LIVE",
        "sections": [
            {
                "name": "Chocolates", "description": "Chocolates description",
                "items": [
                    {
                        "name": "Cadbury", "description": "description",
                        "brands": [
                            {
                                "name": "brand1", "min_quantity": 0, 
                                "max_quantity": 10, "price_per_item": 50
                            },
                            {
                                "name": "brand2", "min_quantity": 0,
                                "max_quantity": 8, "price_per_item": 60
                            },
                            {
                                "name": "brand3", "min_quantity": 0,
                                "max_quantity": 9, "price_per_item": 70
                            }
                            
                            ]
                    },
                    {
                        "name": "Diary milk silk", "description": "description",
                        "brands": [
                            {
                                "name": "brand4", "min_quantity": 0, 
                                "max_quantity": 10, "price_per_item": 40
                            },
                            {
                                "name": "brand5", "min_quantity": 0,
                                "max_quantity": 5, "price_per_item": 80
                            },
                            {
                                "name": "brand6", "min_quantity": 0,
                                "max_quantity": 6, "price_per_item": 50
                            }
                            
                            ]
                    }
                        ]
            },
            {
                "name": "Chips",
                "description": "Chips description",
                "items": [
                    {
                        "name": "Lays",
                        "description": "description",
                        "brands": [
                            {
                                "name": "brand7", "min_quantity": 0, 
                                "max_quantity": 20, "price_per_item": 80
                            },
                            {
                                "name": "brand8", "min_quantity": 0,
                                "max_quantity": 8, "price_per_item": 90
                            },
                            {
                                "name": "brand9", "min_quantity": 0,
                                "max_quantity": 7, "price_per_item": 50
                            }
                            
                            ]
                    },
                    {
                        "name": "Bingo",
                        "description": " description",
                        "brands": [
                            {
                                "name": "brand10", "min_quantity": 0, 
                                "max_quantity": 5, "price_per_item": 100
                            },
                            {
                                "name": "brand11", "min_quantity": 0,
                                "max_quantity": 5, "price_per_item": 200
                            },
                            {
                                "name": "brand12", "min_quantity": 0,
                                "max_quantity": 6, "price_per_item": 50
                            }
                            
                            ]
                    }
                    
                    ]
            }
            ]
    },
    {
        "name": "Accommodation",
        "description": "description",
        "close_date": datetime.datetime(2020, 6, 1, 0, 0, 0),
        "expected_delivery_date": datetime.datetime(2020, 6, 6, 0, 0, 0),
        "status": "CLOSED",
        "sections": [
            {
                "name": "Shampoos", "description": "Shampoos description",
                "items": [
                    {
                        "name": "Tresemme", "description": "Tresemme description",
                        "brands": [
                            {
                                "name": "brand13", "min_quantity": 0, 
                                "max_quantity": 5, "price_per_item": 100
                            },
                            {
                                "name": "brand14", "min_quantity": 0,
                                "max_quantity": 8, "price_per_item": 150
                            },
                            {
                                "name": "brand15", "min_quantity": 0,
                                "max_quantity": 7, "price_per_item": 50
                            }
                            
                            ]
                    },
                    {
                        "name": "Dove", "description": "Dove description",
                        "brands": [
                            {
                                "name": "brand16", "min_quantity": 0, 
                                "max_quantity": 5, "price_per_item": 100
                            },
                            {
                                "name": "brand17", "min_quantity": 0,
                                "max_quantity": 8, "price_per_item": 150
                            },
                            {
                                "name": "brand18", "min_quantity": 0,
                                "max_quantity": 6, "price_per_item": 50
                            }
                            
                            ]
                    }
                        ]
            }, 
            {
                "name": "Hair oil",
                "description": "Hair oil description",
                "items": [
                    {
                        "name": "Coconut oil",
                        "description": "Coconut oil description",
                        "brands": [
                            {
                                "name": "brand19", "min_quantity": 0, 
                                "max_quantity": 5, "price_per_item": 100
                            },
                            {
                                "name": "brand20", "min_quantity": 0,
                                "max_quantity": 8, "price_per_item": 150
                            },
                            {
                                "name": "brand21", "min_quantity": 0,
                                "max_quantity": 7, "price_per_item": 50
                            }
                            
                            ]
                    },
                    {
                        "name": "indulekha",
                        "description": "indulekha description",
                        "brands": [
                            {
                                "name": "brand22", "min_quantity": 0, 
                                "max_quantity": 5, "price_per_item": 100
                            },
                            {
                                "name": "brand23", "min_quantity": 0,
                                "max_quantity": 5, "price_per_item": 150
                            },
                            {
                                "name": "brand24", "min_quantity": 0,
                                "max_quantity": 6, "price_per_item": 50
                            }
                            
                            ]
                    }
                    
                    ]
            }
            ]
    },
    # form3
    {
        "name": "Fruits form",
        "description": "Fruits form description",
        "close_date": datetime.datetime(2020, 5, 10, 0, 0, 0),
        "expected_delivery_date": datetime.datetime(2020, 5, 20, 0, 0, 0),
        "status": "DONE",
        "sections": [
            {
                "name": "section5", "description": "section5 description",
                "items": [
                    {
                        "name": "Apples", "description": "Apples description",
                        "brands": [
                            {
                                "name": "brand25", "min_quantity": 0, 
                                "max_quantity": 5, "price_per_item": 100
                            },
                            {
                                "name": "brand26", "min_quantity": 0,
                                "max_quantity": 8, "price_per_item": 200
                            },
                            {
                                "name": "brand27", "min_quantity": 0,
                                "max_quantity": 7, "price_per_item": 50
                            }
                            
                            ]
                    },
                    {
                        "name": "Mango", "description": "Mango description",
                        "brands": [
                            {
                                "name": "brand28", "min_quantity": 0, 
                                "max_quantity": 5, "price_per_item": 100
                            },
                            {
                                "name": "brand29", "min_quantity": 0,
                                "max_quantity": 5, "price_per_item": 200
                            },
                            {
                                "name": "brand30", "min_quantity": 0,
                                "max_quantity": 6, "price_per_item": 50
                            }
                            
                            ]
                    }
                        ]
            },
            {
                "name": "section6",
                "description": "section6 description",
                "items": [
                    {
                        "name": "Oranges",
                        "description": "Oranges description",
                        "brands": [
                            {
                                "name": "brand31", "min_quantity": 0, 
                                "max_quantity": 5, "price_per_item": 100
                            },
                            {
                                "name": "brand32", "min_quantity": 0,
                                "max_quantity": 8, "price_per_item": 200
                            },
                            {
                                "name": "brand33", "min_quantity": 0,
                                "max_quantity": 7, "price_per_item": 50
                            }
                            
                            ]
                    },
                    {
                        "name": "grapes",
                        "description": "grapes description",
                        "brands": [
                            {
                                "name": "brand34", "min_quantity": 0, 
                                "max_quantity": 5, "price_per_item": 100
                            },
                            {
                                "name": "brand35", "min_quantity": 0,
                                "max_quantity": 5, "price_per_item": 200
                            },
                            {
                                "name": "brand36", "min_quantity": 0,
                                "max_quantity": 6, "price_per_item": 50
                            }
                            
                            ]
                    }
                    
                    ]
            }
            ]
    },
    {
        "name": "form4",
        "description": "form4 description",
        "close_date": datetime.datetime(2020, 5, 25, 0, 0, 0),
        "expected_delivery_date": datetime.datetime(2020, 6, 1, 0, 0, 0),
        "status": "LIVE",
        "sections": [
            {
                "name": "section7", "description": "section7 description",
                "items": [
                    {
                        "name": "item13", "description": "item13 description",
                        "brands": [
                            {
                                "name": "brand37", "min_quantity": 0, 
                                "max_quantity": 5, "price_per_item": 100
                            },
                            {
                                "name": "brand38", "min_quantity": 0,
                                "max_quantity": 8, "price_per_item": 200
                            },
                            {
                                "name": "brand39", "min_quantity": 0,
                                "max_quantity": 7, "price_per_item": 50
                            }
                            
                            ]
                    },
                    {
                        "name": "item14", "description": "item14 description",
                        "brands": [
                            {
                                "name": "brand40", "min_quantity": 0, 
                                "max_quantity": 5, "price_per_item": 100
                            },
                            {
                                "name": "brand41", "min_quantity": 0,
                                "max_quantity": 5, "price_per_item": 200
                            },
                            {
                                "name": "brand142", "min_quantity": 0,
                                "max_quantity": 6, "price_per_item": 50
                            }
                            
                            ]
                    }
                        ]
            },
            {
                "name": "section8",
                "description": "section8 description",
                "items": [
                    {
                        "name": "item15",
                        "description": "item15 description",
                        "brands": [
                            {
                                "name": "brand43", "min_quantity": 1, 
                                "max_quantity": 5, "price_per_item": 100
                            },
                            {
                                "name": "brand44", "min_quantity": 2,
                                "max_quantity": 8, "price_per_item": 200
                            },
                            {
                                "name": "brand45", "min_quantity": 5,
                                "max_quantity": 7, "price_per_item": 50
                            }
                            
                            ]
                    },
                    {
                        "name": "item16",
                        "description": "item16 description",
                        "brands": [
                            {
                                "name": "brand146", "min_quantity": 1, 
                                "max_quantity": 5, "price_per_item": 100
                            },
                            {
                                "name": "brand47", "min_quantity": 2,
                                "max_quantity": 5, "price_per_item": 200
                            },
                            {
                                "name": "brand48", "min_quantity": 2,
                                "max_quantity": 6, "price_per_item": 50
                            }
                            
                            ]
                    }
                    
                    ]
            }
            ]
    },

    {
        "name": "form5",
        "description": "form5 description",
        "close_date": datetime.datetime(2020, 6, 3, 0, 0, 0),
        "expected_delivery_date": datetime.datetime(2020, 6, 6, 0, 0, 0),
        "status": "LIVE",
        "sections": [
            {
                "name": "section9", "description": "section9 description",
                "items": [
                    {
                        "name": "item17", "description": "item17 description",
                        "brands": [
                            {
                                "name": "brand50", "min_quantity": 0, 
                                "max_quantity": 5, "price_per_item": 100
                            },
                            {
                                "name": "brand51", "min_quantity": 0,
                                "max_quantity": 8, "price_per_item": 200
                            },
                            {
                                "name": "brand52", "min_quantity": 0,
                                "max_quantity": 7, "price_per_item": 50
                            }
                            
                            ]
                    },
                    {
                        "name": "item118", "description": "item18 description",
                        "brands": [
                            {
                                "name": "brand53", "min_quantity": 0, 
                                "max_quantity": 5, "price_per_item": 100
                            },
                            {
                                "name": "brand54", "min_quantity": 0,
                                "max_quantity": 5, "price_per_item": 200
                            },
                            {
                                "name": "brand55", "min_quantity": 0,
                                "max_quantity": 6, "price_per_item": 50
                            }
                            
                            ]
                    }
                        ]
            },
            {
                "name": "section10",
                "description": "section10 description",
                "items": [
                    {
                        "name": "item19",
                        "description": "item19 description",
                        "brands": [
                            {
                                "name": "brand56", "min_quantity": 1, 
                                "max_quantity": 5, "price_per_item": 100
                            },
                            {
                                "name": "brand57", "min_quantity": 2,
                                "max_quantity": 8, "price_per_item": 200
                            },
                            {
                                "name": "brand58", "min_quantity": 5,
                                "max_quantity": 7, "price_per_item": 50
                            }
                            
                            ]
                    },
                    {
                        "name": "item20",
                        "description": "item20 description",
                        "brands": [
                            {
                                "name": "brand159", "min_quantity": 1, 
                                "max_quantity": 5, "price_per_item": 100
                            },
                            {
                                "name": "brand60", "min_quantity": 2,
                                "max_quantity": 5, "price_per_item": 200
                            },
                            {
                                "name": "brand61", "min_quantity": 2,
                                "max_quantity": 6, "price_per_item": 50
                            }
                            
                            ]
                    }
                    
                    ]
            }
            ]
    },
    {
        "name": "form6",
        "description": "form6 description",
        "close_date": datetime.datetime(2020, 5, 10, 0, 0, 0),
        "expected_delivery_date": datetime.datetime(2020, 5, 11, 0, 0, 0),
        "status": "CLOSED",
        "sections": [
            {
                "name": "section21", "description": "section21 description",
                "items": [
                    {
                        "name": "item13", "description": "item13 description",
                        "brands": [
                            {
                                "name": "brand62", "min_quantity": 0, 
                                "max_quantity": 5, "price_per_item": 100
                            },
                            {
                                "name": "brand63", "min_quantity": 0,
                                "max_quantity": 8, "price_per_item": 200
                            },
                            {
                                "name": "brand64", "min_quantity": 0,
                                "max_quantity": 7, "price_per_item": 50
                            }
                            
                            ]
                    },
                    {
                        "name": "item22", "description": "item22 description",
                        "brands": [
                            {
                                "name": "brand65", "min_quantity": 0, 
                                "max_quantity": 5, "price_per_item": 100
                            },
                            {
                                "name": "brand66", "min_quantity": 0,
                                "max_quantity": 5, "price_per_item": 200
                            },
                            {
                                "name": "brand167", "min_quantity": 0,
                                "max_quantity": 6, "price_per_item": 50
                            }
                            
                            ]
                    }
                        ]
            },
            {
                "name": "section12",
                "description": "section12 description",
                "items": [
                    {
                        "name": "item23",
                        "description": "item23 description",
                        "brands": [
                            {
                                "name": "brand68", "min_quantity": 1, 
                                "max_quantity": 5, "price_per_item": 100
                            },
                            {
                                "name": "brand69", "min_quantity": 2,
                                "max_quantity": 8, "price_per_item": 200
                            },
                            {
                                "name": "brand70", "min_quantity": 5,
                                "max_quantity": 7, "price_per_item": 50
                            }
                            
                            ]
                    },
                    {
                        "name": "item24",
                        "description": "item24 description",
                        "brands": [
                            {
                                "name": "brand71", "min_quantity": 1, 
                                "max_quantity": 5, "price_per_item": 100
                            },
                            {
                                "name": "brand72", "min_quantity": 2,
                                "max_quantity": 5, "price_per_item": 200
                            },
                            {
                                "name": "brand73", "min_quantity": 2,
                                "max_quantity": 6, "price_per_item": 50
                            }
                            
                            ]
                    }
                    
                    ]
            }
            ]
    },
    {
        "name": "form7",
        "description": "form7 description",
        "close_date": datetime.datetime(2020, 6, 6, 0, 0, 0),
        "expected_delivery_date": datetime.datetime(2020, 6, 10, 0, 0, 0),
        "status": "LIVE",
        "sections": [
            {
                "name": "section13", "description": "section13 description",
                "items": [
                    {
                        "name": "item25", "description": "item25 description",
                        "brands": [
                            {
                                "name": "brand74", "min_quantity": 0, 
                                "max_quantity": 5, "price_per_item": 100
                            },
                            {
                                "name": "brand75", "min_quantity": 0,
                                "max_quantity": 8, "price_per_item": 200
                            },
                            {
                                "name": "brand76", "min_quantity": 0,
                                "max_quantity": 7, "price_per_item": 50
                            }
                            
                            ]
                    },
                    {
                        "name": "item26", "description": "item26 description",
                        "brands": [
                            {
                                "name": "brand77", "min_quantity": 0, 
                                "max_quantity": 5, "price_per_item": 100
                            },
                            {
                                "name": "brand78", "min_quantity": 0,
                                "max_quantity": 5, "price_per_item": 200
                            },
                            {
                                "name": "brand79", "min_quantity": 0,
                                "max_quantity": 6, "price_per_item": 50
                            }
                            
                            ]
                    }
                        ]
            },
            {
                "name": "section14",
                "description": "section14 description",
                "items": [
                    {
                        "name": "item27",
                        "description": "item27 description",
                        "brands": [
                            {
                                "name": "brand80", "min_quantity": 1, 
                                "max_quantity": 5, "price_per_item": 100
                            },
                            {
                                "name": "brand81", "min_quantity": 2,
                                "max_quantity": 8, "price_per_item": 200
                            },
                            {
                                "name": "brand82", "min_quantity": 5,
                                "max_quantity": 7, "price_per_item": 50
                            }
                            
                            ]
                    },
                    {
                        "name": "item28",
                        "description": "item28 description",
                        "brands": [
                            {
                                "name": "brand83", "min_quantity": 1, 
                                "max_quantity": 5, "price_per_item": 100
                            },
                            {
                                "name": "brand84", "min_quantity": 2,
                                "max_quantity": 5, "price_per_item": 200
                            },
                            {
                                "name": "brand85", "min_quantity": 2,
                                "max_quantity": 6, "price_per_item": 50
                            }
                            
                            ]
                    }
                    
                    ]
            }
            ]
    },
    {
        "name": "form8",
        "description": "form8 description",
        "close_date": datetime.datetime(2020, 4, 4, 0, 0, 0),
        "expected_delivery_date": datetime.datetime(2020, 4, 4, 0, 0, 0),
        "status": "CLOSED",
        "sections": [
            {
                "name": "section15", "description": "section15 description",
                "items": [
                    {
                        "name": "item28", "description": "item28 description",
                        "brands": [
                            {
                                "name": "brand86", "min_quantity": 0, 
                                "max_quantity": 5, "price_per_item": 100
                            },
                            {
                                "name": "brand87", "min_quantity": 0,
                                "max_quantity": 8, "price_per_item": 200
                            },
                            {
                                "name": "brand88", "min_quantity": 0,
                                "max_quantity": 7, "price_per_item": 50
                            }
                            
                            ]
                    },
                    {
                        "name": "item29", "description": "item29 description",
                        "brands": [
                            {
                                "name": "brand89", "min_quantity": 0, 
                                "max_quantity": 5, "price_per_item": 100
                            },
                            {
                                "name": "brand90", "min_quantity": 0,
                                "max_quantity": 5, "price_per_item": 200
                            },
                            {
                                "name": "brand91", "min_quantity": 0,
                                "max_quantity": 6, "price_per_item": 50
                            }
                            
                            ]
                    }
                        ]
            },
            {
                "name": "section16",
                "description": "section16 description",
                "items": [
                    {
                        "name": "item30",
                        "description": "item30 description",
                        "brands": [
                            {
                                "name": "brand92", "min_quantity": 1, 
                                "max_quantity": 5, "price_per_item": 100
                            },
                            {
                                "name": "brand93", "min_quantity": 2,
                                "max_quantity": 8, "price_per_item": 200
                            },
                            {
                                "name": "brand94", "min_quantity": 5,
                                "max_quantity": 7, "price_per_item": 50
                            }
                            
                            ]
                    },
                    {
                        "name": "item31",
                        "description": "item31 description",
                        "brands": [
                            {
                                "name": "brand95", "min_quantity": 1, 
                                "max_quantity": 5, "price_per_item": 100
                            },
                            {
                                "name": "brand96", "min_quantity": 2,
                                "max_quantity": 5, "price_per_item": 200
                            },
                            {
                                "name": "brand97", "min_quantity": 2,
                                "max_quantity": 6, "price_per_item": 50
                            }
                            
                            ]
                    }
                    
                    ]
            }
            ]
    },
    {
        "name": "form9",
        "description": "form9 description",
        "close_date": datetime.datetime(2020, 3, 10, 0, 0, 0),
        "expected_delivery_date": datetime.datetime(2020, 10, 10, 0, 0, 0),
        "status": "LIVE",
        "sections": [
            {
                "name": "section17", "description": "section17 description",
                "items": [
                    {
                        "name": "item32", "description": "item32 description",
                        "brands": [
                            {
                                "name": "brand98", "min_quantity": 0, 
                                "max_quantity": 5, "price_per_item": 100
                            },
                            {
                                "name": "brand99", "min_quantity": 0,
                                "max_quantity": 8, "price_per_item": 50
                            },
                            {
                                "name": "brand100", "min_quantity": 0,
                                "max_quantity": 7, "price_per_item": 50
                            }
                            
                            ]
                    },
                    {
                        "name": "item33", "description": "item33 description",
                        "brands": [
                            {
                                "name": "brand101", "min_quantity": 0, 
                                "max_quantity": 5, "price_per_item": 100
                            },
                            {
                                "name": "brand102", "min_quantity": 0,
                                "max_quantity": 5, "price_per_item": 90
                            },
                            {
                                "name": "brand103", "min_quantity": 0,
                                "max_quantity": 6, "price_per_item": 50
                            }
                            
                            ]
                    }
                        ]
            },
            {
                "name": "section18",
                "description": "section18 description",
                "items": [
                    {
                        "name": "item34",
                        "description": "item34 description",
                        "brands": [
                            {
                                "name": "brand105", "min_quantity": 1, 
                                "max_quantity": 5, "price_per_item": 100
                            },
                            {
                                "name": "brand106", "min_quantity": 2,
                                "max_quantity": 8, "price_per_item": 80
                            },
                            {
                                "name": "brand107", "min_quantity": 5,
                                "max_quantity": 7, "price_per_item": 50
                            }
                            
                            ]
                    },
                    {
                        "name": "item35",
                        "description": "item35 description",
                        "brands": [
                            {
                                "name": "brand108", "min_quantity": 1, 
                                "max_quantity": 5, "price_per_item": 100
                            },
                            {
                                "name": "brand109", "min_quantity": 2,
                                "max_quantity": 5, "price_per_item": 70
                            },
                            {
                                "name": "brand110", "min_quantity": 2,
                                "max_quantity": 6, "price_per_item": 50
                            }
                            
                            ]
                    }
                    
                    ]
            }
            ]
    },

    {
        "name": "form20",
        "description": "form20 description",
        "close_date": datetime.datetime(2020, 11, 8, 0, 0, 0),
        "expected_delivery_date": datetime.datetime(2020, 1, 10, 0, 0, 0),
        "status": "CLOSED",
        "sections": []},
    {
        "name": "form22",
        "description": "form22 description",
        "close_date": datetime.datetime(2020, 10, 8, 0, 0, 0),
        "expected_delivery_date": datetime.datetime(2020, 2, 10, 0, 0, 0),
        "status": "CLOSED",
        "sections": []},
    {
        "name": "form23",
        "description": "form23 description",
        "close_date": datetime.datetime(2020, 10, 8, 0, 0, 0),
        "expected_delivery_date": datetime.datetime(2020, 3, 10, 0, 0, 0),
        "status": "CLOSED",
        "sections": []},
    {
        "name": "form24",
        "description": "form24 description",
        "close_date": datetime.datetime(2020, 10, 8, 0, 0, 0),
        "expected_delivery_date": datetime.datetime(2020, 5, 3, 0, 0, 0),
        "status": "CLOSED",
        "sections": []
    },
    {
        "name": "form25",
        "description": "form25 description",
        "close_date": datetime.datetime(2020, 1, 8, 0, 0, 0),
        "expected_delivery_date": datetime.datetime(2020, 1, 9, 0, 0, 0),
        "status": "CLOSED",
        "sections": []
    },
    {
        "name": "form26",
        "description": "form26 description",
        "close_date": datetime.datetime(2020, 10, 8, 0, 0, 0),
        "expected_delivery_date": datetime.datetime(2020, 10, 10, 0, 0, 0),
        "status": "CLOSED",
        "sections": []},
    {
        "name": "form27",
        "description": "form27 description",
        "close_date": datetime.datetime(2019, 10, 8, 0, 0, 0),
        "expected_delivery_date": datetime.datetime(2019, 10, 10, 0, 0, 0),
        "status": "CLOSED",
        "sections": []
    },
    {
        "name": "form28",
        "description": "form28 description",
        "close_date": datetime.datetime(2019, 10, 8, 0, 0, 0),
        "expected_delivery_date": datetime.datetime(2019, 10, 10, 0, 0, 0),
        "status": "CLOSED",
        "sections": []
    },
    {
        "name": "form29",
        "description": "form29 description",
        "close_date": datetime.datetime(2019, 10, 8, 0, 0, 0),
        "expected_delivery_date": datetime.datetime(2019, 10, 10, 0, 0, 0),
        "status": "CLOSED",
        "sections": []},
    {
        "name": "form30",
        "description": "form30 description",
        "close_date": datetime.datetime(2019, 10, 8, 0, 0, 0),
        "expected_delivery_date": datetime.datetime(2019, 10, 10, 0, 0, 0),
        "status": "CLOSED",
        "sections": []
    },

    ]



new_orders_list = [
# user 1 order live
    {   
        "user_id":1,
        "form_id": 1,
        "section_id":1,
        "item_id": 1,
        "brand_id": 1,
        "count": 7,
        "pending_count": 0,
        "out_of_stock": 0
     },
    {   
        "user_id":1,
        "form_id": 1,
        "section_id":2,
        "item_id": 3,
        "brand_id": 7,
        "count": 10,
        "pending_count": 0,
        "out_of_stock": 0
     },
     {   
        "user_id":1,
        "form_id": 1,
        "section_id": 1,
        "item_id": 2,
        "brand_id": 4,
        "count": 5,
        "pending_count": 0,
        "out_of_stock": 0
     },

     {   
        "user_id":1,
        "form_id": 2,
        "section_id": 3,
        "item_id": 5,
        "brand_id": 13,
        "count": 3,
        "pending_count": 3,
        "out_of_stock": 0
     },
    {   
        "user_id":1,
        "form_id": 2,
        "section_id": 3,
        "item_id": 6,
        "brand_id": 16,
        "count": 7,
        "pending_count": 0,
        "out_of_stock": 0
     },
     {   
        "user_id": 1,
        "form_id": 2,
        "section_id": 4,
        "item_id": 7,
        "brand_id": 18,
        "count": 6,
        "pending_count": 3,
        "out_of_stock": 0
     },
     {   
        "user_id": 1,
        "form_id": 2,
        "section_id": 4,
        "item_id": 8,
        "brand_id": 24,
        "count": 3,
        "pending_count": 0,
        "out_of_stock": 0
     },
# done form done
    {   
        "user_id": 1,
        "form_id": 3,
        "section_id": 5,
        "item_id": 9,
        "brand_id": 25,
        "count": 3,
        "pending_count": 0,
        "out_of_stock": 0
     },
     {   
        "user_id": 1,
        "form_id": 3,
        "section_id": 5,
        "item_id": 10,
        "brand_id": 29,
        "count": 3,
        "pending_count": 0,
        "out_of_stock": 0
     },
     {   
        "user_id": 1,
        "form_id": 3,
        "section_id": 6,
        "item_id": 11,
        "brand_id": 32,
        "count": 4,
        "pending_count": 0,
        "out_of_stock": 0
     },
     {   
        "user_id": 1,
        "form_id": 3,
        "section_id": 6,
        "item_id": 12,
        "brand_id": 35,
        "count": 5,
        "pending_count": 0,
        "out_of_stock": 0
     },


# user 2 order live
    {   
        "user_id": 2,
        "form_id": 1,
        "section_id":1,
        "item_id": 1,
        "brand_id": 1,
        "count": 7,
        "pending_count": 0,
        "out_of_stock": 0
     },
    {   
        "user_id": 2,
        "form_id": 1,
        "section_id":2,
        "item_id": 3,
        "brand_id": 7,
        "count": 10,
        "pending_count": 0,
        "out_of_stock": 0
     },
     {   
        "user_id": 2,
        "form_id": 1,
        "section_id": 1,
        "item_id": 2,
        "brand_id": 4,
        "count": 5,
        "pending_count": 0,
        "out_of_stock": 0
     },
# closed form
     {   
        "user_id": 2,
        "form_id": 2,
        "section_id": 3,
        "item_id": 5,
        "brand_id": 13,
        "count": 3,
        "pending_count": 3,
        "out_of_stock": 0
     },
    {   
        "user_id": 2,
        "form_id": 2,
        "section_id": 3,
        "item_id": 6,
        "brand_id": 16,
        "count": 7,
        "pending_count": 0,
        "out_of_stock": 0
     },
     {   
        "user_id": 2,
        "form_id": 2,
        "section_id": 4,
        "item_id": 7,
        "brand_id": 18,
        "count": 6,
        "pending_count": 3,
        "out_of_stock": 0
     },
     {   
        "user_id": 2,
        "form_id": 2,
        "section_id": 4,
        "item_id": 8,
        "brand_id": 24,
        "count": 3,
        "pending_count": 0,
        "out_of_stock": 0
     },
# done form done
    {   
        "user_id": 2,
        "form_id": 3,
        "section_id": 5,
        "item_id": 9,
        "brand_id": 25,
        "count": 3,
        "pending_count": 0,
        "out_of_stock": 0
     },
     {   
        "user_id": 2,
        "form_id": 3,
        "section_id": 5,
        "item_id": 10,
        "brand_id": 29,
        "count": 3,
        "pending_count": 0,
        "out_of_stock": 0
     },
     {   
        "user_id": 2,
        "form_id": 3,
        "section_id": 6,
        "item_id": 11,
        "brand_id": 32,
        "count": 4,
        "pending_count": 0,
        "out_of_stock": 0
     },
     {   
        "user_id": 2,
        "form_id": 3,
        "section_id": 6,
        "item_id": 12,
        "brand_id": 35,
        "count": 5,
        "pending_count": 0,
        "out_of_stock": 0
     },

# user 3 order live
    {   
        "user_id": 3,
        "form_id": 1,
        "section_id":1,
        "item_id": 1,
        "brand_id": 1,
        "count": 7,
        "pending_count": 0,
        "out_of_stock": 0
     },
    {   
        "user_id": 3,
        "form_id": 1,
        "section_id":2,
        "item_id": 3,
        "brand_id": 7,
        "count": 10,
        "pending_count": 0,
        "out_of_stock": 0
     },
     {   
        "user_id": 3,
        "form_id": 1,
        "section_id": 1,
        "item_id": 2,
        "brand_id": 4,
        "count": 5,
        "pending_count": 0,
        "out_of_stock": 0
     },
# closed form
     {   
        "user_id": 3,
        "form_id": 2,
        "section_id": 3,
        "item_id": 5,
        "brand_id": 13,
        "count": 3,
        "pending_count": 3,
        "out_of_stock": 0
     },
    {   
        "user_id": 3,
        "form_id": 2,
        "section_id": 3,
        "item_id": 6,
        "brand_id": 16,
        "count": 7,
        "pending_count": 0,
        "out_of_stock": 0
     },
     {   
        "user_id": 3,
        "form_id": 2,
        "section_id": 4,
        "item_id": 7,
        "brand_id": 18,
        "count": 6,
        "pending_count": 3,
        "out_of_stock": 0
     },
     {   
        "user_id": 3,
        "form_id": 2,
        "section_id": 4,
        "item_id": 8,
        "brand_id": 24,
        "count": 3,
        "pending_count": 0,
        "out_of_stock": 0
     },
# done form done
    {   
        "user_id": 3,
        "form_id": 3,
        "section_id": 5,
        "item_id": 9,
        "brand_id": 25,
        "count": 3,
        "pending_count": 0,
        "out_of_stock": 0
     },
     {   
        "user_id": 3,
        "form_id": 3,
        "section_id": 5,
        "item_id": 10,
        "brand_id": 29,
        "count": 3,
        "pending_count": 0,
        "out_of_stock": 0
     },
     {   
        "user_id": 3,
        "form_id": 3,
        "section_id": 6,
        "item_id": 11,
        "brand_id": 32,
        "count": 4,
        "pending_count": 0,
        "out_of_stock": 0
     },
     {   
        "user_id": 3,
        "form_id": 3,
        "section_id": 6,
        "item_id": 12,
        "brand_id": 35,
        "count": 5,
        "pending_count": 0,
        "out_of_stock": 0
     }


    ]
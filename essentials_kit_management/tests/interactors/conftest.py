import datetime

import pytest

from essentials_kit_management.constants.enums import (
    TransactionStatusEnum, TransactionTypeEnum
    
    )

from essentials_kit_management.interactors.storages.dtos import (
    UserDto, BrandDto, ItemDto, SectionDto, FormDto, OrderDto,
    HomePageFormDto, GetFormBrandDto, GetFormSectionDto, GetFormItemDto,
    GetFormDto, GetSectionItemDto, GetFormItemOrderDto, UpdateFormNewOrderDto,
    UpdateFormOrderDto, GetUserOrderDto, GetUserItemDto, TransactionDto,
    GetUserTransactionDto, GetMyWalletDto, GetFormItemDtoWithSectionId,
    GetFormBrandDtoWithItemId
    
    )


@pytest.fixture()
def user_dtos():
    user_dtos = [
        UserDto(user_id=1,
                name="sulthan",
                username="123445678",
                password="sulthan@123"),
        UserDto(user_id=2,
                name="anju",
                username="123445671",
                password="anju@123")
        ]
    return user_dtos


@pytest.fixture()
def brand_dtos():
    brand_dtos = [
        BrandDto(brand_id=1,
                 name="HoneyBee",
                 min_quantity=2,
                 max_quantity=10,
                 price_per_item=100),
        BrandDto(brand_id=2,
                 name="KnockOut",
                 min_quantity=2,
                 max_quantity=11,
                 price_per_item=200)
        ]
    return brand_dtos


@pytest.fixture()
def items_dtos():
    items_dtos = [
        ItemDto(item_id=1,
                name="Choco",
                description="choco"),
        ItemDto(item_id=2,
                name="lace",
                description="lace")
        ]
    return items_dtos

@pytest.fixture()
def order_dtos():
    order_dtos = [
        OrderDto(order_id=1,
                 user_id=1,
                 item_id=1,
                 brand_id=1,
                 form_id=1,
                 section_id=1,
                 count=10,
                 pending_count=0,
                 out_of_stock=0),
        OrderDto(order_id=2,
                 user_id=2,
                 item_id=2,
                 brand_id=2,
                 form_id=1,
                 section_id=2,
                 count=10,
                 pending_count=5,
                 out_of_stock=0),
        OrderDto(order_id=3,
                 user_id=2,
                 item_id=2,
                 brand_id=2,
                 form_id=2,
                 section_id=2,
                 count=5,
                 pending_count=5,
                 out_of_stock=5)

        ]
    return order_dtos


@pytest.fixture()
def form_dtos():
    form_dtos = [
        FormDto(form_id=1,
                name="FORM1",
                description="FORM1",
                status="LIVE",
                close_date=datetime.datetime(2020,10,10,0,0),
                expected_delivery_date=datetime.datetime(2020,10,10,0,0)),
        FormDto(form_id=2,
                name="FORM2",
                description="FORM2",
                status="CLOSED",
                close_date=datetime.datetime(2020,10,10,0,0),
                expected_delivery_date=datetime.datetime(2020,10,10,0,0)),
        FormDto(form_id=3,
                name="FORM3",
                description="FORM3",
                status="LIVE",
                close_date=datetime.datetime(2020,10,10,0,0),
                expected_delivery_date=datetime.datetime(2020,10,10,0,0))

        ]
    return form_dtos


@pytest.fixture()
def get_expected_form_dtos():
    home_page_form_dtos = [
        HomePageFormDto(form_id=1,
                        name="FORM1",
                        status="LIVE",
                        close_date=datetime.datetime(2020,10,10,0,0),
                        expected_delivery_date=datetime.datetime(
                            2020,10,10,0,0),
                        items_count=20,
                        estimated_cost=3000,
                        items_pending_count=5,
                        cost_incurred_for_delivery=2000),
        HomePageFormDto(form_id=2,
                        name="FORM2",
                        status="CLOSED",
                        close_date=datetime.datetime(2020,10,10,0,0),
                        expected_delivery_date=datetime.datetime(
                            2020,10,10,0,0),
                        items_count=5,
                        estimated_cost=1000,
                        items_pending_count=5,
                        cost_incurred_for_delivery=0),
        HomePageFormDto(form_id=3,
                        name="FORM3",
                        status="LIVE",
                        close_date=datetime.datetime(2020,10,10,0,0),
                        expected_delivery_date=datetime.datetime(
                            2020,10,10,0,0),
                        items_count=0,
                        estimated_cost=0,
                        items_pending_count=0,
                        cost_incurred_for_delivery=0)

        ]
    return home_page_form_dtos



@pytest.fixture()
def get_form_dto():
    form_dto = FormDto(
        form_id=1,
        name="FORM1",
        description="FORM1",
        status="LIVE",
        close_date=datetime.datetime(2020, 10, 10, 0, 0),
        expected_delivery_date=datetime.datetime(2020, 10, 10, 0, 0)
    )
    return form_dto

@pytest.fixture()
def get_form_section_dtos():
    section_dtos = [
        SectionDto(section_id=1,
                   name="SECTION1",
                   description="DESCRIP SECTION1"),
        SectionDto(section_id=2,
                   name="SECTION2",
                   description="DESCRIP SECTION2")
           ]
    return section_dtos

@pytest.fixture()
def get_form_items_dtos():
    items_dtos = [
        GetFormItemDtoWithSectionId(
                item_id=1,
                name="choco",
                description="choco",
                section_id=1),
        GetFormItemDtoWithSectionId(
                item_id=2,
                name="lace",
                description="lace",
                section_id=1)
        ]
    return items_dtos

@pytest.fixture()
def get_form_brand_dtos():
    brand_dtos = [
        GetFormBrandDtoWithItemId(
            brand_id=1,
            name="HoneyBee",
            min_quantity=2,
            max_quantity=10,
            price_per_item=100,
            item_id=1),
        GetFormBrandDtoWithItemId(
            brand_id=2,
            name="KnockOut",
            min_quantity=2,
            max_quantity=11,
            price_per_item=200,
            item_id=1),
        GetFormBrandDtoWithItemId(
            brand_id=3,
            name="KingFisher",
            min_quantity=2,
            max_quantity=11,
            price_per_item=200,
            item_id=2)
        
        ]
    return brand_dtos


@pytest.fixture()
def get_form_order_dtos():
    order_dtos = [
        OrderDto(order_id=1,
                 user_id=1,
                 item_id=1,
                 brand_id=1,
                 form_id=1,
                 section_id=1,
                 count=10,
                 pending_count=0,
                 out_of_stock=0),
        OrderDto(order_id=2,
                 user_id=1,
                 item_id=2,
                 brand_id=3,
                 form_id=1,
                 section_id=1,
                 count=10,
                 pending_count=5,
                 out_of_stock=0)
        ]
    return order_dtos




@pytest.fixture()
def get_form_expected_form_details_dto():

    brand1= GetFormBrandDtoWithItemId(
            brand_id=1,
            name="HoneyBee",
            min_quantity=2,
            max_quantity=10,
            price_per_item=100,
            item_id=1)
    brand2 = GetFormBrandDtoWithItemId(
            brand_id=2,
            name="KnockOut",
            min_quantity=2,
            max_quantity=11,
            price_per_item=200,
            item_id=1)
    brand3 = GetFormBrandDtoWithItemId(
            brand_id=3,
            name="KingFisher",
            min_quantity=2,
            max_quantity=11,
            price_per_item=200,
            item_id=2)
        
    order1 = GetFormItemOrderDto(order_id=1,
                                 brand_id=1,
                                 ordered_count=10,
                                 out_of_stock=0)
    order2 = GetFormItemOrderDto(order_id=2,
                                 brand_id=3,
                                 ordered_count=10,
                                 out_of_stock=0)
    
    item1 = GetFormItemDto(item_id=1,
                           name="choco",
                           description="choco",
                           brands=[brand1, brand2],
                           order=order1)
    item2 = GetFormItemDto(item_id=2,
                           name="lace",
                           description="lace",
                           brands=[brand3],
                           order=order2)

    section1 = GetFormSectionDto(section_id=1,
                                 name="SECTION1",
                                 description="DESCRIP SECTION1",
                                 items=[item1, item2])

    section2 = GetFormSectionDto(section_id=2,
                                 name="SECTION2",
                                 description="DESCRIP SECTION2",
                                 items=[])
    
    get_form_dto = GetFormDto(form_id=1,
                              name="FORM1",
                              close_date=datetime.datetime(2020, 10, 10, 0, 0),
                              sections=[section1, section2])

    return get_form_dto




@pytest.fixture()
def update_form_order_dict():

    form_orders_dict = {
        "form_id": 1,
        "sections": [
            {
                "section_id": 1,
                "order_details": [
                    {
                        "item_id": 1,
                        "order_id": 1,
                        "brand_id": 1,
                        "ordered_count": 2,
                        "out_of_stock": 0
                    },
                    {
                        "item_id": 2,
                        "order_id": 2,
                        "brand_id": 0,
                        "ordered_count": 0,
                        "out_of_stock": 0
                    },
                    ]
            },
            {
                "section_id": 2,
                "order_details": [
                    {
                        "item_id": 3,
                        "order_id": 0,
                        "brand_id": 3,
                        "ordered_count": 2,
                        "out_of_stock": 0
                    },
                    {
                        "item_id": 4,
                        "order_id": 0,
                        "brand_id": 4,
                        "ordered_count": 2,
                        "out_of_stock": 0
                    }
                    ]
            }
            
            ]
    }
    return form_orders_dict



@pytest.fixture()
def expected_update_form_dto_list():

    new_order_details_1 = UpdateFormOrderDto(item_id=3,
                                             order_id=0,
                                             brand_id=3,
                                             ordered_count=2,
                                             out_of_stock=0)
    new_order_details_2 = UpdateFormOrderDto(item_id=4,
                                             order_id=0,
                                             brand_id=4,
                                             ordered_count=2,
                                             out_of_stock=0)
    
    new_order_1 =  UpdateFormNewOrderDto(form_id=1,
                                         section_id=2,
                                         order_details=new_order_details_1)
    
    new_order_2 =  UpdateFormNewOrderDto(form_id=1,
                                         section_id=2,
                                         order_details=new_order_details_2)

    upate_order_details1 = UpdateFormOrderDto(item_id=1,
                                              order_id=1,
                                              brand_id=1,
                                              ordered_count=2,
                                              out_of_stock=0)

    update_order_list = [upate_order_details1]
    new_orders_list = [new_order_1, new_order_2]
    remove_order_list = [2]

    return [update_order_list, new_orders_list, remove_order_list]





@pytest.fixture()
def get_user_brand_dtos():
    brand_dtos = [
        BrandDto(brand_id=1,
                 name="HoneyBee",
                 min_quantity=2,
                 max_quantity=10,
                 price_per_item=100),
        BrandDto(brand_id=2,
                 name="KnockOut",
                 min_quantity=2,
                 max_quantity=11,
                 price_per_item=200),
        BrandDto(brand_id=3,
                 name="KingFisher",
                 min_quantity=2,
                 max_quantity=11,
                 price_per_item=200)

        ]
    return brand_dtos


@pytest.fixture()
def get_user_items_dtos():
    items_dtos = [
        GetUserItemDto(item_id=1,
                       name="choco",
                       description="choco"),
        GetUserItemDto(item_id=2,
                       name="lace",
                       description="lace"),
        GetUserItemDto(item_id=3,
                       name="bingo",
                       description="bingo")
        ]
    return items_dtos

@pytest.fixture()
def get_user_order_dtos():
    order_dtos = [
        OrderDto(order_id=1,
                 user_id=1,
                 item_id=1,
                 brand_id=1,
                 form_id=1,
                 section_id=1,
                 count=10,
                 pending_count=5,
                 out_of_stock=0),
        OrderDto(order_id=2,
                 user_id=1,
                 item_id=2,
                 brand_id=2,
                 form_id=1,
                 section_id=2,
                 count=2,
                 pending_count=0,
                 out_of_stock=0),
        OrderDto(order_id=3,
                 user_id=1,
                 item_id=3,
                 brand_id=3,
                 form_id=1,
                 section_id=2,
                 count=5,
                 pending_count=2,
                 out_of_stock=0)# i have doubt at out of stock 

        ]
    return order_dtos


@pytest.fixture()
def get_expected_get_user_order_dtos():
    
    order1 = GetUserOrderDto(
        item_id=1,
        items_added=10,
        item_name="choco",
        items_recived=5,
        cost_incurred=500,
        out_of_stock=0)

    order2 = GetUserOrderDto(
        item_id=2,
        item_name="lace",
        items_added=2,
        items_recived=5,
        cost_incurred=400,
        out_of_stock=0)
    order3 = GetUserOrderDto(
        item_id=3,
        item_name="bingo",
        items_added=5,
        items_recived=2,
        cost_incurred=600,
        out_of_stock=0)

    return [order1, order2, order3]


@pytest.fixture()
def get_user_transaction_dtos_and_my_wallet_dto():

    transaction_dto1 = TransactionDto(
        transaction_id=1,
        user_id=1,
        amount=1000,
        screen_shot="",
        transaction_type=TransactionTypeEnum.PAYTM.value,
        date=datetime.datetime(2020, 10, 10, 0, 0, 0),
        status=TransactionStatusEnum.APPROVED.value,
        remark="wallet")
    transaction_dto2 = TransactionDto(
        transaction_id=2,
        user_id=1,
        amount=500,
        screen_shot="",
        transaction_type=TransactionTypeEnum.PAYTM.value,
        date=datetime.datetime(2020, 10, 10, 0, 0, 0),
        status=TransactionStatusEnum.PENDING.value,
        remark="wallet")
    transaction_dto3 = TransactionDto(
        transaction_id=3,
        user_id=1,
        amount=-500,
        screen_shot="",
        transaction_type=TransactionTypeEnum.PAYTM.value,
        date=datetime.datetime(2020, 10, 10, 0, 0, 0),
        status=TransactionStatusEnum.APPROVED.value,
        remark="snackform")

    transaction_list = [transaction_dto1,
                        transaction_dto2,
                        transaction_dto3]

    expected_my_wallet = GetMyWalletDto(
        balance=500,
        transaction_dtos=[
            GetUserTransactionDto(
                transaction_id=1,
                amount=1000,
                date=datetime.datetime(2020, 10, 10, 0, 0, 0),
                status=TransactionStatusEnum.APPROVED.value,
                remark="wallet"),
            GetUserTransactionDto(
                transaction_id=2,
                amount=500,
                date=datetime.datetime(2020, 10, 10, 0, 0, 0),
                status=TransactionStatusEnum.PENDING.value,
                remark="wallet"),
            GetUserTransactionDto(
                transaction_id=3,
                amount=-500,
                date=datetime.datetime(2020, 10, 10, 0, 0, 0),
                status=TransactionStatusEnum.APPROVED.value,
                remark="snackform")
            ]
        )

    return [transaction_list, expected_my_wallet]

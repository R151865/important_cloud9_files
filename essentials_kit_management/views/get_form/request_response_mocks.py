


RESPONSE_200_JSON = """
{
    "form_name": "string",
    "form_id": 1,
    "close_date": "string",
    "sections": [
        {
            "section_id": 1,
            "name": "string",
            "description": "string",
            "items_details": [
                {
                    "item_id": 1,
                    "item_name": "string",
                    "description": "string",
                    "brands": [
                        {
                            "brand_id": 1,
                            "brand_name": "string",
                            "min_quantity": 1,
                            "max_quantity": 1,
                            "price_per_item": 1
                        }
                    ],
                    "order": {
                        "order_id": 1,
                        "brand_id": 1,
                        "ordered_count": 1,
                        "out_of_stock": 1
                    }
                }
            ]
        }
    ]
}
"""


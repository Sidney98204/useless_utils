import requests
import json

def pprint(message, body):
    print(f"----------------------------------------{message}----------------------------------------")
    print(json.dumps(json.loads(body), indent=4))

def item_request():
    url = "https://antonio.dev.procurify.xyz/api/v3/ap/items/"

    payload = json.dumps({
    "bill_by_cost": False,
    "cost_allocations": [
        {
        "amount": "0.00",
        "budget": 94,
        "currency": 1
        }
    ],
    "currency": 1,
    "custom_fields": [],
    "description": "an_item_name",
    "packing_slips": [],
    "shipping_amount": None,
    "sku": "",
    "tax_is_inclusive": False,
    "tax": None,
    "unit": "",
    "vendor": 6,
    "quantity": "1",
    "unit_cost": "0.00"
    })
    headers = {
    'Authorization': 'Basic Y2hyaXMuaGFkZmllbGRAZXhhbXBsZS5jb206YXNk',
    'Content-Type': 'application/json'
    }

    items_response = requests.request("POST", url, headers=headers, data=payload, verify=False)

    pprint("ITEMS", items_response.text)
    return items_response.json()["data"]["id"]


def bill_request():
    url = "https://antonio.dev.procurify.xyz/api/v2/ap/bills/"

    payload = json.dumps({
    "items": [],
    "vendor": 6,
    "invoice_number": "",
    "payment_method": 10,
    "payment_terms": "",
    "invoice_date": "2022-08-17",
    "due_date": "2022-08-17",
    "gl_post_date": "2022-08-17",
    "note": "",
    "costs": [],
    "invoice_attachments": [],
    "approval_chain": None,
    "approver": None
    })
    headers = {
    'Authorization': 'Basic Y2hyaXMuaGFkZmllbGRAZXhhbXBsZS5jb206YXNk',
    'Content-Type': 'application/json'
    }

    bill_response = requests.request("POST", url, headers=headers, data=payload, verify=False)

    pprint("BILLS", bill_response.text)

    return bill_response.json()["data"]["id"]

def add_items(bill_id, item_id):

    url = f"https://antonio.dev.procurify.xyz/api/v3/ap/bills/{bill_id}/add-items/"

    payload = json.dumps({
    "items": [
        {
        "id": item_id,
        "quantity": "1.00000000",
        "unit_cost": 0,
        "bill_by_cost": False,
        "total_cost": 0
        }
    ]
    })
    headers = {
    'Authorization': 'Basic Y2hyaXMuaGFkZmllbGRAZXhhbXBsZS5jb206YXNk',
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload, verify=False)

    pprint("ADD_ITEMS", response.text)

def update_bill(bill_id, item_id, status):
    url = f"https://antonio.dev.procurify.xyz/api/v2/ap/bills/{bill_id}/"

    payload = json.dumps({
    "items": [
        {
        "id": item_id,
        "bill_by_cost": False,
        "quantity": "1.00000000",
        "tax": None,
        "shipping_amount": None,
        "tax_amount": 0,
        "tax_is_inclusive": False,
        "total_cost": 11,
        "total_cost_with_tax": 11,
        "unit_cost": 11,
        "packing_slips": [],
        "cost_allocations": [
            {
            "id": 225,
            "budget": 94,
            "object_id": 131,
            "amount": "11.00000000",
            "currency": 1,
            "created_on": "2022-08-17T14:57:39.539617-07:00"
            }
        ],
        "custom_fields": []
        }
    ],
    "vendor": 6,
    "invoice_number": "",
    "payment_method": 10,
    "payment_terms": "",
    "invoice_date": "2022-08-17",
    "due_date": "2022-08-17",
    "gl_post_date": "2022-08-17",
    "note": "",
    "costs": [],
    "invoice_attachments": [],
    "approval_chain": 2,
    "approver": 2,
    "status": status
    })
    headers = {
    'Authorization': 'Basic Y2hyaXMuaGFkZmllbGRAZXhhbXBsZS5jb206YXNk',
    'Content-Type': 'application/json'
    }

    response = requests.request("PUT", url, headers=headers, data=payload, verify=False)

    pprint("UPDATE BILL", response.text)


item_id = item_request()
bill_id = bill_request()
add_items(bill_id, item_id)
update_bill(bill_id, item_id, 0)
update_bill(bill_id, item_id, 1)






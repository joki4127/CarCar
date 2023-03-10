import json
from common.json import ModelEncoder
from .models import Customer, AutomobileVO, SalesPerson, SalesRecord

class CustomerListEncoder(ModelEncoder):
    model = Customer
    properties = ["name", "phone_number", "id"]


class AutomobileVODetailEncoder(ModelEncoder):
    model = AutomobileVO
    properties = ["vin"]

class CustomerDetailEncoder(ModelEncoder):
    model = Customer
    properties = [
        "name",
        "address",
        "phone_number"
    ]

class SalesPersonDetailEncoder(ModelEncoder):
    model = SalesPerson
    properties = [
        "name",
        "employee_id"
    ]

class SalesRecordListEncoder(ModelEncoder):
    model = SalesRecord
    properties = ["price", "id", "automobile", "salesperson", "customer"]

    encoders = {
        "automobile": AutomobileVODetailEncoder(),
        "salesperson": SalesPersonDetailEncoder(),
        "customer": CustomerDetailEncoder()
    }

    # def get_extra_data(self, o):
    #     return {
    #         "automobile": o.automobile.vin,
    #         "salesperson": [o.salesperson.name, o.salesperson.employee_id],
    #         "customer": o.customer.name
    #     }

class SalesRecordDetailEncoder(ModelEncoder):
    model = SalesRecord
    properties = [
        "price",
        "automobile",
        "salesperson",
        "customer"
    ]
    encoders = {
        "automobile": AutomobileVODetailEncoder(),
        "salesperson": SalesPersonDetailEncoder(),
        "customer": CustomerDetailEncoder()
    }
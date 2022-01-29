

from flask import Flask, request, abort
from mock_data import catalog
import json
import random
from config import db
from flask_cors import CORS
from bson import ObjectId


# new instance of Flask class
app = Flask("__name__")
CORS(app) # DANGER... anyone can connect to this server

me = {
            "name": "Eric",
            "last": "Moore",
            "age:": 35,
            "hobbies":[],
            "address":{
                "street": "Evergreen",
                "number": 42,
                "city": "SpringField"

                }
    }


@app.route("/", methods=['GET'])
def home():
    return "Hello from Python"


@app.route("/test")
def any_name():
    return "I'm a test function"


@app.route("/about")
def my_name():
    return (me["name"] + " " + me["last"])


# *******************************************************************************
# ********************************** API ENDPOINTS ******************************
# *******************************************************************************

@app.route("/api/catalog")
def get_catalog():
    cursor = db.products.find({})
    results = []
    for product in cursor:
        product["_id"]= str(product["_id"])
        results.append(product)

    return json.dumps(results)




@app.route("/api/catalog", methods=["post"])
def save_product():
    product = request.get_json()
    print (product)


    #  data validations
    # product has to be 5 c
    # if no title then return error
    if not 'title' in product or len(product["title"]) < 5:
        return abort(400, "Title is required, and should be at least 5 chars long")

    # should be a price
    if not 'price' in product:
        return abort(400, "Price is required")

    # if price is not float and not an int, error
    if not isinstance(product["price"], float) and not isinstance(product["price"], int):
        return abort(400, "Price should be a valid number")
        


    # price should be greater than 0
    if product["price"] <= 0:
        return abort(400, "Price should be greater than 0")



    #save the product in catalog
    db.products. insert_one(product)
    print("----saved----")
    print(product)

    #get string of object id
    product["_id"] = str(product["_id"])

    return json.dumps(product)
 


@app.route("/api/cheapest")
def get_cheapest():
    # find the chepest product on the catalog list
    # 1 - travel the list (catalog) for loop
    # 2 - print the price on the consol
    cursor = db.products.find({})
    cheap = cursor[0]
    for product in cursor:
        if product["price"] < cheap["price"]:
            cheap = product

    cheap["_id"] = str(cheap["_id"])
    #return it as json
    return json.dumps(cheap)



@app.route("/api/product/<id>")
def get_product(id):
    #vaidate id is valid ObjectId
    if(not ObjectId.is_valid(id)):
        return abort(400, "id is not a valid ObjectId")

    # find the product whos _id is equal to id
    result = db.products.find_one({"_id":ObjectId(id)})
    if not result:
        return abort(404) #404 - not Found


    result["_id"] = str(result["_id"])
    
    return json.dumps(result)



#end point to retrieve all products by category
@app.route("/api/catalog/<category>")
def get_by_category(category):
    result=[]
    cursor = db.products.find({"category": category})
    for prod in cursor:
        prod["_id"] = str(prod["_id"])
        result.append(prod)
    return json.dumps(result)


@app.route("/api/categories")
def get_categories():
    result=[]
    for product in catalog:
        cat = product["category"]

        if cat not in result:
            result.append(cat)
        
    return json.dumps(result)
    

    #/api/reports/prodCount
@app.route("/api/reports/prodCount")
def get_products(): 
  count =  len(catalog)
  return json.dumps(count)



@app.route("/api/reports/total")
def get_total():
    total = 0

    for prod in catalog:

        totalProd = prod["price"] * prod["stock"]
        total += totalProd

    return json.dumps(total)

    #/api/report/highestInvestment
@app.route("/api/report/highestInvestment")
def get_highest_investment():
    highest = catalog[0]
    for prod in catalog:

        prod_invest = prod["price"]* prod["stock"]
        high_invest = highest["price"]* highest["stock"]

        if prod_invest > high_invest:
            highest = prod
      

    #return it as json
    return json.dumps(highest)


    ####################################################################################################
    #####################################Coupon codes enpoints##########################################
    ####################################################################################################

    #GET
@app.route("/api/couponCodes")
def get_coupon_codes():
    cursor = db.couponCode.find({})                    
    result = []
    for coupon in cursor:
        coupon["_id"]= str(coupon["_id"])
        result.append(coupon)

    return json.dumps(result)



    #POST /api/coupponCodes
    
@app.route("/api/couponCodes", methods=["POST"])
def save_coupon():
    couponCode = request.get_json()
    print (couponCode)

    if not "code" in couponCode:
        return abort(400, "code is required")

    if not "discount" in couponCode:
        return abort(400, "discount is required")


    db.couponCode.insert_one(couponCode)

    #get string of object id
    couponCode["_id"] = str(couponCode["_id"])

    return json.dumps(couponCode)


    # POST /api/couponCodes  x
# 1 - create the end point   x
# 2 - get the json from the reqs  x
#   - validate (code, discount)
# 3 - save the couponCode to db.couponCodes
# 4 - return the saved object as json
# 5 - test it

@app.route("/api/couponCodes/<code>")
def valid_coupon(code):


    # find the code 
    result = db.couponCode.find_one({"code": code})
    if not result:
        return abort(404) #404 - not Found

    #fix _id
    result["_id"] = str(result["_id"])
    
    #return as json
    return json.dumps(result)


# start the server
app.run(debug=True)
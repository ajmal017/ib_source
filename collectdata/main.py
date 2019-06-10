import os

from peewee import *
from playhouse.db_url import connect
import model.Vendor
from conn.db import *

# Connect to the database URL defined in the environment, falling
# back to a local Sqlite database if no database URL is specified.
# mysql://user:passwd@ip:port/my_db

def main():
    db.connect()

    Vendor.insert({
       Vendor.id:0,
       Vendor.contact_name : "contact_name1",
       Vendor.cost_alert:1001.01,
       Vendor.is_valid:"Y",
       Vendor.need_cost_advance: "N",
       Vendor.tel: "100111123",
       Vendor.vendor_name:"vendor_name"
    }).execute()

    query = Vendor.select()
    for tweet in query:
        # Instead of "tweet.user", we will just get the raw ID value stored
        # in the column.
        print(tweet.id, tweet.vendor_name)

if __name__ == "__main__":
    main()
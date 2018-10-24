import sys
from pymongo import MongoClient
import pprint

from couchbase.bucket import Bucket
from couchbase.n1ql import N1QLQuery

from datetime import datetime

def main():
    mongoUrl = ''
    client = MongoClient(mongoUrl, 27017)
    db = client.sonny
    collection = db.fpresults

    print ('MongoDB Count All:')
    pprint.pprint(collection.count_documents({}))

    d = datetime(2018, 10, 22, 12, 0, 0)
    print ('MongoDB Count for 1 day: ')
    pprint.pprint(collection.find({"created_at": {"$gt": d}}).count())

    couchbaseUrl = 'domain/bucketName'
    bucket_release = Bucket(couchbaseUrl)
    query = N1QLQuery("SELECT COUNT (*) FROM `bot-event-data`")

    # add for fixing "couchbase.exceptions.HTTPError"
    query.cross_bucket = True

    # create primary index for querying
    # bucket.n1ql_query("CREATE PRIMARY INDEX ON `bot-fp-result-data`").execute()
    print ('Couchbase Count All: ')
    for row in bucket_release.n1ql_query(query):
        print(row)

    return 0

if __name__ == '__main__':
    sys.exit(main())
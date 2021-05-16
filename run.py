from base64 import encode
from optparse import OptionParser
from sparql import SparqlUtil
import sys
import io

def make_opt_parser():
    parser = OptionParser()
    parser.add_option('--fe',action='store_true',dest='find_entity')
    parser.add_option('--qe',action='store_true',dest='query_entity')
    parser.add_option('--fr',action='store_true',dest='find_relation')
    parser.add_option('--qr',action='store_true',dest='query_relation')
    parser.add_option('--qo',action='store_true',dest='query_object')
    parser.add_option('--qrber',action='store_true',dest='query_relation_by_er')
    parser.add_option('--qohber',action='store_true',dest='query_onehop_by_er')
    parser.add_option('-l','--limit',action='store',default=10,type=int,dest='limit')
    return parser

if __name__ == '__main__':
    sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
    sparql_util = SparqlUtil()

    parser = make_opt_parser()
    option,args = parser.parse_args()

    result = None
    if option.find_entity == True:
        result = sparql_util.find_entity(args[0])
    elif option.query_entity == True:
        result = sparql_util.query_entity_label(args[0])
    elif option.find_relation == True:
        result = sparql_util.find_relation(args[0],args[1],option.limit)
    elif option.query_relation == True:
        result = sparql_util.query_relation(args[0])
    elif option.query_object == True:
        result = sparql_util.query_object(args[0],args[1])
    elif option.query_relation_by_er == True:
        result = sparql_util.query_relation_by_er(args[0],args[1])
    elif option.query_onehop_by_er == True:
        result = sparql_util.query_onehop_by_er(args[0],args[1])
    if result is not None:
        for row in result:
            print(row)


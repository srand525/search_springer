import helper
import importlib
import SpringerFetch
import SpringerParse
# import SpringerPush
importlib.reload(helper)
importlib.reload(SpringerFetch)
importlib.reload(SpringerParse)

# ssl._create_default_https_context = ssl._create_unverified_context


# input_term_arg= sys.argv[1]
# input_db_arg = sys.argv[2]
# email_id_arg = sys.argv[3]

def springer_search_fetch(input_term,api_key):
    springer_fetch_inst = SpringerFetch.springer_fetch(input_term,api_key)

    url = springer_fetch_inst.ping_api()

    results,record_count = springer_fetch_inst.pull_results(url)

    # record_count = 10

    prop_dict = springer_fetch_inst.search_properties(record_count)

    unique_id = prop_dict['id']

    helper.serialize_output(unique_id,results['records'])

    helper.update_id_json(prop_dict)

    return(record_count,prop_dict)

def main(input_term,api_key):
    input_term = input_term.lower()
    springer_search_fetch(input_term,api_key)
    SpringerParse.main()
    # parse_df = helper.id_run('parse','springer')
    # parse_df

#
# def main(input_term,input_db,email_id):
#     input_db = input_db.lower()
#     ncbi_search(input_term,input_db,email_id)
#     ncbi_fetch(input_db,input_term, email_id)
#     if input_db == 'pmc':
#         PMCParse.main()
# def ncbi_search(input_term,input_db,email_id):
#     ncbi_search_inst = NCBISearch.ncbi_search(input_term = input_term,input_db = input_db,email_id = email_id)
#     # record_count = ncbi_search_inst.pub_count()
#     record_count = 10
#     id_list_all = ncbi_search_inst.pub_search(record_count)
#     prop_dict = ncbi_search_inst.search_properties(record_count)
#     unique_id = prop_dict['id']
#     helper.serialize_output(unique_id,id_list_all)
#     helper.update_id_json(prop_dict)
#     # helper.clean_folder()
#     return prop_dict
#
#
# def ncbi_fetch(input_db,input_term, email_id):
#         fetch_inst = NCBIFetch.ncbi_fetch(input_db,email_id)
#
#         id_list_fetch = helper.id_run('search',input_db)
#
#         doc_list = fetch_inst.pub_fetch(id_list_fetch)
#
#         prop_dict = fetch_inst.search_properties()
#
#         unique_id = prop_dict['id']
#
#         helper.serialize_output(unique_id,doc_list)
#
#         helper.update_id_json(prop_dict)
#         return(len(id_list_fetch),prop_dict)
#
# def main(input_term,input_db,email_id):
#     input_db = input_db.lower()
#     ncbi_search(input_term,input_db,email_id)
#     ncbi_fetch(input_db,input_term, email_id)
#     if input_db == 'pmc':
#         PMCParse.main()
#     # if input_db == 'pubmed':
#     #     PUBMEDParse.main()
#     # if input_db == 'springer':
#     #     SpringerParse.main()
#     # main_push(input_term,input_db,cur,con,pull_requestor)
#
if __name__ == '__main__':
    main(input_term,api_key)

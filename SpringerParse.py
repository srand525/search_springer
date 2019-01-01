import helper
import pandas as pd
import datetime

def parse_abstract(article):
    abstract = article['abstract']
        #include text cleaning code!
    return abstract

def parse_author(article):
    author_list = article['creators']
    auth_list = [a['creator'] for a in author_list]
    auth_names_list = [b.split(',') for b in auth_list]
    auth_dict_list = []
    for auth in auth_names_list:
        if len(auth) >= 2:
            auth_dict = {}
            auth_dict['fname'] = auth[1]
            auth_dict['lname'] = auth[0]
            auth_dict['contact'] = None
            auth_dict['affl'] = None
        if len(auth) < 2:
            auth_dict = {}
            auth_dict['fname'] = auth[0]
            auth_dict['lname'] = None
            auth_dict['contact'] = None
            auth_dict['affl'] = None
        auth_dict_list.append(auth_dict)
    return auth_dict_list

def parse_date(article):
    publishdatefull = article['publicationDate']
    return publishdatefull

def parse_id(article):
    associatedId = article['identifier']
    optionalId01 = article['doi']
    optionalId02 = article['issn']
    id_dict = {'springer':associatedId,'doi':optionalId01,'issn':optionalId02}
    return id_dict

def parse_springer(article):
    title = article['title']
    journal_name = article['publicationName']
    journal_id = article['journalid']
    pub_type = article['genre']
    abstract = parse_abstract(article)
    publishdatefull = parse_date(article)
    id_dict = parse_id(article)
    auth_dict_list = parse_author(article)
    kwd_dict_list = []

    d = {
        'title':title,
        'associatedId': id_dict['springer'],
        'author': auth_dict_list,
        'journalName' : journal_name,
        'journalISO':journal_id,
        'pubtype': pub_type,
        'publishdate':None,
        'publishdatefull':publishdatefull,
        'meshterms': kwd_dict_list,
        'abstract':abstract,
        'optionalId01' :id_dict['doi'],
        'optionalId02': id_dict['issn'],
        'pullsource': 'springer'
    }
    return d


def parse_all(article_list):
  article_dict_list = []
  for art in article_list:
    try:
        d = parse_springer(art)
        article_dict_list.append(d)
    except:
        pass
  parsed_df = pd.DataFrame(article_dict_list)
  return parsed_df

def parse_properties(parsed_df):
    unique_id = helper.create_unique_id()
    now = datetime.datetime.now()
    time_stamp = now.strftime("%Y-%m-%d %H:%M")
    n_records_parsed = len(parsed_df.index)
    prop_dict = {'id':unique_id,'id_type':'parse'
    ,'input_db':'springer','record_count':n_records_parsed
    ,'run_date':time_stamp}
    return prop_dict

def main():
    article_list = helper.id_run('fetch','springer')
    parsed_df = parse_all(article_list)
    prop_dict = parse_properties(parsed_df)
    unique_id = prop_dict['id']
    helper.serialize_output(unique_id,parsed_df)
    helper.update_id_json(prop_dict)

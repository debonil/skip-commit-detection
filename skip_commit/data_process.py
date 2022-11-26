import typing
import pandas as pd
import pathlib
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer


src_file_ext = ['R', 'jks', 'Procfile', 'classpath', 'properties', 'gradle', 'yml', 'spec', 'avi', 'png', 'ai', 'ser', 'json', 'sh', 'gpx', 'ttf', 'kwgt', 'csv', 'style', 'dtd', 'xml', 'Rproj', 'pro',
                'conf', 'Dockerfile', 'pdf', 'gz', 'jpg', 'class', 'travis', 'html', 'bat', 'gradlew', 'mustache', 'java', 'klck', 'ico', 'pl', 'userdata/keepthisfile', 'jar', 'css', 'prefs', 'project', 'bib']

meta_files_ext = ['Procfile', 'classpath', 'properties',
                  'gradle', 'csv', 'gradlew', 'prefs', 'project', '.gitignore']

list_defec_words = ['bug', 'fix', 'fixed', 'defect', 'issue']

list_merge_words = ['Merge', 'merge', 'merged']

list_format = ['formated', 'format', 'formatting']

version_words = ['version', 'Version']

list_comment = ['commented', 'comment', 'commenting', 'comments']


file_stats = {}

GitCommitBasic = typing.TypedDict('GitCommitBasic',
                                  {'author': dict,
                                   'comment_count': int,
                                   'committer': dict,
                                   'message': str,
                                   'tree': dict,
                                   'url': str,
                                   'verification': dict})
GitCommit = typing.TypedDict('GitCommit',
                             {'sha': str,
                              'node_id': str,
                              'commit': GitCommitBasic,
                              'url': str,
                              'html_url': str,
                              'comments_url': str,
                              'author': dict,
                              'committer': dict,
                              'parents': list,
                              'stats': dict,
                              'files': list})


def calc_entropy(val_list: list[int]):
    s = sum(val_list)
    if s == 0:
        return 0
    acc = 0
    for val in val_list:
        acc += (val/s) ** 2
    return 1 - acc


def get_entropy_changes(allFiles):
    this_l = []
    for file in allFiles:
        this_l.append(file['changes'])
    return calc_entropy(this_l)


def find_number_mod_directory(allFiles):
    list_dir = []
    for file in allFiles:
        this_file = file['filename']
        if "/" in this_file:
            path = pathlib.PurePath(this_file)
            list_dir.append(path.parent.name)
    return len(set(list_dir))


def get_file_types_value(allFiles):
    file_exts = []
    for file in allFiles:
        # #print(file)
        this_file = file['filename']
        # #print(this_file)
        file_extension = pathlib.Path(this_file).suffix
        #file_ext = file.split(".")[-1]
        file_exts.append(file_extension)
    file_ext_cm = list(set(file_exts))
    return 0 if any(word in file_ext_cm for word in src_file_ext) else 1


def get_file_meta(allFiles):
    file_exts = []
    for file in allFiles:
        # #print(file)
        this_file = file['filename']
        # #print(this_file)
        file_extension = pathlib.Path(this_file).suffix
        #file_ext = file.split(".")[-1]
        file_exts.append(file_extension)
    file_ext_cm = list(set(file_exts))
    return 1 if any(word in file_ext_cm for word in meta_files_ext) else 0


def get_text_tfidf(all_commits):
    all_messages = []
    for this_comit in all_commits:
        all_messages.append(this_comit['commit']['message'])
    documents = all_messages
    # create set of stopwords to remove
    stop_words = set(stopwords.words('italian'))
    english_stop_words = set(stopwords.words('english'))
    stop_words.update(english_stop_words)

    # check if word in stop words
    # print('when' in stop_words)  # True
    # print('il' in stop_words)  # True

    # else add word to the set
    # print('went' in stop_words)  # False
    stop_words.add('skip')
    stop_words.add("ci")

    # create tf-idf from original documents
    tfidf = TfidfVectorizer(stop_words=stop_words,
                            use_idf=True, max_features=10)
    x = tfidf.fit_transform(documents)
    featuere_name = tfidf.get_feature_names_out()
    return x, featuere_name


def get_no_developer_for_file(all_commits):
    file_dev_stat = []
    file_set = set()
    developer_set = set()
    for this_commit in all_commits:
        all_files_this_commit = this_commit['files']
        for this_file in all_files_this_commit:
            file_dev_stat.append(
                {this_file['filename']: this_commit['commit']['author']['name']})
            file_set.add(this_file['filename'])
            developer_set.add(this_commit['commit']['author']['name'])
    # print(len(developer_set))
    for this_file_set in file_set:
        devlopers = set()
        for combi in file_dev_stat:
            file_name = list(combi.keys())[0]
            if str(file_name) in str(this_file_set):
                devlopers.add(list(combi.values())[0])
        file_stats[this_file_set] = len(devlopers)
    # #print(file_stasts)
    return file_stats

#file_stats = get_no_developer_for_file()

# #print(file_stats)


def get_no_dev_change_files(all_files):
    files_stats_count = []
    for this_file in all_files:
        # #print(file_stats[this_file['filename']])
        if this_file['filename'] in file_stats:
            files_stats_count.append(
                int(file_stats[str(this_file['filename'])]))
        return max(files_stats_count) if len(files_stats_count) else 0


def map_to_df(commit_dict: GitCommit):

    new_dict = {}

    #new_dict['DIFF_NS'] =0
    new_dict['DIFF_ND'] = find_number_mod_directory(commit_dict['files'])
    new_dict['DIFF_NF'] = int(len(commit_dict['files']))
    new_dict['DIFF_EN'] = get_entropy_changes(commit_dict['files'])

    new_dict['SIZE_LA'] = int(commit_dict['stats']['additions'])
    new_dict['SIZE_LD'] = int(commit_dict['stats']['deletions'])
    #new_dict['SIZE_LT'] = 0
    #new_dict['SIZE_TFC'] = 0

    new_dict['PURP_FIX'] = 1 if any(word.lower(
    ) in commit_dict['commit']['message'] for word in list_defec_words) else 0
    new_dict['PURP_MR'] = 1 if any(word.lower(
    ) in commit_dict['commit']['message'] for word in list_merge_words) else 0
    #new_dict['PURP_CFT'] =0

    #new_dict['HIST_NDEV'] = get_no_dev_change_files(commit_dict['files'])
    #new_dict['HIST_AGE'] =0
    #new_dict['HIST_NUC'] =0

    #new_dict['EXP_EXP'] =0
    #new_dict['EXP_REXP'] =0
    #new_dict['EXP_SEXP'] =0

    #new_dict['TEXT_CM'] =0

    new_dict['SKIP_DOC'] = get_file_types_value(commit_dict['files'])
    new_dict['SKIP_MET'] = get_file_meta(commit_dict['files'])
    new_dict['SKIP_COM'] = 1 if any(
        word.lower() in commit_dict['commit']['message'] for word in list_comment) else 0
    new_dict['SKIP_FRM'] = 1 if any(
        word.lower() in commit_dict['commit']['message'] for word in list_format) else 0
    new_dict['SKIP_BLD'] = 1 if any(
        word.lower() in commit_dict['commit']['message'] for word in version_words) else 0

    new_dict['LABEL'] = int(('[ci skip]' in commit_dict['commit']['message'].lower()) or (
        '[skip ci]' in commit_dict['commit']['message'].lower()))

    return new_dict


def preprocess_data(all_commits):
    print(f'\t\t\t before all_commits length {len(all_commits)}')
    all_commits = [x for x in all_commits if x.get('files')]
    print(f'\t\t\t after all_commits length {len(all_commits)}')
    new_format = [map_to_df(cm) for cm in all_commits]
    x, featuere_name = get_text_tfidf(all_commits)
    new_format_df = pd.DataFrame(new_format)
    for i, fn in enumerate(featuere_name):
        new_format_df['CM_'+fn] = x.A.T[i]
    return new_format_df

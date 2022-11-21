""" 
Functions of this file are:
    Download Git commits using API
    Transform Raw API data into feature vector

"""

import data_process
import os
import requests
import json
import os


api_token = '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'
headers = {'Accept': 'application/vnd.github+json',
           'Authorization': 'Bearer {0}'.format(api_token)}


def write_to_file(file_name, data):
    with open(f'data/{file_name}.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def mine_repository(repo_url: str):
    file_name = repo_url.replace('/', '_')
    if os.path.exists(f'data/{file_name}.json'):
        print(f'Repository {repo_url} already expolred!')
        return
    print(f'Exploring repository {repo_url}:')
    github_log_api_endpoint = f'https://api.github.com/repos/{repo_url}/commits'
    r = requests.get(github_log_api_endpoint, headers=headers)
    r_git_log = json.loads(r.content)
    r.close()
    if not isinstance(r_git_log, dict):
        page_count = 1
        links_str = r.headers['Link']
        while links_str:
            page_count += 1
            next_link = [l.split(';')[0] for l in links_str.split(
                ',') if '; rel="next"' in l]
            if next_link:
                print(
                    f'\r Calling next page request = {next_link[0][1:-1]}', end='')
                r = requests.get(next_link[0][1:-1], headers=headers)
                r_git_log_next = json.loads(r.content)
                if not isinstance(r_git_log_next, dict):
                    r_git_log.extend(r_git_log_next)
                    links_str = r.headers['Link']
                else:
                    break
            else:
                break
        print('\r', end='')
        print(
            f'\t{len(r_git_log)} commits found in repository {repo_url} in {page_count} pages. {" "*30}')
        for i, commit in enumerate(r_git_log):
            print(f'\r\tDeep loading commit {i+1} of {len(r_git_log)}', end='')
            commit_sha = commit["sha"]
            github_commit_api_endpoint = f'{github_log_api_endpoint}/{commit_sha}'
            r = requests.get(github_commit_api_endpoint, headers=headers)
            r_git_commit = json.loads(r.content)
            r.close()
            commit.update(r_git_commit)
        print(
            f'\r\t{len(r_git_log)} commits deep loaded for repository {repo_url}.')
        write_to_file(file_name, r_git_log)
    else:
        print(f'Could not access repository {repo_url}')
        print(f'Error: {r_git_log}')

# Driver Code to Download commit data from API


target_repos_list = ['tracee/contextlogger', 'jMotif/SAX', 'ksclarke/solr-iso639-filter', 'jMotif/GI',
                     'GrammarViz2/grammarviz2_src', 'eBay/parallec', 'zixpo/candybar', 'steve-community/steve', 'mtsar/mtsar']

for repo_url in target_repos_list:
    mine_repository(repo_url)


# driver code to transform raw json data to feature vector

def do():
    repo_files = os.listdir('data/')

    all_commits_cnt = 0
    # all_commits:list[dict] = []
    for repo_file in repo_files:
        with open('data/' + repo_file, 'r', encoding='utf-8') as f:
            repo_commits = json.load(f)
            try:
                new_format_df = data_process.preprocess_data(repo_commits)
                new_file_name = f'processed_data/{os.path.splitext(repo_file)[0]}.csv'
                new_format_df.to_csv(new_file_name, index=False)
                all_commits_cnt += len(repo_commits)
                print(f'{repo_file} successfully processed')
            except Exception as e:
                print(f'error in formatting {repo_file} : {e.__traceback__}')
        # all_commits.extend(repo_commits)
    print(f'{all_commits_cnt} commits from {len(repo_files)} repository loaded!')

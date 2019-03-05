import git
from flashtext import KeywordProcessor

keyword_processor = KeywordProcessor()

repo = git.Repo("../wifi_activity_logger")
keyword_processor.add_keyword('connect')

commits_list = list(repo.iter_commits())

all_commits = ""

print('Commits: {}'.format(len(commits_list)))
for i in range(len(commits_list)):
	if i == len(commits_list)-1:
		break
	a_commit = commits_list[i]
	b_commit = commits_list[i+1]

	diff = a_commit.diff(b_commit, create_patch=True)

	# db.connect('secret_pw', 'google.com')
	for diff in diff.iter_change_type('M'):
		try:
			commit_diff = diff.a_blob.data_stream.read().decode('utf-8')
			all_commits += commit_diff
		except IOError:
			print("Err")
		except UnicodeDecodeError:
			print("Err")

all_commits_lines = all_commits.splitlines()
for f in all_commits_lines:
	if len(keyword_processor.extract_keywords(f)) > 0:
		print(f)

import git
from flashtext import KeywordProcessor

keyword_processor = KeywordProcessor()

repo = git.Repo("../wifi_activity_logger")
keyword_processor.add_keyword('.connect')

commits_list = list(repo.iter_commits())

print('Commits: {}'.format(len(commits_list)))
for i in range(len(commits_list)):
	a_commit = commits_list[i]
	b_commit = commits_list[i+1]

	diff = a_commit.diff(b_commit, create_patch=True)

	all_commits = ""

	for diff in diff.iter_change_type('M'):
		try:
			commit_diff = diff.a_blob.data_stream.read().decode('utf-8')
			all_commits += commit_diff
		except IOError:
			print("Err")
		except UnicodeDecodeError:
			print("Err")
	#print(all_commits)
	print(keyword_processor.extract_keywords(all_commits))

import git
repo = git.Repo("/")

commits_list = list(repo.iter_commits())

print('Commits: {}'.format(len(commits_list)))
for i in range(len(commits_list)):
	print(i)
	if not i <= 0:
		a_commit = commits_list[i]
		b_commit = commits_list[i+1]

		diff = a_commit.diff(b_commit, create_patch=True)

		for diff in diff.iter_change_type('M'):
			try:
				print(diff.a_blob.data_stream.read().decode('utf-8'))
			except IOError:
				print("Err")
			except UnicodeDecodeError:
				print("Err")

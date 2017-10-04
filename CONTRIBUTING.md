#Fork a Repo 

A *fork* is a copy of a repository. Forking a repository allows you to freely experiment with changes without affecting the original project.

Most commonly, forks are used to either propose changes to someone else's project or to use someone else's project as a starting point for your own idea.

##### Propose changes to someone else's project

A great example of using forks to propose changes is for bug fixes. Rather than logging an issue for a bug you've found, you can:

- Fork the repository.
- Make the fix.
- Submit a *pull request* to the project owner.

If the project owner likes your work, they might pull your fix into the original repository!

###How to fork this repo

Forking a repository is a simple two-step process. We've created a repository for you to practice with!

1. On GitHub, navigate to the [Student-Group-Activity-Recognition](https://github.com/prateekiiest/Student-Group-Activity-Recognition) repository.
2. the top-right corner of the page, click **Fork**. ![Fork button](https://help.github.com/assets/images/help/repository/fork_button.jpg)

Resource [Github](https://help.github.com/articles/fork-a-repo/)



# Create branches and push changes to the master repo

Create the branch on your local machine and switch in this branch :

```
$ git checkout -b [name_of_your_new_branch]
```

Change working branch :

```
$ git checkout [name_of_your_new_branch]
```

Push the branch on github :

```
$ git push origin [name_of_your_new_branch]
```

When you want to commit something in your branch, be sure to be in your branch. Add -u parameter to set upstream.

You can see all branches created by using :

```
$ git branch
```

Which will show :

```
* approval_messages
  master
  master_clean
```

Add a new remote for your branch :

```
$ git remote add [name_of_your_remote] 
```

Push changes from your commit into your branch :

```
$ git push [name_of_your_new_remote] [name_of_your_branch]
```

Update your branch when the original branch from official repository has been updated :

```
$ git fetch [name_of_your_remote]
```

Then you need to apply to merge changes, if your branch is derivated from develop you need to do :

```
$ git merge [name_of_your_remote]/develop
```

Delete a branch on your local filesystem :

```
$ git branch -d [name_of_your_new_branch]
```

To force the deletion of local branch on your filesystem :

```
$ git branch -D [name_of_your_new_branch]
```

Delete the branch on github :

```
$ git push origin :[name_of_your_new_branch]
```

Resource [GitHub](https://github.com/Kunena/Kunena-Forum/wiki/Create-a-new-branch-with-git-and-manage-branches)



# Contributing

When contributing to this repository, please first discuss the change you wish to make via issue or any other method with the owners of this repository before making a change. 

Please note we have a code of conduct, please follow it in all your interactions with the project.

## Pull Request Process

1. Ensure any install or build dependencies are removed before the end of the layer when doing a 
   build.
2. Update the README.md with details of changes to the interface.
3. Increase the version numbers in any examples files and the README.md to the new version that this
   Pull Request would represent. 
4. You may merge the Pull Request in once you have the sign-off of two other developers, or if you 
   do not have permission to do that, you may request the second reviewer to merge it for you.

## Code of Conduct

### Our Standards

Examples of behavior that contributes to creating a positive environment
include:

* Using welcoming and inclusive language
* Being respectful of differing viewpoints and experiences
* Gracefully accepting constructive criticism
* Focusing on what is best for the community
* Showing empathy towards other community members

Examples of unacceptable behavior by participants include:

* The use of sexualized language or imagery and unwelcome sexual attention or
  advances
* Trolling, insulting/derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or electronic
  address, without explicit permission
* Other conduct which could reasonably be considered inappropriate in a
  professional setting

### Our Responsibilities

Project maintainers are responsible for clarifying the standards of acceptable
behavior and are expected to take appropriate and fair corrective action in
response to any instances of unacceptable behavior.

Project maintainers have the right and responsibility to remove, edit, or
reject comments, commits, code, wiki edits, issues, and other contributions
that are not aligned to this Code of Conduct, or to ban temporarily or
permanently any contributor for other behaviors that they deem inappropriate,
threatening, offensive, or harmful.

### Scope

This Code of Conduct applies both within project spaces and in public spaces
when an individual is representing the project or its community. Examples of
representing a project or community include using an official project e-mail
address, posting via an official social media account, or acting as an appointed
representative at an online or offline event. Representation of a project may be
further defined and clarified by project maintainers.

### Enforcement

All complaints will be reviewed and investigated and will result in a response that
is deemed necessary and appropriate to the circumstances. The project team is
obligated to maintain confidentiality with regard to the reporter of an incident.
Further details of specific enforcement policies may be posted separately.

Project maintainers who do not follow or enforce the Code of Conduct in good
faith may face temporary or permanent repercussions as determined by other
members of the project's leadership.


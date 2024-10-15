Integration with Github
GitHub is one of the most important platforms for Continuous Integration (CI) because it is the most popular site for hosting and collaborating code projects.

In order to build your project on GitHub, a CI server needs to fetch your code and other artifacts such as configuration files from source control. The exact details vary depending on the CI system in use, but the basic outline is this:

Log into GitHub and go to the 
[personal access tokens (classic) page](https://github.com/settings/tokens)
.

From the Generate new token drop-down menu, select Generate new token (classic).

Give the token a name and select the permissions your CI system needs (these will usually be listed in the CI system documentation).

Click Generate token. Make sure you save the token. It will only be displayed once.

Provide your GitHub username and the token to your CI system.

After you have integrated the two, the CI system will watch your GitHub project for new code commits. Usually this means watching for three types of events:

Commits to the master branch.

Commits to an alternative branch.

Pull requests being merged into master or another branch.

These events can trigger the CI system to fetch the latest code and run the CI pipeline in that branch. 

Webhooks
GitHub is able to notify CI tools about code changes through webhooks. A webhook is a URL provided to GitHub by the CI system. GitHub will send an HTTP request to the webhook URL whenever certain events happen in the GitHub repository (such as the three scenarios outlined above). GitHub will pass certain information in the HTTP request that informs the CI system of the commit.

Usually the CI system will use your GitHub API token to add the webhooks to your GitHub project for you. In some cases, they will provide instructions and a webhook URL that you can paste into GitHub yourself.

GitHub’s status checks
GitHub’s status checks notify you if your commits meet the conditions set for the repository to which you’re contributing. A status check is a GitHub API feature that allows an external CI system to mark a pipeline as pending, succeeded, or failed. A screenshot below shows a display of status checks: 

A screenshot of status checks in GitHub showing that 11 checks were successful, two failed, and four were skipped.
![img.png](img.png)
A single pipeline may create several status checks in GitHub. For example:

Build - succeeded

Unit tests - succeeded

Integration tests - pending

Security scan - pending

GitHub will display the status checks on the appropriate commit or branch, so that you can watch the status of the pipeline without having to find it in the CI tool. For an example of what status checks look like, see 
[About status checks](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/collaborating-on-repositories-with-code-quality-features/about-status-checks)
.

Key takeaways
CI with GitHub benefits developers and the community. After you have integrated with GitHub, the CI system will watch your GitHub project for new code commits. GitHub communicates changes with the CI system through webhooks. You can review the status checks to see if your commits meet the conditions.

References
[What is GitHub And How To Use It?](https://www.simplilearn.com/tutorials/git-tutorial/what-is-github) [Updated] (simplilearn.com)

[A beginner’s guide to CI/CD and automation on GitHub](https://github.blog/2022-06-03-a-beginners-guide-to-ci-cd-and-automation-on-github/) - The GitHub Blog

[Creating webhooks - GitHub Docs](https://docs.github.com/en/webhooks-and-events/webhooks/creating-webhooks)

[GitHub integration overview - CircleCI](https://circleci.com/docs/github-integration/)

[How to Setup a GitHub to Jenkins Pipeline with WebHooks](https://santoshk.dev/posts/2022/how-to-setup-a-github-to-jenkins-pipeline-with-webhook/) – Fullstack with Santosh (santoshk.dev)

[About status checks](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/collaborating-on-repositories-with-code-quality-features/about-status-checks) - GitHub Docs

[Enabling GitHub Checks](https://circleci.com/docs/enable-checks/) - CircleCI


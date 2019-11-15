Contribution Guide
==================

Welcome to our project! We love that you're interested in contributing,
and we're happy to help you with your contribution.


1. Create a fork of this repository on [GitHub](https://www.github.com>)
   under your own account.

2. Clone the repository to your local machine by running

   ```console
   $ git clone https://github.com/username/repo.git
   ```

   replacing `username` and `repo` with your GitHub username and the
   name of the cloned repository, respectively.

3. Create a new branch

   ```console
   $ git checkout -b my-new-branch
   ```

4. Make some awesome changes, then commit them by running:

   ```console
   $ git commit -m "Description of your changes"
   ```

   If you leave off the `-m "Description of your changes"` part, you'll
   get a text editor where you can write a longer message if you like.

5. Merge in any changes from the main repository that might have
   occurred since you made the fork. Fix any merge conflicts

   ```console
   $ git checkout master
   $ git pull upstream master
   $ git checkout my-new-branch
   $ git merge master
   ```

6. Push the branch:

   ```console
   $ git push -u origin my-new-branch
   ```

7. Submit a pull request on [GitHub](https://www.github.com)

8. Thanks for your contribution! One of the maintainers will get back to
   you soon with any suggested changes or feedback.

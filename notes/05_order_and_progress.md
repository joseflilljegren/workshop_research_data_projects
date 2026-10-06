# Project setup

## Rules of thumb:

### 1. Commit your progress

If you or Claude needs to go back to look at how things were done before, git is your solution. Comment your commits to your collaborators and ask Claude to write documentation for the usage of the code and how it should be run

### 2. Generate output

The input of the project should be fixed. Alterations of that input depends on what actions _you_ make to alter it. Consequently, a source image should never be replaced. Instead, it should save as a new image in an altered state. Imagine images that are stored in folders like:
 
 1. `raw`
 2. `rotated`
 3. `preprocessed`
 4. `manually_preprocessed`


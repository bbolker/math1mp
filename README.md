This repository holds material for Math 1MP3, "Introduction to mathematical/statistical programming", at McMaster University. Other material, especially sensitive or protected material, may be posted on [Avenue to Learn](http://avenue.mcmaster.ca).

Unless noted otherwise, material is licensed under the [Creative Commons CC-BY-SA license](https://creativecommons.org/licenses/by-sa/4.0/legalcode).

The user-facing version of this site (convenient access to HTML and PDF versions of notes etc.) is at the corresponding [Github page](http://bbolker.github.io/math1mp/).

## pushing changes to the course web page

All the material for the web page is on the `gh-pages` branch.

System setup (optional):

- go to the directory that holds your local copy of the repository
- make a new clone of the repo into a `gh-pages` subdirectory:
    `git clone git@github.com:bbolker/math1mp.git gh-pages`
- switch to that directory and `git branch gh-pages` to switch to the gh-pages branch
- now you can switch back and forth between branches by changing directories

to build a particular version of the web notes:

- go to the notes directory
- in R, `rmarkdown::render("week2.rmd", output_format="...")`
 choices are "html_document", "pdf_document", "word_document" (or "ioslides_presentation") - this will generate a file e.g. `week2.docx` - move this to `../gh-pages/notes` and then commit and push

you can also go to `gh-pages` and run e.g. `make notes/week2.pdf` (and then commit and push)

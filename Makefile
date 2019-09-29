SRCDIR=..

## https://stackoverflow.com/questions/12069457/how-to-change-the-extension-of-each-file-in-a-list-with-multiple-extensions-in-g

## GOAL: make a list of all .rmd files in the relevant directories
admin   := $(notdir $(wildcard ${SRCDIR}/admin/*.rmd))
notes   := $(notdir $(wildcard ${SRCDIR}/notes/*.rmd))

## GOAL: define categories of output
nnhtml  := $(notes:%.rmd=%.html)
nnpdf   := $(notes:%.rmd=%.pdf)
nnpdf   := $(notes:%.rmd=%.docx)
aahtml  := $(admin:%.rmd=%.html)

## GOAL: build HTML for admin files, HTML+PDF+DOCX (maybe .slides.html too?) for notes
all: ${aahtml} ${nnhtml} ${nnpdf} ${nndocx}

## basic HTML/PDF rules
%.html: ${SRCDIR}/%.[Rr]md
	echo "rmarkdown::render(\"$<\",output_dir='.')" | R --slave

%.pdf: ${SRCDIR}/%.rmd
	echo "rmarkdown::render(\"$<\",output_dir='.',output_format=\"pdf_document\")" | R --slave

## rule for admin HTML that redirects output properly
%.html: ${SRCDIR}/admin/%.rmd
	echo "rmarkdown::render(\"$<\",output_format='html_document',output_dir='admin')" | R --slave

%.html: ${SRCDIR}/notes/%.rmd
	echo "rmarkdown::render(\"$<\",output_format='html_document',output_dir='notes')" | R --slave

admin/%.html: ${SRCDIR}/admin/%.rmd
	echo "rmarkdown::render(\"$<\",output_file=\"$@\",output_format='html_document',output_dir='admin')" | R --slave

notes/%.html: ${SRCDIR}/notes/%.rmd
	echo "rmarkdown::render(\"$<\",output_file=\"$@\",output_format='html_document',output_dir='notes')" | R --slave

notes/%.slides.html: ${SRCDIR}/notes/%.rmd
	echo "rmarkdown::render(\"$<\",output_file=\"$@\",output_format='ioslides_presentation',output_dir='notes')" | R --slave

notes/%.pdf: ${SRCDIR}/notes/%.rmd
	echo "rmarkdown::render(\"$<\",output_format='tufte_handout',output_dir='notes')" | R --slave

notes/%.docx: ${SRCDIR}/notes/%.rmd
	echo "rmarkdown::render(\"$<\",output_format='word_document',output_dir='notes')" | R --slave

misc/resources.html: ${SRCDIR}/misc/resources.md
	echo "rmarkdown::render(\"$<\",output_format='html_document',output_dir='misc')" | R --slave

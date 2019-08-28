SRCDIR=..

## https://stackoverflow.com/questions/12069457/how-to-change-the-extension-of-each-file-in-a-list-with-multiple-extensions-in-g


admin = $(notdir $(wildcard ${SRCDIR}/admin/*.rmd))
nnhtml := $(notes:%=notes/%.html)
nnrmd  := $(notes:%=notes/%.rmd)
aahtml := $(admin:%.rmd=%.html)

all: ${aahtml} ${nnhtml}

%.html: ${SRCDIR}/%.[Rr]md
	echo "rmarkdown::render(\"$<\",output_dir='.')" | R --slave

%.pdf: ${SRCDIR}/%.rmd
	echo "rmarkdown::render(\"$<\",output_dir='.',output_format=\"pdf_document\")" | R --slave

%.html: ${SRCDIR}/admin/%.rmd
	echo "rmarkdown::render(\"$<\",output_format='html_document',output_dir='admin')" | R --slave

notes/%.html: ${SRCDIR}/notes/%.rmd
	echo "rmarkdown::render(\"$<\",output_format='html_document',output_dir='notes')" | R --slave

notes/%.slides.html: ${SRCDIR}/notes/%.rmd
	echo "rmarkdown::render(\"$<\",,output_file=\"$@\",output_format='ioslides_presentation',output_dir='notes')" | R --slave

notes/%.pdf: ${SRCDIR}/notes/%.rmd
	echo "rmarkdown::render(\"$<\",output_format='tufte_handout',output_dir='notes')" | R --slave


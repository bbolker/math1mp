SRCDIR=..

## https://stackoverflow.com/questions/12069457/how-to-change-the-extension-of-each-file-in-a-list-with-multiple-extensions-in-g


admin   := $(notdir $(wildcard ${SRCDIR}/admin/*.rmd))
notes   := $(notdir $(wildcard ${SRCDIR}/notes/*.rmd))
nnhtml  := $(notes:%.rmd=%.html)
nnpdf   := $(notes:%.rmd=%.pdf)
nnpdf   := $(notes:%.rmd=%.docx)
aahtml  := $(admin:%.rmd=%.html)

all: ${aahtml} ${nnhtml} ${nnpdf} ${nndocx}

%.html: ${SRCDIR}/%.[Rr]md
	echo "rmarkdown::render(\"$<\",output_dir='.')" | R --slave

%.pdf: ${SRCDIR}/%.rmd
	echo "rmarkdown::render(\"$<\",output_dir='.',output_format=\"pdf_document\")" | R --slave

%.html: ${SRCDIR}/admin/%.rmd
	echo "rmarkdown::render(\"$<\",output_format='html_document',output_dir='admin')" | R --slave

%.html: ${SRCDIR}/notes/%.rmd
	echo "rmarkdown::render(\"$<\",output_format='html_document',output_dir='notes')" | R --slave

notes/%.slides.html: ${SRCDIR}/notes/%.rmd
	echo "rmarkdown::render(\"$<\",,output_file=\"$@\",output_format='ioslides_presentation',output_dir='notes')" | R --slave

notes/%.pdf: ${SRCDIR}/notes/%.rmd
	echo "rmarkdown::render(\"$<\",output_format='tufte_handout',output_dir='notes')" | R --slave

notes/%.docx: ${SRCDIR}/notes/%.rmd
	echo "rmarkdown::render(\"$<\",output_format='word_document',output_dir='notes')" | R --slave


SRCDIR=../../notes

%.html: ${SRCDIR}/%.rmd
	Rscript -e "rmarkdown::render(\"$<\",output_dir='.')"

%.pdf: ${SRCDIR}/%.rmd
	Rscript -e "rmarkdown::render(\"$<\",output_dir='.',output_format=\"pdf_document\")"


final_hints.html: ../../misc/final_hints.md
	pandoc -o final_hints.html ../../misc/final_hints.md

clean:
	rm -f *.log *.aux *.md *.out texput.log



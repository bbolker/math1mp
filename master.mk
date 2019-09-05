%.html: %.rmd
	echo "rmarkdown::render(\"$<\",output_format='html_document')" | R --slave

##%.pdf: %.rmd
##n	echo "rmarkdown::render(\"$<\",output_format='tufte_handout')" | R --slave

admin = $(wildcard admin/*.rmd)
notes = $(wildcard notes/*.rmd)
notepages = $(notes:%.rmd=gh-pages/%.html)
adminpages = $(admin:%.rmd=gh-pages/%.html)

pushnotes: $(notepages)
pushadmin: $(adminpages)

clean:
	find . \( -name "*~" -o -name "\#*#" -o -name "__pycache__" -o -name "*.out" -o -name "*.aux" -o -name "*.log" -o -name "*.out" \) -exec rm -Rf {} \;

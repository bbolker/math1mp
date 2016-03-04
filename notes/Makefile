%.html: %.rmd
	Rscript -e "library(\"rmarkdown\"); render(\"$<\")"

%.md: %.rmd
	Rscript -e "library(\"knitr\"); knit(\"$<\")"

%.tex: %.md
	pandoc -s -S -t latex -V documentclass=tufte-handout $*.md -o $*.tex

%.pdf: %.tex
	pdflatex --interaction=nonstopmode $*

clean:
	rm -f *.log *.aux *.md *.out texput.log

numpy_ex.html: README.rst trans_ex.py
	python3 -c "import trans_ex; trans_ex.trans_examples('README.rst','numpy_ex.md')"
	pandoc -s -o numpy_ex.html numpy_ex.md


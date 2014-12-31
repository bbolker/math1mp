%.html: %.rmd
	Rscript -e "library(\"rmarkdown\"); render(\"$<\")"

%.pdf: %.rmd
	Rscript -e "library(\"rmarkdown\"); render(\"$<\",output_format='pdf_document')"

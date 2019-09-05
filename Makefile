## This is 1MP3

current: target
-include target.mk

######################################################################

# Session

vim_session:
	bash -cl "vmt"

Sources += master.mk

######################################################################

## FRYing up some stuff to work with BB's current structure

admin = $(wildcard admin/*.rmd)
adminTargets = $(admin:%.rmd=pages/%.html)
notes = $(wildcard notes/*.rmd)

## [r]md_[h]tml-[r]ecipe
define rh_r
echo "rmarkdown::render(\"$<\",,output_dir='.',output_format=\"html_document\")" | R --slave
mv $(notdir $@) $@
endef

## PDF
define rp_r
echo "rmarkdown::render(\"$<\",,output_dir='.',output_format=\"tufte_handout\")" | R --slave
mv $(notdir $@) $@
endef

## Word (docx)
define rw_r
echo "rmarkdown::render(\"$<\",,output_dir='.',output_format=\"word_document\")" | R --slave
mv $(notdir $@) $@
endef

## ioslides
define rs_r
echo "rmarkdown::render(\"$<\",,output_dir='.',output_format=\"\")" | R --slave
mv $(notdir $@) $@
endef

adminTargets: $(adminTargets)

$(adminTargets): pages/%.html: %.rmd
	$(rh_r)

######################################################################

### Makestuff

Sources += Makefile

Ignore += makestuff
msrepo = https://github.com/dushoff
Makefile: makestuff/Makefile
makestuff/Makefile:
	git clone $(msrepo)/makestuff
	ls $@

-include makestuff/os.mk
-include makestuff/git.mk
-include makestuff/visual.mk
-include makestuff/projdir.mk

clean:
	find . \( -name "*~" -o -name "\#*#" -o -name "__pycache__" -o -name "*.out" -o -name "*.aux" -o -name "*.log" -o -name "*.out" \) -exec rm -Rf {} \;

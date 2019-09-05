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

define rh_r
echo "rmarkdown::render(\"$<\",,output_dir='.',output_format=\"html_document\")" | R --slave
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

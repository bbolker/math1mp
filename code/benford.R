benford <- function(x,fn,digit=1) {
    if (missing(x)) x <- readLines(fn)
    ff <- function(x,d) {
        if (d>0) x[d] else x[length(x)+(d+1)]
    }
    dig <- sapply(strsplit(x,""),ff,digit)
    table(dig)
}

library(XML)
theurl <- "http://en.wikipedia.org/wiki/List_of_lakes_in_Minnesota"
tables <- readHTMLTable(theurl)
View(tables[[1]])
areas <- na.omit(as.numeric(as.character(tables[[1]][[4]])))
b <- benford(as.character(areas))
plot(b[-1]/sum(b[-1]))
b2 <- benford(as.character(areas),digit=-1)

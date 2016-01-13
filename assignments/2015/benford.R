library("XML")
theurl <- "http://en.wikipedia.org/wiki/List_of_rivers_by_length"
tables <- readHTMLTable(theurl)
n.rows <- unlist(lapply(tables, function(t) dim(t)[1]))
tt <- as.character(tables[[6]][["Length (miles)"]])
tt <- gsub("([0-9,]+).*$","\\1",tt)
writeLines(tt,con="benford_rivers.txt")

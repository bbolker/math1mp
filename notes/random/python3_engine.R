eng_python3 <- function (options)
    ## modification of built-in python engine (i.e.
    ## pp <- knit_engines$get("python")
    ## dump("pp",file=...)
    ## _only_ required change is to add 'python3="-c"' in
    ## command-line-argument switch() selector
    ## also need %n% -> knit
{
    engine = options$engine
    code = if (engine %in% c("highlight", "Rscript", "sas", "haskell")) {
        f = basename(tempfile(engine, ".", switch(engine, sas = ".sas", 
            Rscript = ".R", ".txt")))
        writeLines(c(switch(engine, sas = "OPTIONS NONUMBER NODATE PAGESIZE = MAX FORMCHAR = '|----|+|---+=|-/<>*' FORMDLIM=' ';", 
            haskell = ":set +m"), options$code), f)
        on.exit(unlink(f))
        switch(engine, sas = {
            saslst = sub("[.]sas$", ".lst", f)
            on.exit(unlink(c(saslst, sub("[.]sas$", ".log", f))), 
                add = TRUE)
            f
        }, haskell = paste("-e", shQuote(paste(":script", f))), 
            f)
    }
    else paste(switch(engine, bash = "-c", coffee = "-e", groovy = "-e", 
        node = "-e", perl = "-e", python = "-c", python3 = "-c", ruby = "-e", 
        scala = "-e", sh = "-c", zsh = "-c", NULL), shQuote(paste(options$code, 
        collapse = "\n")))
    code = if (engine %in% c("awk", "gawk", "sed", "sas")) 
        paste(code, options$engine.opts)
    else paste(options$engine.opts, code)
    `%n%`  <- knitr:::`%n%`
    cmd = options$engine.path %n% engine
    out = if (options$eval) {
        message("running: ", cmd, " ", code)
        tryCatch(system2(cmd, code, stdout = TRUE, stderr = TRUE), 
            error = function(e) {
                if (!options$error) 
                  stop(e)
                paste("Error in running command", cmd)
            })
    }
    else ""
    if (!options$error && !is.null(attr(out, "status"))) 
        stop(paste(out, collapse = "\n"))
    if (options$eval && engine == "sas" && file.exists(saslst)) 
        out = c(readLines(saslst), out)
    engine_output(options, options$code, out)
}
require("knitr")
knit_engines$set(python3 = eng_python3)

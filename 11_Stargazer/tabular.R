library(dplyr)
library(stargazer)
out = stargazer(iris)
is(out)

tabular <- function(stargazer.out,file.name){
  out = head(stargazer.out[-1:-6],-1) 
  cat(paste(out, collapse="\n"),sep="\n",file = file.name)
}

iris %>% 
  stargazer(.) %>%
  tabular(.,"fn.tex")

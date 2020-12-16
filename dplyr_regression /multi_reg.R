rm(list=ls())

library(broom)
library(dplyr)
library(tibble)
library(purrr)
library(stargazer)
library(tidyr)
library(sandwich);
library(plm);
library(lmtest);
library(xtable)

table1 = mtcars %>%
  do(model1 = lm(wt~mpg, data=.) %>% coeftest(.,vcov = function(x) vcovHC(x, method="white1", type="HC1")) , 
     model2 = lm(wt~mpg+cyl, data=.) %>% coeftest(.,vcov = function(x) vcovHC(x, method="white1", type="HC1")) ,
     model3 = lm(wt~cyl, data=.) %>% coeftest(.,vcov = function(x) vcovHC(x, method="white1", type="HC1"))) 

stargazer(as.list(table1[1,]),type="text")

library(reticulate)
os <- import("os")
os$listdir(".")
source_python("risk-neutral-probability.py")
#py_install("numpy")
rnp(0.01,0.1,4,10000,1)


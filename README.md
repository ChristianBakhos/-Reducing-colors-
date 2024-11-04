Design an IP model and implement an algorithm for compressing a picture by reducing the number of its colors.
Intructions: Find the optimal objective function value of your IP model using Glpk, for the instance(20col.png, setting k = 8).
Implementation hint: Most likely, enumerating all possible centers for the instance 20col.png (image
 with 20 colors) would yield an IP with too many variables, for Glpk to be able to solve it. Here is a trick
 to reduce the number of variables (in particular, to reduce the number of possible centers to consider):
 • Run the local search algorithm on the instance 20col.png, with few random
 initializations. Store the best objective function value found.
 • When considering a centroid for a possible cluster, look at the total cost yield by just this cluster: if
 this is larger than the best objective function value above, you know that cluster would surely not be
 formed, and hence there is no need to introduce a variable for its centroid...

 Algorithm used is k means clustering: 
             Given p vectors xi Rn (for i = 1p), and a number k, we wish to find k centers C = {c1...ck} in R^n
             and assign each xi to the closest center in C, that is, to c(i) = argmin(cj in C) xi-cj^2(euclidean distance). 
             The objective is to minimize the total dissimilarity sum(p,i=1) xi-c(i)^2.

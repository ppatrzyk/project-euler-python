library(data.table)
library(ggplot2)

test <- data.table(expand.grid(a = 1:99, b = 1:99))
test[, product := a*b]
test2 <- test[!duplicated(product), ]
test2[, prodrank := rank(-product, ties.method = 'min')]
test2[, mylab := paste0(prodrank, " (", a, ",", b, ")")]

p <- ggplot(test2[a > 90 & b > 90, ], aes(a, b)) + 
  geom_tile(aes(fill = product), colour = "white") +
  geom_text(label = test2[a > 90 & b > 90, mylab]) +
  scale_fill_gradient(low = "white", high = "steelblue")
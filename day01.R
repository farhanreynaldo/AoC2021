library(tidyverse)

SAMPLES = "199
200
208
210
200
207
240
269
260
263
"

depths <- SAMPLES %>% 
  read_lines() %>% 
  as.numeric()

count_increasing <- function(depths) {
  count <- 0
  for (i in 1:(length(depths)-1)) {
    if (depths[i+1] > depths[i]) {
      count = count + 1
    }
  }
  count
}

stopifnot(count_increasing(depths) == 7)

print(count_increasing(input))

rolling_sum <- function(depths) {
  rolling_depths <- c()
  for (i in 1:(length(depths)-2)) {
    rolling_depths = c(rolling_depths, sum(depths[i], depths[i+1], depths[i+2]))
  }
  rolling_depths
}

stopifnot(count_increasing(rolling_sum(depths)) == 5)

print(count_increasing(rolling_sum(input)))
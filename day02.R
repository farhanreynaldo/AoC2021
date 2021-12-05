library(tidyverse)

SAMPLES = "
forward 5
down 5
forward 8
up 3
down 8
forward 2
"

parse_input <- function(input) {
  input %>% 
    str_trim() %>% 
    as_tibble() %>% 
    separate_rows(value, sep = '\n') %>% 
    separate(value, c("command", "value"), convert = T) %>%
    mutate(x = if_else(command == "forward", value, 0L), 
           y = case_when(
             command == "up" ~ -value,
             command == "down" ~ value,
             TRUE ~ 0L)
    )
}

p1 <- function(df) {
  df %>% 
    summarise(
      x = sum(x), 
      y = sum(y), 
      result = sum(x) * sum(y)
    ) %>% 
    pull(result)
}

stopifnot(SAMPLES %>% parse_input() %>% p1 == 150)
print(read_file('input/day02.txt') %>% parse_input() %>% p1())

p2 <- function(df) {
  df %>% 
    mutate(aim = cumsum(y), 
           depth = x * aim) %>% 
    summarise(
      x = sum(x),
      depth = sum(depth),
      result = sum(x) * sum(depth)
    ) %>% 
    pull(result)
}

stopifnot(SAMPLES %>% parse_input() %>% p2() == 900)
print(read_file('input/day02.txt') %>% parse_input() %>% p2())

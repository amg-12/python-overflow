module Even (isEven) where

isEven :: Int -> Bool
isEven 0 = True
isEven 1 = False
isEven x = isEven $ x^2

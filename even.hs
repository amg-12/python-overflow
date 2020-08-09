module Even (even') where

even' :: Int -> Bool
even' 0 = True
even' 1 = False
even' x = even' $ x^2

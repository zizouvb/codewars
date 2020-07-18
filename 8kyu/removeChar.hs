module Haskell.Codewars.RemoveChar where

removeChar :: String -> String
removeChar [] = []
removeChar [x] = []
removeChar (x:str) = init str

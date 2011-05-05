import Data.List (genericSplitAt)

type Index = Integer
type II    = (Integer,Index)

index :: [Integer] -> [II]
index x =  zip x [0..]

norep :: (II,II) -> Bool
norep ((a,c),(b,d)) = not (a == b && c == d)

combine :: [II] -> [ (II,II) ]
combine x = filter norep $ [ ((a,c),(b,d)) | (a,c) <- x , (b,d) <- x ]

seed :: Integer -> (Index,Index,Integer,Integer)
seed credit = (-1,-1,credit,credit)

disc :: (Index,Index,Integer,Integer) -> (II,II) -> (Index,Index,Integer,Integer)
disc old@(i1,i2,cr,diff) ((a,c),(b,d)) =
    let cdiff = (cr - (a + b)) in
    if cdiff >= 0 then 
        if cdiff < diff then
            (c,d,cr,cdiff)
        else
            old
    else
        old

credit :: Integer -> [(II,II)] -> (Index,Index,Integer,Integer)
credit credit = foldl disc (seed credit)

-- returns problems as a tuple of items and credit
parseCases :: [Integer] -> [([Integer],Integer)]
parseCases (numCases:xs) = go xs
    where 
      go [] = []
      go (credit:times:rest) = let (art,next) = genericSplitAt times rest
                               in (art,credit) : go next 

solve :: ([Integer],Integer) -> (Integer,Integer)
solve (art,cr) = let (i1,i2,_,_) = credit cr (combine.index $ art)
                 in 
                   if i1 <= i2 then
                       (i1+1,i2+1)
                   else
                       (i2+1,i1+1)

main :: IO () 
main = do 
  file <- getContents
  let raw = (map read (words file)) :: [Integer]
  let cases = parseCases raw
  let results = map solve cases
  putStr (concatMap (\(i,n) -> "Case #" ++ show i ++ ": " ++ show n ++ "\n")
                              (zip [1..] results))
  
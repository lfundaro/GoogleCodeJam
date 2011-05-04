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

-- main = do 
--  :( i need a monad to do this ...
  
  
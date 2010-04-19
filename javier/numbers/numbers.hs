
{-
  Google code jam - Online round A 2008 - warming up
  Problem: Numbers
  Implementation: free precision numbers (on lists) multiplied
  to obtain the n power of the number. From there the three
  lower precision numbers are taken
-}

{- Big Number: Positive lis, precision List and precision value
-}
data BigNumber = BN [Int] Int deriving (Show, Eq)

instance Num BigNumber where
    (BN pos prec) * (BN pos2 prec2) = multiply (BN pos prec) (BN pos2 prec2) 

showBigNumber::BigNumber->String
showBigNumber (BN p pr) =
    show p ++" "++show pr

{- Returns the multiplication of the reverse lists. 
The first list is already reverse for threeSquareFive efficiency
-}

multiply::BigNumber -> BigNumber -> BigNumber
multiply (BN p1 pr1) (BN p2 pr2) =
    (BN (reverse (multiplication (reverse p1) (reverse p2) [] [])) (pr1+pr2))
       
unitMul::[Int]->Int-> Int -> [Int]->[Int]
unitMul [] _ 0 l3 = l3
unitMul [] _ carry l3 = l3++[carry]
unitMul (xl1:yl1) xl2 carry l3 
    | (xl1*xl2)+carry>9 = unitMul yl1 xl2 (div ((xl1*xl2)+carry) 10) (l3++[mod ((xl1*xl2)+carry)  10])
    | otherwise = unitMul yl1 xl2 0 (l3++[(xl1*xl2)+carry])

{- Accumulated sum of two reversed list of int
-}
unitSum::[Int]->[Int]->Int->[Int]->[Int]
unitSum l1 [] 0 l3 = l3++l1
unitSum [] l2 0 l3 = l3++l2
unitSum (xl1:yl1) [] carry l3 = l3++((xl1+carry):yl1)
unitSum [] (xl2:yl2) carry l3 = l3++((xl2+carry):yl2)
unitSum [] [] carry l3 = l3++[carry]

unitSum (xl1:yl1) (xl2:yl2) carry l3 
    |((xl1+xl2)+carry)>9 = unitSum yl1 yl2 (div ((xl1+xl2)+carry) 10) (l3++[mod ((xl1+xl2)+carry)  10])
    | otherwise = unitSum yl1 yl2 0 (l3++[(xl1+xl2)+carry])

{- Accumulated multiplication of two reversed lists of int
-}

multiplication::[Int]->[Int]->[Int]->[Int]->[Int]
multiplication l1 [] _ l3 = l3
multiplication l1 (xl1:yl2) expand l3 =
    unitSum (expand ++ (unitMul l1 xl1 0 [])) (multiplication l1 yl2 (0:expand) []) 0 []

power::Int->BigNumber->BigNumber
power n (BN l pr) =
    tailPower n  (BN  l pr) (BN l pr)

tailPower::Int->BigNumber->BigNumber->BigNumber
tailPower 1 _ (BN l pr) = (BN l pr)
tailPower n (BN l pr) (BN l2 pr2) =
    tailPower (n-1) (BN l pr) (multiply (BN l pr) (BN l2 pr2))

{-Computes the n power of 3 + sqrt 5 
-}
threeSquareFive::Int->BigNumber
threeSquareFive n  = 
     power n (BN [5,2,3,6,0,6,7,9,8] 1) 




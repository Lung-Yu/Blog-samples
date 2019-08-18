#R 的基本資料屬性包含以下五種，可用 class或 typeof 函數判斷資料屬性
#character：文字字串，用 "" 包起來，ex："test"
#numeric：實數
#integer：整數
#complex：複數
#logical(boolean)：True 或 False

class("test")
class(10.10)
class(10)
class(as.integer(3)) # 因為 R 計算上是都是以雙倍精確度來計算，所以必須指定為 integer，不然都會被當成 numeric 看待。
class(as.integer(3.1)) # as.integer 可以將不是整數的數值變成整數
class(as.integer(T)) # as.integer(T) = 1
class(as.integer(F)) # as.integer(T) = 0
class(2+2i)
class(TRUE) # 注意都要大寫，不可寫 True，但可以簡化成 T
class(T)

#倘若輸入數值轉換異常則會輸出為NA。如將character輸入至as.integer處理失敗會產生NA。
a <- as.integer("a")
a

#基本運算
#四則運算、次方、平方根、商數與餘數。
a <- 6
b <- 4

a + b
a - b 
a * b
a / b 

a ^ b
a ** b
sqrt(b)

8 ^ (1/3)

a %/% b # a 除以b 的商數
a %% b # a 除以b 餘數


#sign：判斷是正、負數或 0
sign(10)
sign(-10)
sign(0)

#abs：取絕對值
abs(10)
abs(-10)
abs(0)

#log 運算
log(10) # log 以 e 為底
log1p(9) # log(x) = log1p(x - 1)
log(10, 2) # 指定 log 以 2 為底
log2(10) # log2 代表以 2 為底
log10(10) # log10 代表以 10 為底
log(0)
log(-1)

#exp
exp(1)
exp(10)
expm1(10) # expm1(x) = exp(x) - 1





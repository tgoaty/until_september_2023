from field import Field
ad = Field(60, 20, 20)
k, c = 0, 0
while True:
    k += 1
    for i in ad.matrix:
        if 6 in i:
            c += 1
            break
    if k%5000 == 0:
        print(k, c )

    ad = Field(60, 20, 20)


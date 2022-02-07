def solution(x, y):
    v1 = int(x)
    v2 = int(y)
    retorno = 'impossible'
    flag = False
    contador = 0
    while flag==False:
        # print('{}..{},{}'.format(contador, v1, v2))
        if(v1==1 and v2==1):
            retorno = contador
            flag = True
            continue
        contador = contador + 1

        if (v2==1 and v1>1):
            contador = contador + v1 - 2
            retorno = contador
            flag = True
        elif (v1==1 and v2>1):
            contador = contador + v2 - 2
            retorno = contador
            flag = True

        if (v1 > v2):
            m = 1
            if (v2>0 and (v1//v2)>1):
                m = v1//v2
                if (v1%v2==0):
                    break
                else:
                    contador = contador + m - 1
            v1 = (v1 - v2 * m)
            continue
           
        elif (v2 > v1):
            m = 1
            if (v1>0 and (v2//v1)>1):
                m = v2//v1
                if (v2%v1==0):
                    break
                else:
                    contador = contador + m - 1
            v2 = (v2 - v1 * m)
            continue
            
        if (v1==v2 and v1!=1):
            flag = True
        elif (v1<1 or v2<1):
            flag = true

    aa = str(contador).split("e+")
    if (len(aa)==2):
        retorno = str(aa[0]) + ('0' * int(aa[1]))
    aa2 = str(retorno).split(".")
    if (len(aa2)==2):
        retorno = aa2[0]
    return str(retorno)

  
print(solution('1000000000000000000000000000000000000000000000000','379'))

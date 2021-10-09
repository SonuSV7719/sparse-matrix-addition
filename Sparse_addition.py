def sparseAddition(mat1, mat2):

    i=0

    j=0

    addition = []

    l1 = len(mat1)-1

    l2 = len(mat2)-1

    while i<= l1 and j <= l2:

        tempMat = []

        if mat1[i][0]==mat2[j][0]:

            if mat1[i][1]==mat2[j][1]:

                tempMat.append(mat1[i][0])

                tempMat.append(mat1[i][1])

                sum = mat1[i][2]+mat2[j][2]

                tempMat.append(sum)

                addition.append(tempMat)

                i+=1

                j+=1

                print("tem", tempMat)

                print("addtion", addition)

            else:

                if mat1[i][1]<mat2[j][1]:

                    tempMat.append(mat1[i][0])

                    tempMat.append(mat1[i][1])

                    tempMat.append(mat1[i][2])

                    addition.append(tempMat)

                    i+=1

                    print("tem", tempMat)

                    print("addtion", addition)

                else:

                    if mat1[i][1]>mat2[j][1]:

                        tempMat.append(mat2[j][0])

                        tempMat.append(mat2[j][1])

                        tempMat.append(mat2[j][2])

                        addition.append(tempMat)

                        j+=1

                        print("tem", tempMat)

                        print("addtion", addition)

        else:

            if mat1[i][0]>mat2[j][0]:

                tempMat.append(mat2[j][0])

                tempMat.append(mat2[j][1])

                tempMat.append(mat2[j][2])

                addition.append(tempMat)

                j+=1

                print("tem", tempMat)

                print("addtion", addition)

            else:

                if mat1[i][0]<mat2[j][0]:

                    tempMat.append(mat1[i][0])

                    tempMat.append(mat1[i][1])

                    tempMat.append(mat1[i][2])

                    addition.append(tempMat)

                    i+=1

                    print("tem", tempMat)

                    print("addtion", addition)

    if j == (len(mat2)) and i == (len(mat1)-1):

        tempMat1 = []

        tempMat1.append(mat1[i][0])

        tempMat1.append(mat1[i][1])

        tempMat1.append(mat1[i][2])

        addition.append(tempMat1)

    if j == (len(mat2)-1) and i == (len(mat1)):

        tempMat2 = []

        tempMat2.append(mat2[j][0])

        tempMat2.append(mat2[j][1])

        tempMat2.append(mat2[j][2])

        addition.append(tempMat2)

    return addition



mat1 = [[0,1,2],[1,0,3],[1,1,6],[2,1,7]]

mat2 = [[0,1,2],[1,0,3],[1,3,9],[2,0,6],[2,1,9]]

print(sparseAddition(mat1, mat2))

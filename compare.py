def compare_script():
    import os
    import csv

    def compareProducts():
        with open('old_result.csv','r') as t1, open('new_result.csv', 'r') as t2:
            old = csv.reader(t1,delimiter='*')
            new = csv.reader(t2,delimiter='*')

            list_old = list(old)
            list_new = list(new)
            list_old.sort()
            list_new.sort()

            with open('update.csv', 'w') as outFile:
                outFile.write("Esewa Pasal \n")
                for i in range(len(list_new)):
                    for j in range(len(list_old)):
                        if(list_new[i][0]==list_old[j][0]):
                            if (list_new[i][1]!=list_old[j][1]):
                                row1 = list_old[j][0],list_old[j][1]
                                row2 = list_new[i][0],list_new[i][1]
                                print(row1)
                                print(row2)
                                outFile.write(str(row1))
                                outFile.write(str(row2))
                                outFile.write('\n')

    compareProducts()
    os.remove("old_result.csv")
    os.rename('new_result.csv', 'old_result.csv')

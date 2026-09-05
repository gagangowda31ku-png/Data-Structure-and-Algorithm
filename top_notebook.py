class Notebook:
    def __init__(self,title , username ,likes):
        self.title  = title
        self.username = username
        self.likes = likes

    def __repr__(self):
        return f"<{self.title}/{self.username}>    {self.likes}  Likes"

nb1 = Notebook('cifar10cnnmodel' , 'Gagan' , 6788)
nb2 = Notebook("LinearRegression" , 'Avinash' , 908)
nb3 = Notebook('LogisticRegressin' , 'Dharnesh', 5678)
nb4 = Notebook("feedforwardnueral" ,'Karthik',4567)
nb5 = Notebook("RandomForest" , 'Lohith',67)
nb6 = Notebook('Quara-question-classifiaction' , 'Chirath H m' ,689)
nb7 = Notebook('GradientBosting','Kavana',6789)
nb8 = Notebook('KMeans','Lakshmi' ,238)
nb9 = Notebook("KNN-MOdel" , 'Hruthik' ,1234) 



notebooks = [nb1 , nb2 , nb3 , nb4 , nb5 , nb6 , nb7 , nb8, nb9]

def compare_likes(nb1 , nb2):
    if nb1.likes > nb2.likes:
        return 'lesser'
    elif nb1.likes == nb2.likes:
        return 'equal'
    elif nb1.likes < nb2.likes:
        return 'greater'

def default_compare(x, y):
    if x < y:
        return 'lesser'

    elif x == y:
        return 'equal'

    else:
        return 'greater'

def merge_sort(objs , compare = default_compare):
    if len(objs) < 2:
        return objs

    mid = len(objs) // 2
    left_sorted = merge_sort(objs[:mid] , compare)
    right_sorted = merge_sort(objs[mid:] , compare)

    return merge(left_sorted , right_sorted , compare)

def merge(left , right , compare):
    i , j = 0 , 0
    merged = []

    while i < len(left) and j < len(right):
        result = compare(left[i] , right[j])

        if result == 'lesser' or result == 'equal':
            merged.append(left[i])
            i += 1

        else:
            merged.append(right[j])
            j += 1

    return merged + left[i: ] + right[j: ]
        
print(merge_sort(notebooks , compare_likes))
    


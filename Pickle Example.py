import pickle 

lst = [1,2,2,4,4,5]

pickle.dump(lst, open("lel.p", "wb"))


new_lst = pickle.load(open("lel.p", "rb"))

print(new_lst)

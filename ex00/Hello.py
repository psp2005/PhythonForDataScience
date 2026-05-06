ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

ft_list[1] = "World!"

ft_tuple = (ft_tuple[0], "France!")

# 튜플 다른 수정안1
# ft_tuple = ("Hello", "France!")
# 튜플 다른 수정안2
# tmp = list(ft_tuple)
# tmp[1] = "France!"
# ft_tuple = tuple(tmp)


ft_set.remove("tutu!")
ft_set.add("Paris!")

ft_dict["Hello"] = "42Paris!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
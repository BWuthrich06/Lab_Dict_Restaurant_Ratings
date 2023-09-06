"""Restaurant rating lister."""


def load_data(filename):
    data_list = []
    file = open(filename)

    for name in file:
        data = name.rstrip().split(":")
        data_tuple = tuple(data)
        data_list.append(data_tuple)

    file.close()
    return data_list





def get_restaurant_ratings():

    ratings = {}
    
    data = load_data("scores.txt")


    for item in data:

        name = item[0]          # or destructure:  name, rating = row
        rating = item[1]
        ratings[name] = rating 
        
    restaurant_name = input("Choose a restaurant name: ")
    restaurant_score = input("What do you rate the restaurant? ")

    ratings[restaurant_name] = restaurant_score

    #Turn dictionary into list, and sorts list
    sort_ratings = ratings.items()
    data_sort = sorted(sort_ratings)


#Turn list back into dictionary
    new_ratings = {}
    for item in data_sort:
        name, rating = item
        new_ratings[name] = rating

    return new_ratings

print(get_restaurant_ratings())






import data_structure.array as array
import data_structure.hash_table as ht

my_array = array.Array()
hash_table = ht.HashTable(50)

if __name__ == "__main__":
    # # array
    # my_array.push(1)
    # my_array.push(2)
    # my_array.push(3)
    # my_array.delete(1)
    # print(my_array)

    # # reverse a string
    # my_string = "abcdef"
    # print(array.reverse(my_string))

    # # merge sorted arrays
    # arr1 = [0, 3, 4, 31]
    # arr2 = [4, 6, 30]
    # print(array.merge_sorted(arr1, arr2))
    # print(array.merge_sorted2(arr1, arr2))
    hash_table.set("Mandag", 1)
    hash_table.set("Mandag", 3)
    hash_table.set("Tirstag", 88)
    try:
        hash_table.get("B")
    except KeyError as err:
        print(err)

    print(hash_table)
    print(list(hash_table.keys()))

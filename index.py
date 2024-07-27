# # Question :01
# userList = []
# length = int(input('Enter the length of the list: '))

# for i in range(length):
#     value = int(input(f'Enter value for index {i}: '))
#     userList.append(value)

# print('Your List:', userList)

# print('Alternate List:', userList[::2])


# # Question :02
# userList = []
# length = int(input('Enter the length of the list: '))

# for i in range(length):
#     value = int(input(f'Enter value for index {i}: '))
#     userList.append(value)
    
# print('orignal list :' , userList)
# print('reserve List :' , userList[::-1])


# # Question :03
# userList = []
# length = int(input('Enter the length of the list: '))

# for i in range(length):
#     value = int(input(f'Enter value for index {i}: '))
#     userList.append(value)

# maxNum = 0
# for i in userList:
#     if maxNum < i:
#         maxNum = i

# print('Largest number is :' , maxNum)


# # Question :04
# userList = [1,2,3,4,5,6,7,8]

# if len(userList) > 0:
#     last_element = userList.pop()
#     userList.insert(0, last_element)

# print('Rotated List:', userList)


# # Question :05
# sen = 'Python is a programming language!'
# print(sen)
# word_to_delete = input('Enter a word to delete from this sentence: ')
# words = sen.split()

# if word_to_delete in words:
#     words.remove(word_to_delete)

# new_sen = ' '.join(words)

# print("New sentence:", new_sen)

# # Question :06
# month_names = {
#     '01': 'January', '02': 'February', '03': 'March', '04': 'April',
#     '05': 'May', '06': 'June', '07': 'July', '08': 'August',
#     '09': 'September', '10': 'October', '11': 'November', '12': 'December'
# }

# date_input = input("Enter a date in the form mm/dd/yyyy: ")
# month, day, year = date_input.split('/')
# month_name = month_names[month]
# print(f"{month_name} {int(day)}, {year}")


# # Question :07
# user_input = input("Enter a sentence: ")
# words = user_input.split()
# capitalized_words = []

# for word in words:
#     capitalized_words.append(word.capitalize())

# capitalized_string = ' '.join(capitalized_words)

# print("Capitalized sentence:", capitalized_string)


# # Question :08
# matrix = [
#     [2,11,7,12], 
#     [5,2,9,15],  
#     [8,3,10,42]  
# ]

# num_rows = len(matrix)

# for i in range(num_rows):
#     row_sum = sum(matrix[i])
#     print(f"Sum of row {i + 1} = {row_sum}")


# # Qustion :09
# matrix1 = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# matrix2 = [
#     [9, 8, 7],
#     [6, 5, 4],
#     [3, 2, 1]
# ]
# result_matrix = [[0] * len(matrix1[0]) for _ in range(len(matrix1))]

# for i in range(len(matrix1)):
#     for j in range(len(matrix1[0])):
#         result_matrix[i][j] = matrix1[i][j] + matrix2[i][j]

# for row in result_matrix:
#     print(row)


# # Question :10
# matrix1 = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]

# matrix2 = [
#     [7, 8],
#     [9, 10],
#     [11, 12]
# ]

# num_rows1 = len(matrix1)
# num_cols1 = len(matrix1[0])
# num_rows2 = len(matrix2)
# num_cols2 = len(matrix2[0])

# if num_cols1 != num_rows2:
#     print("Matrix multiplication is not possible due to incompatible dimensions.")
# else:
#     result_matrix = [[0] * num_cols2 for _ in range(num_rows1)]

#     for i in range(num_rows1):
#         for j in range(num_cols2):
#             for k in range(num_cols1):
#                 result_matrix[i][j] += matrix1[i][k] * matrix2[k][j]

#     print("Resultant Matrix:")
#     for row in result_matrix:
#         print(row)

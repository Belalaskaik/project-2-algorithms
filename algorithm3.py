# Open the file named "in2C.txt" in read mode and assign it to a variable named "f"
with open('in2C.txt', 'r') as f:
        # Read the entire content of the file and assign it to a variable named "content"
    content = f.read()
    # Split the content of the file into lines and assign it to a variable named "lines"

lines = content.split('\n')
# Remove the first line of "lines" as it is assumed to be a header
lines = lines[1:]
# Remove any empty lines from "lines"
lines = [line for line in lines if line.strip()]

# Define a function named "arrayslists" that takes a list of lines as input
def arrayslists(lines):
    # Create an empty list named "arrays"
    arrays = []
    # Iterate over each line in "lines"
    for line in lines:
        # If the line starts with "Array_", extract the list of integers from the line and append it to "arrays"
        if line.startswith('Array_'):
            # Extract the string containing the list of integers from the line
            arr_str = line[line.index('['):].strip()
            # Remove any square brackets from "arr_str"
            arr_str = arr_str.replace(']', '')
            arr_str = arr_str.replace('[', '')
            # Remove any spaces from "arr_str"
            arr_str = arr_str.replace(' ', '')
            # Remove any trailing commas from "arr_str"
            if arr_str[-1:]== ",":
                arr_str = arr_str[:-1]
            # Remove any leading or trailing spaces from "arr_str"
            arr_str = arr_str.strip()
            # Split "arr_str" into a list of integers and append it to "arrays"
            arrays.append(arr_str[:].split(","))
        # If the line does not start with "Array_"
        else:
            # Remove any square brackets from the line
            arr_str = line
            arr_str = arr_str.replace(']', '')
            arr_str = arr_str.replace('[', '')
            arr_str = arr_str.replace('[', '')
            # Remove any spaces from the line
            arr_str = arr_str.replace(' ', '')
            arr_str = arr_str.strip()
            if arr_str[-1:]== ",":
                arr_str = arr_str[:-1]
            # Remove any leading or trailing spaces from the line
            arr_str = arr_str.strip()
            # Split the line into a list of integers and append it to "arrays"
            arrays.append(arr_str[:].split(","))
    # Return the list of lists named "arrays"
    return arrays

# Define a function named "merge_and_sort" that takes a list of lists of integers as input
def merge_and_sort(lists):
    merged_list = []
    for sublist in lists:
        for element in sublist:
            merged_list.append(int(element))
    merged_list.sort()
    return merged_list

# Call the "arrayslists" function with "lines" as input and assign the resulting list of lists to a variable named "inputLists"
inputLists = arrayslists(lines)

array_1 = inputLists[0:3]
array_1 = merge_and_sort(array_1)
array_2 = inputLists[4:7]
array_2 = merge_and_sort(array_2)
array_3 = inputLists[7:10]
array_3 = merge_and_sort(array_3)

print(f"Array_1 Output: {array_1} \nArray_2 Output: {array_2} \nArray_3 Output: {array_3}")

'''
Example :-

There are three substrings of length  to consider: 'AAA', 'BCA' 
and 'DDE'. The first substring is all 'A' characters, so . The 
second substring has all distinct characters, so . The third 
substring has  different characters, so . Note that a subsequence 
maintains the original order of characters encountered. The order 
of characters in each subsequence shown is important.
'''

def merge_the_tools(string, k):

    for i in range(0, len(string), k):

        part = string[i:i+k]

        result = ""

        for ch in part:

            if ch not in result:

                result += ch

        print(result)


if __name__ == '__main__':
    string, k = input("Enter S"), int(input("Enter N"))
    merge_the_tools(string, k)
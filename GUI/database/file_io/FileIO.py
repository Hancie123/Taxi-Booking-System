#Create new text file
#write content ontext file
#Read content from text file


FILE_NAME='data.txt'

#Create new text file
# file=open(FILE_NAME, 'r')
# print(file.read())
# file.close()

#write content ontext file
# file=open(FILE_NAME,'w' )
# file.write("Hello Nitesh!")
# file.close()

#Append content
# file=open(FILE_NAME, 'a')
# file.write("  Hello from PCPS College")
# file.close()

#Read content
file=open(FILE_NAME, 'r')
r=file.read()
print(r)

# slicing = create a substring by extracting elements from another string
#           indexing[] or slice()
#           [start:stop:step] = [0:15:2]
#           start n stop can be left empty [::2] default first and last character

#name = "Mihajlo Francic"

#first_name = name[:7]
#last_name = name[8:]
#rarted_name = name[0:15:2]
#reversed_name = name[::-1]

#print(first_name + " " + last_name)
#print(rarted_name)
#print(reversed_name)

website = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7,-4)

print(website[slice])
print(website2[slice])


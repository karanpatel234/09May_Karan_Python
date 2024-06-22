"""Write a Python program to find the first appearance of the substring 
'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the 
whole 'not'...'poor' substring with 'good'. Return the resulting string."""

test="The weather is not too poor today, but not great either."

# Statement before changing substring

print(test,"\n")

# Statement after changing substring

select_not=test.index("not")
select_poor=test.index("poor")

if select_not != -1 and select_poor != -1 or select_not < select_poor:
    result=test[:select_not] + "good" + test[select_poor + 4:]
    print(result,"\n")
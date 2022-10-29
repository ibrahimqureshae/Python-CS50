import emoji

#Take input arguments
emojize_input = input("Input: ").strip().lower()
print(f"Output:  {emoji.emojize(emojize_input)}")
#output the resultant emoji
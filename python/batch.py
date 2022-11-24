content_list=['ali', 'baba', 'bujang', 'lapuk', 'boi']
batch_size=2
batched_message=[]

for content in range(0,len(content_list), batch_size):
    result = " ".join(content_list[content:content+batch_size])
    batched_message.append(result)
    
for stuff in batched_message:
    print(stuff)
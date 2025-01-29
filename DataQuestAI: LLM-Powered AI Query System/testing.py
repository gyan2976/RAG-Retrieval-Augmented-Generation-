from langchain.text_splitter import RecursiveCharacterTextSplitter

# Test functionality to ensure it works
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
text = "This is a long text that should be split into smaller chunks for processing."
split_text = text_splitter.split_text(text)
print(split_text)
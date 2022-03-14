# Slice list into 3 equal chunks and reverse each chunk

sample_list = [11, 45, 8, "a", "b", "c", 78, 45, 89]

print("Original list ", sample_list)

length = len(sample_list)
chunk_size = int(length / 3)
start = 0
end = chunk_size

# run loop 3 times for 3 chunks
for i in range(3):
    indexes = slice(start, end)

    list_chunk = sample_list[indexes]
    print("Chunk ", i, list_chunk)

    print("After reversing it ", list(reversed(list_chunk)))

    start = end
    end += chunk_size
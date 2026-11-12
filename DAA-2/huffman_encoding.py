import heapq

def huffman(characters, frequencies):

    heap = [[frequencies[i], characters[i]] 
            for i in range(len(characters))]

    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        new_node = [left[0] + right[0], left, right]
        heapq.heappush(heap, new_node)

    def print_codes(node, code=""):

        if len(node) == 2:
            print(node[1], ":", code if code else "0")
            return

        print_codes(node[1], code + "0")
        print_codes(node[2], code + "1")

    print("\nHuffman Codes:")
    print_codes(heap[0])


characters = input("Enter characters separated by space: ").split()
frequencies = list(map(int, input("Enter frequencies: ").split()))

huffman(characters, frequencies)
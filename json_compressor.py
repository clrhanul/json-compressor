class JC_BASE_EXTRA_TYPES:
    pass

def compress_json(json_data: dict):
    k_list = []
    v_list = []
    w = [json_data]
    while w:
        a = w.pop()
        if isinstance(a, dict):
            for k, v in a.items():
                k_list.append(k)
                w.append(v)
            continue
        if isinstance(a, list):
            for i in a:
                w.append(i)
            continue
        v_list.append(a)
    
    # TODO: make code

    return k, v_list

def uncompress_json(compressed_data: bytes):
    # TODO: make code
    pass


if __name__ == "__main__":
    import json

    print("Compressed:")
    with open("example.json", "rb") as f:
        data = json.load(f)
    print(compress_json(data))

    print("Uncompressed:")
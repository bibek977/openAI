import tiktoken

def count_token(string : str,encoding_name : str) -> int:
    """return a number of token"""
    num_tokens = tiktoken.get_encoding(encoding_name).encode(string)
    return num_tokens

print(count_token.__doc__)
print(count_token("how many token will it occupy","cl100k_base"))


def reverse_token(token : int, encoding_name : str) ->str :
    '''return a string'''
    encoding = tiktoken.get_encoding(encoding_name)
    # string = encoding.decode(token)
    string = [encoding.decode_single_token_bytes(t) for t in token]
    return string

print(reverse_token.__doc__)
print(reverse_token([5269, 1690, 4037, 690, 433, 48678],'cl100k_base'))
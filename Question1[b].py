def keyword_segmentation(user_query, marketing_keywords_dictionary):
    word_set = set(marketing_keywords_dictionary)
    memo = {}

    def dfs(s):
        if s in memo:
            return memo[s]
        if not s:
            return [""]

        res = []
        for word in word_set:
            if s.startswith(word):
                rest_sentences = dfs(s[len(word):])
                for sentence in rest_sentences:
                    res.append(word + " " + sentence if sentence else word)
        memo[s] = res
        return res

    return dfs(user_query)


# Example Usage
user_query = "visitkathmandunepal"
keywords = ["visit", "kathmandu", "nepal", "visitkathmandu", "kathmandunepal"]
print(keyword_segmentation(user_query, keywords))

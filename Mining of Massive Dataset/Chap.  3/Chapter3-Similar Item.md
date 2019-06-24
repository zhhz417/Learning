#### Chapter 3: Similar Items

------------

- **Jaccard Similarity**
	Set S, T :  Sim(S,T) = |Intersection of S,T| / |Union of S,T|  
	- Suitable for searching similar text on the massive corpus(only text not semantic). 
	- eg. copy document(Plagiarism); Mirror Pages; Articles from same source.

------------

- **Collaborative Filtering**  
	- eg. Online shopping: We can say two customers are same, if their sets of purchased item have the high Jaccard similarity, should be noticed when its over 20%;
	Movie ratings: finding the similar movies according to the same customers, their favorite.
More detail on chapter 9

------------

- **Shingling of Document**  
	- **k-shingle:** any substring of length k characters within the document.
	- **the value of k** depends on the specific keywords of the specific document. k should be picked large enough that the probability of any shingle appearing in any document is low. (eg. for email, usually using k=5, for large document usually k=9)
	- **Hasing Shingles:**
	- **Word-Based Shingling:** w-shingling, which is composed of contiguous subsequences of tokens within a document, [https://en.wikipedia.org/wiki/W-shingling](https://en.wikipedia.org/wiki/W-shingling)

------------
- **3.3 Similarity-Preserving Summaries of Sets**
	Sets of shingles are very large, so we can use called 'signature' instead of the big sets, which are very small and representive. eg. We can compare the signature sets of two docs to estimate the Jaccard Similarity of the underlayiny(shingle) sets from the signature alone.
	- **Matrix Representation of Sets:** Create a characteristic matrix before building signatures. 
	column: the corresponding set (subset), eg. S1={a,b}; 
	row: the universal set (the set of all elements), eg. S={a,b,c,d,e}.
	- **Minihasing:** For the characteristic matrix, pick a permutation of the rows. The mini hash value of any column(subset) is the value of the first row, in which the column has '1'.

| Element  |  S1 |S2 |S3 |S4   |
| :------------: | :------------: | :------------: | :------------: | :------------: |
|  b |  0 |  0 |  1 |  0 |
|  e |  0 |  0 |  1 |  0 |
|  a |  1 |  0 |  0 |  1 |
|  d |  1 |  0 |  1 |  1 |
|  c |  0 |  1 |  0 |  1 |

- **3.3.3 Minihash and Jaccard Similarity**
	- 两个集合经随机排列转换后得到的两个最小哈希值相等的概率 = 这两个集合的Jaccard相似度
	 prove : Set S1, S2; three classes of rows.
	 		Type X rows have 1 in both columns.
			Type Y rows have 1 in one of the columns and 0 in the other.
			Type Z rows have 0 in both columns.
		SIM(S1, S2) = x/(x+y);  h(S1) = h(S2) = x/(x+y)
		
- **3.3.4 Minihash Signatures**
	 - Characteristic Matrix M, select n different permutation of the row randomly.
	 - The minihash signature for Set S: vector [h1(S), h2(S),..., hn(S)]

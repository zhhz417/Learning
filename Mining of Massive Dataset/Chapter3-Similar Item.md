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


# Analysis

## Layer 1, Head 3

this head pay attention to the CLS token or beginning of the sentence. show one darker gray scale attention on SEP token but thats it.
also its show some consistent attention line on [MASK] or the word that i want model to predict,, but the attention is not strong as CSL token..  

Example Sentences:
- We turned down a narrow lane and passed through a small [MASK].
- i eat the whole [MASK].
- i put the [MASK] on the tabel.

## Layer 1, Head 11

in this layer the attention is strongly focus to the word 'lane' and 'small'. these are the brightest squares.. 
also its show darker and brighter diagonal score pattern on
other words in the  sentence. in head 3 the attention is prominently directed towards the CLS token. in contrast,head 11 also shows attention towards the CLS token but not as strongly as head 3.      

Example Sentences:
- We turned down a narrow lane and passed through a small [MASK].
- then i [MASK] book on the tabel 


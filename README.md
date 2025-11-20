# Verse-Sorter
Program that lets users group certain blobs of text together spending on their separation as line-breaks. Easiest to show as an example:
"Jesus is LORD
Jesus is LORD
Jesus is LORD
Jesus is LORD



Jesus is LORD
Jesus is LORD
Jesus is LORD"
The program would see that there are three line-breaks between the four-string of "Jesus is LORD", and the three-string. It would then group that text into the following:
"Jesus is LORD Jesus is LORD Jesus is LORD Jesus is LORD
Jesus is LORD Jesus is LORD Jesus is LORD"
The reason I wrote it like this is because I needed a program that could organize text where each word was seperated by a paragraph break, but could sort them out in their original ordering. Sounds weird, but it was for very spesific use-case. I'm uploading it encause anyone else would like to use it.
Works for Hebrew as well. 
The default is set to 3 line breaks because that's what I needed it for, but you can change it in the Source Code for what you need. 
As far as I can tell, this only works for ".txt" files, and only works on Windows.

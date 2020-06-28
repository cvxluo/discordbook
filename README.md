
A discord py module for neater displays of data.

Terminology:
Book - overall object
Chapter - group of lines
Line - particular item inside the book
Page - Combination of chapter headers and lines that can be displayed on the embed

Maybe develop ordering of chapters based of lt? (less than)
Generate all pages at the start, then parse through
Bookmark feature to come back to this page after?

Books are static once generated

Make custom options for browsing - a custom parameter that takes a dict of possible emoji - page change combinations?
Note that the whole process is blocking right now because of the while True
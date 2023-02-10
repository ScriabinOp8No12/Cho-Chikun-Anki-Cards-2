To access the completed Cho Chikun Anki deck, please download and open the Cho Chikun PDF2.apkg file


This project needed a few code adjustments from the first Cho Chikun PDF conversion.  

1. All the puzzles at the end of the pdf had the keyword "Diagram" instead of "Solution" or "Variation" for 
the location of where the puzzle begins.  I had to add that word into the list of text Pytesseract (the OCR) scans for.

2. One puzzle had an error in the PDF when the person scanned it.  The word "Pastern" was at the top of the page, instead
of "Pattern". I found this bug when I manually checked the question outputs and realized one puzzle was missing. 
My solution was adding the word "Pastern" as a string that Pytesseract looks for at the top of the page

3. Three other puzzles were not getting detected (Pytesseract wasn't finding the word "Pattern" at the top of the page) 
I realized my crop location of the image was not including the top of the page, so I increased Pytesseract's scanning
area to be 10 pixels more in the Y direction. This solved this bug.

4. Two other puzzles weren't getting detected because Pytesseract incorrectly detected the word "Solution" as "solution" 
Luckily, there weren't any other lower case solution words in the middle of the PDF page, otherwise
there'd be a problem because my image crop would be cropping at the wrong section of the page.

5. My original code for the first Cho Chikun PDF needed to concatenate up to 2 answer images, but this 2nd Cho Chikun
PDF needed up to 3 pages concatenated.  Surprisingly, the code worked for concatenating 3 answer images so I didn't
need to modify any of that code.  


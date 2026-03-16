# La Circe

This is a transcription of Giovanni Battista Gelli's La Circe, as translated by Thomas Brown.

[This translation](https://archive.org/details/b30535827/page/n7/mode/2up), published 1702, is in the public domain, but I had difficulty finding a clean transcription of it online, with the automated OCR texts plagued by the menace of the 'long s'.

So here is a new transcription, using Claude Opus 4.6. I've instructed the robot to modernize the s's, while otherwise leaving the old timey spelling in tact.

[Read it online](https://rmwinslow.com/circe) | 


## Process

1. Go to the [Internet Archive scan](https://archive.org/details/b30535827/page/n7/mode/2up), and download the `SINGLE PAGE PROCESSED JP2 ZIP`. Extract it into the `pages/` folder.
2. Run `resize_pages.py` to scale the images down to about 1 megapixel each.
3. Ask the LLM to batch transcribe the images using the transcribe skill. Each page is converted to a single text file in `pages/txt/`
4. After the text is extracted, run `merge_pages.py` to generate the final markdown pages, which are served using Github Pages.


## Repository structure



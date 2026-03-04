#progam for list that have a specific word count

from loguru import logger

count=0
paragraph="""The morning sun spilled softly across the quiet streets, painting the old buildings in shades of gold and amber. A gentle breeze carried the scent of fresh rain, even though the sky was perfectly clear. Somewhere in the distance, a bicycle bell rang twice before fading into silence."""
paragraph1=paragraph.split(" ")
for letters in paragraph1:
    if letters=="the":
        count+=1
    else:
        continue

logger.info(f"the count of word 'THE' is {count}.")
        

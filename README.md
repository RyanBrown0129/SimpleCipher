# SimpleCipher
A Python cipher program I did as a project at SIUc.  All valid keys: ABCDEFGHIJKLMNOPQRSTUVWXYZ,.-_
You type in a key for the cipher to use.  The key controls how much the letters are shifted.  The shifted letter replaces the letter in the key it was shifted by so the key is always changing to make the cipher more difficult to break.

The key and plain texted is converted to numbers then the plain text number and key number is added together.  That number is taken by modulos 30 and that final number is converted back to a letter or special character.

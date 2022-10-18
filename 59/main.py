#  Created by Simone Margio
#  www.simonemargio.im

# Problem: someone has attempted to censor my strings by replacing every vowel with a *, l*k* th*s. Luckily,
# I've been able to find the vowels that were removed.
# Given a censored string and a string of the censored vowels, return the original uncensored string
# Info: the vowels are given in the correct order!
# Input: censored string + vowels
# Output: uncensored string
# Es: "Wh*r* d*d my v*w*ls g*?", "eeioeo" -> Where did my vowels go?
# Es: "W*W, s* m*ch m*g*c!", "oouai" -> WoW, so much magic!

def uncensored(txt, vowels):
    return txt.replace('*', '{}').format(*vowels)


print(uncensored("Wh*r* d*d my v*w*ls g*?", "eeioeo"))
print(uncensored("W*W, s* m*ch m*g*c!", "oouai"))

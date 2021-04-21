#!bin/bash 

#download a text file from ftp://sunsite.informatik.rwth-aachen.de/pub/mirror/ibiblio/gnome/README if it is not yet present in the current directory (use wget for this).

if [[ ( -f "README" ) ]]; then
  echo "file with this name already present in the current directory"
else
wget "ftp://sunsite.informatik.rwth-aachen.de/pub/mirror/ibiblio/gnome/README"
fi

#read file README
cat README |

#make all text lowercase (use tr)
tr '[:upper:]' '[:lower:]' |

#split it into individual words per line (use cat and/or sed for this) - aka replace spaces with a newline and remove special charakters and separators used in README
sed 's/ /\n/g' |
tr -d [:punct:] |
tr -d [:digit:] |
sed '/^$/d' |

#alphabetically sort the list of words and remove duplicates (sort and uniq, possibly also grep)
sort |
uniq -c |

#print out the 10 most common words in the text (without number of occurrences) on stdout (uniq, sort, and head)
sort -r |
head -n 10 |
tr -d [:digit:]

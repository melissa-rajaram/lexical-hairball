#! /usr/bin/python
""" 
    This class is used to extract the orthographic forms from the SALT-generated Root Word List (RWL)
    - For each orthographic form, also extracts the total number of times the form was used across all
      the transcripts, and the percentage of individuals that used each word
    - Contains the total number of transcripts used. This was previously calculated from the directory
      of files that contain the transcripts (not contained in RWL)
    - the type of data returned is a defaultdict(dict), which is a nested hash table containing the
      following form:
      
      RWL_words[orthographic_word] -> [TOKEN] -> total number of times the word used across all transcripts
      RWL_words[orthographic_word] -> [NUMCHILD] -> percentage of transcripts that contain the word 

    SANITY CHECK: SANE
    - The format of SALT RWL files is a header, and then orthographic words in transcripts, organized 
      with one orthographic word per line. Since this class extracts all orthographic forms from the 
      transcripts, the number of forms extracted should be one less than the number of lines in the 
      RWL file. Below is the number of lines in each file, as counted by the 'wc -l' command in the 
      linux environment. 
      
      6104 three_adult.CSV
      3742 three_child.CSV
      6043 four_adult.CSV
      3768 four_child.CSV
      6601 six_adult.CSV
      4467 six_child.CSV
    
    - When this program is run by itself, it produces the following information:
      entries from three adult RWL 6103
      entries from three child RWL 3741
      entries from four adult RWL 6042
      entries from four child RWL 3767
      entries from six adult RWL 6600
      entries from six child RWL 4466
      
    - CONCLUSION:
      This program is functioning as expected because the number of entries in the data returned from
      a single RWL is one less than the total number of lines in the file.

    LAST EXAMINED: 8-23-18
    STATUS: - can be used as a mininal sanity check in rajaram_dissertation,
              but unused in dissertation
            - probably not DRY, but usable

"""
from collections import defaultdict
from completed_projects.rajaram_dissertation.locations import Locations


class RootWordList():

    def __init__(self):
        pass

    def orthographic_from_rwl(self, rwl_file):
        # extracts each orthographic form from the SALT RWL

        orth_words = defaultdict(dict)

        f = open(rwl_file, "r")
        f.readline()
        for line in f.readlines():
            wordInfo = line.strip()
            wordInfo = wordInfo.split(",")
            #
            orth_words[wordInfo[0].lower()]['TOKEN'] = wordInfo[3]
            #
            orth_words[wordInfo[0].lower()]['NUMCHILD'] = wordInfo[1]
        f.close()

        return orth_words

if __name__ == "__main__":
    TEST = RootWordList()
    L = Locations()
    print('entries from three adult RWL', len(TEST.orthographic_from_rwl(L.threeAdultSALT)))
    print('entries from three child RWL',len(TEST.orthographic_from_rwl(L.threeChildSALT)))
    print('entries from four adult RWL', len(TEST.orthographic_from_rwl(L.fourAdultSALT)))
    print('entries from four child RWL', len(TEST.orthographic_from_rwl(L.fourChildSALT)))
    print('entries from six adult RWL', len(TEST.orthographic_from_rwl(L.sixAdultSALT)))
    print('entries from six child RWL', len(TEST.orthographic_from_rwl(L.sixChildSALT)))


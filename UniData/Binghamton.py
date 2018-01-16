'''
Created on Jan 15, 2018

@author: Doeun Kim
'''

class Binghamton(object):
    '''
    classdocs : Data regarding Binghamton
    '''


    def getLetterGrades(self):
        letterGrades = ['A','A-','B+','B','B-','C+','C','C-','D','F']
        grades=[4.00,3.70,3.30,3.00,2.70,2.30,2.00,1.70,1.00,0.00]
        return {'LetterGrades':letterGrades,'Grades':grades}
        
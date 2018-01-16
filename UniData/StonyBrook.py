'''
Created on Jan 15, 2018

@author: Doeun Kim
'''

class StonyBrook:
    '''
    classdocs: Data regarding Stony Brook
    '''


    def getLetterGrades(self):
        letterGrades = ['A','A-','B+','B','B-','C+','C','C-','D+','D','F','Q']
        grades=[4.00,3.67,3.33,3.00,2.67,2.33,2.00,1.67,1.33,1.00,0.00,0.00]
        return {'LetterGrades':letterGrades,'Grades':grades}
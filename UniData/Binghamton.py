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
        grades=[4.0,3.7,3.3,3.0,2.7,2.3,2.0,1.7,1.0,0.0]
        return {'LetterGrades':letterGrades,'Grades':grades}
        
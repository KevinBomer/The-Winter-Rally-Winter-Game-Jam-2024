init python:

    class base_class(renpy.python.RevertableObject):

        def __getstate__(self):
            return vars(self).copy()

        def __setstate__(self,new_dict):
            self.__dict__.update(new_dict)

    class player(base_class):
        '''
        Player Class where we can init the player
        '''

        def __init__(self):
            """
            Init of the Player
            The following attributes will be instantiated:
            """

            self.player_name = "Player Name"
            self.relationships = {}
            self.choices = []

        def clamp(self, value, minValue, maxValue):
            '''
            Clamp the provided value between the provided min and max bounds.
            '''
            return max(min(maxValue, value), minValue)

        def addRelationship(self, character):
            '''
            Add one relationship to list
            '''

            self.updateRelationship(character, 0)

        def increaseRelationship(self, character, value, showui=True, showui_duration=2.5):
            '''
            Increment Relationship
            '''

            if character not in self.relationships:
                self.updateRelationship(character, 0)
            
            if showui:
                show_expbar_multiple((
                        (character, self.relationships[character], self.clamp(self.relationships[character] + value, 0, 10)),
                    ), showui_duration
                )
            self.relationships[character] = self.clamp(self.relationships[character] + value, 0, 10)

        def increaseRelationshipMultiple(self, cp_dict, showui=True, showui_duration=2.5):
            '''
            Increment Relationship for multiple characters at once
            '''

            for character in cp_dict:
                if character not in self.relationships:
                    self.updateRelationship(character, 0)
            
            if showui:
                cplist = []
                for character in cp_dict:
                    from_val = self.getRelationship(character)
                    to_val = self.clamp(from_val + cp_dict[character], 0, 10)
                    cplist += ((character, from_val, to_val),)
                show_expbar_multiple(cplist, showui_duration)
            
            for character in cp_dict:
                self.relationships[character] = self.clamp(self.relationships[character] + cp_dict[character], 0, 10)

        def getRelationship(self, character):
            '''
            Get Relationship
            '''

            if character not in self.relationships:
                self.updateRelationship(character, 0)
            
            return self.relationships[character]

        def updateRelationship(self, character, value):
            '''
            Update one Relationship from the list
            '''

            self.relationships[character] = value

        def showRelationshipUI(self, characters, duration=2.5):
            '''
            Show the relationship points in the UI
            '''

            if type(characters) is str:
                characters = [characters]

            cplist = []

            for character in characters:
                p = self.getRelationship(character)
                cplist += ((character, p, p),)

            show_expbar_multiple(cplist, duration)

        def getHighestRankingRelationship(self):
            '''
            Get the relationship with the highest ranking.
            '''

            return max(self.relationships, key=self.relationships.get)

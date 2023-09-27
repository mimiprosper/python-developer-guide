class ParentProto:
    def __init__(self, father="james", mother="mary"):
        self.father = father
        self.mother = mother

    def p_name(self):
        return self.father, self.mother


class Character(ParentProto):
    def character_list(self):
        return {
            self.father: ['love traveling ', 'football', ],
            self.mother: [' cooking everday']
        }


class Likes:
    def att(self):
        get_parent = ParentProto().p_name()
        return {
            get_parent[0]: ['like vacation', 'like watching football'],
            get_parent[1]: ['like making dishes', "love to swim"]
        }


class ChilNode(Character, Likes):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.mother = ParentProto().p_name()[0]
        self.father = ParentProto().p_name()[0]

    def inheritance(self):

        def DRY(type, P, gen):
            global l_sententence, Like_sentence
            l_sententence = ""
            Like_sentence = ""
            call_like = self.att().get(P)
            call_character = self.character_list().get(P)

            for words in call_like:
                Like_sentence += words + ","

            for words in call_character:
                l_sententence += words + ","

            print(f"""
            {P} is the {type} of {self.name} and the behave the same way which is..
            {l_sententence}
            """)
            print(f"""
            {self.name} and {gen} {P} like the same thing which is...
            {Like_sentence}
            """)

        if self.gender == "male":
            DRY("father", gen="his father", P=self.father)
        elif self.gender == "female":
            DRY("mother", self.mother, "her mother")


ParentProto()
caller = ChilNode("chibuike", "male")
caller = ChilNode("joy", "female")
caller.inheritance()

 
from JSITA.mainapp.models import Offer, Skill


def offer_not_id_db(link):
    pass


def add_to_db(offer_details):

    Offer.objects.create(url=offer_details['url'],
                         name=offer_details['name'],
                         location=offer_details['location'],
                         company=offer_details['company'],
                         salary=offer_details['salary'],
                         date_added=offer_details['date'],
                         exp=offer_details['exp'],
                         )


def skill_not_in_db(skill):
    pass


def create_skills(skills):
    for skill in skills:
        if skill_not_in_db(skill):
            sk = Skill.objects.create(name=skill)

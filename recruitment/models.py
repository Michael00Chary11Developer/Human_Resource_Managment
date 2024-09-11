from django.db import models


class Recruitment(models.Model):
    """_summary_
    ID is the primary key. It fills automatically
    condition_choices and possition_choices must be chosen in recruitment_condition and recruitment_possition
    """
    rec_id = models.AutoField(primary_key=True)
    condition_choices = [
        ("Accept", "accepted"),
        ("Reject", "reject"),
        ("Uncertain", "uncertain"),
    ]
    possition_choices = [
        ("Nothing", "nothing"),
        ("Front End Developer", 'Front end Developer'),
        ("Back End Developer", "back end developer"),
        ("Full Stack Developer", "full stack developer"),
        ("DevOps Engineer", "devOps engineer"),
        ("UX/UI Designer", "UX/UI designer"),
        ("Network Engineer", "network engineer"),
    ]

    recruitment_possition = models.CharField(
        max_length=50, choices=possition_choices, default='Nothing')

    """
    get the resume
    and see how many time spent for interviews
    and date of recruiment
    by models
    recieved_resume , checked_resume , approved_resume , interviewed_resume get positive integer
    time_sepnt_interview is durationfield get timedelta object =>hours:minutes:secconds
    recruiment_condition about condotion of interview reject or accept
    date_recruiment is the date of the interview is datetefield and get object of datefield
    """

    recieved_resume = models.PositiveIntegerField()
    checked_resume = models.PositiveIntegerField()
    approved_resume = models.PositiveIntegerField()
    interviewed_resume = models.PositiveSmallIntegerField()
    time_spent_interview = models.DurationField()
    recruitment_condition = models.CharField(
        max_length=50, choices=condition_choices, default='Uncertain')
    date_recruitment = models.DateField()

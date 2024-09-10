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

    recieved_resume = models.PositiveIntegerField()
    checked_resume = models.PositiveIntegerField()
    approved_resume = models.PositiveIntegerField()
    interviewed_resume = models.PositiveSmallIntegerField()
    time_spent_interview = models.DurationField()
    recruitment_condition = models.CharField(
        max_length=50, choices=condition_choices, default='Uncertain')
    date_recruitment=models.DateField()  

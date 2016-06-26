from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
from django.forms import ModelForm,TextInput,CheckboxSelectMultiple,Textarea

# Create your models here.


class signup_form(UserCreationForm):
    username = forms.RegexField(
        label=_("Username"), max_length=30, regex=r"^[\w.@+-]+$",
        error_messages={
            'invalid': _("This value may contain only letters, numbers and "
                         "@/./+/-/_ characters.")},
        widget=forms.TextInput(attrs={'class': 'form-control',
                                'required': 'true',
                                })
    )

    email = forms.CharField(
        label=_("Email"),
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'type': 'email',
                                      'required': 'true'
                                      })
    )

    password1 = forms.CharField(
        label=_("Password"),
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'required': 'true',

                                          })
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'type': 'password',
                                          'required': 'true',
                                          }),
    )

    class Meta:
        model = User
        fields = ['username','email','password1','password2']


faculty_choices = [('arts and social sciences','Arts and Social Sciences'),
                   ('computing','Computing'),
                   ('science','Science'),
                   ('business','Business'),
                   ('dentistry','Dentistry'),
                   ('design & environment','Design & Environment'),
                   ('duke-nus','Duke-NUS'),
                   ('engineering','Engineering'),
                   ('law','Law'),
                   ('medicine','Medicine'),
                   ('music','Music'),
                   ('yale-nus','Yale-NUS'),
                   ]
                   
grade_choices = [("a+", "A+"), 
		 ("a","A"), 
		 ("a-","A-"), 
		 ("b+","B+"), 
		 ("b","B"), 
		 ("b-","B-"),
		 ("c+", "C+"),
		 ("c", "C"),
		 ("d+", "D+"),
		 ("d", "D"),
		 ("f", "F"),
		 ]

semester_choices = [('sem1', "Semester 1"),
	            ('sem2', 'Semester 2"),
	            ]


class Tutee(models.Model):
    user = models.OneToOneField(User,null=True,blank=True,related_name='profile')
    faculty = models.CharField(max_length=20,choices=faculty_choices,blank=True,default='Null')
    matric_photo = models.ImageField(upload_to='matric_photo/',max_length=1000,blank=True,default='Null')
    is_verified_student = models.NullBooleanField(blank=True,default='Null')
    profile_pic = models.ImageField(upload_to='profile_pic/',max_length=1000,blank=True,default='profile_pic/default profile picture.png')


def create_user_profile(sender,instance, created, **kwargs):
    if created:
        Tutee.objects.create(user=instance)

post_save.connect(create_user_profile,sender=User)


year_of_study_choices = [('year 1','Year 1'),('year 2','Year 2'),('year 3','Year 3'),('year 4','Year 4')]


class tuition_type_choices(models.Model):
    tuition_choice = models.CharField(max_length=20)

    def __str__(self):
        return self.tuition_choice


class schedule_choices(models.Model):
    schedule_choice = models.CharField(max_length=30)

    def __str__(self):
        return self.schedule_choice


class tutor(models.Model):
    user = models.ForeignKey(User,blank=True,unique=True,verbose_name='user')
    faculty = models.CharField(max_length=30,choices=faculty_choices,blank=False,default='')
    major = models.CharField(max_length=100)
    year_of_study = models.CharField(max_length=10,choices=year_of_study_choices,blank=False,default='')
    preferred_tuition_type = models.ManyToManyField(tuition_type_choices)
    preferred_schedule = models.ManyToManyField(schedule_choices)
    description = models.TextField(max_length=10000)


class tutor_form(forms.ModelForm):
    preferred_tuition_type = forms.ModelMultipleChoiceField(queryset=tuition_type_choices.objects.all(), required=False, widget=forms.CheckboxSelectMultiple())
    preferred_schedule = forms.ModelMultipleChoiceField(queryset=schedule_choices.objects.all(), required=False, widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = tutor
        exclude = ['user']
        labels = {
            'faculty': _('Faculty*:'),
            'major':_('Major*'),
            'year_of_study':_('Year of study*'),
            'preferred_tuition_type':_('Preferred tuition type* (multiple selection allowed)'),
            'preferred_schedule':_('Preferred tuition schedule* (multiple selection allowed)'),
            'description':_('Description about yourself* (maximum 150 words)')
        }
        widgets = {
            'description': Textarea(attrs={'cols':100})
        }

class Module(models.Models):
	mod_code = models.CharField(max_length=10, blank = False, primary_key=True)
	mod_name = models.CharField(max_length=30, blank = False, default='')

class tutor_mod(models.Model):
	mod_code = models.ForeignKey(Module, blank=False, verbose_name='module code', on_delete=models.CASCADE)
	user = models.ForeignKey(User,blank=False,unique=True,verbose_name='user', on_delete=models.CASCADE)
	grade = models.CharField(max_length=5, choices=grade_choices, blank=False, default="")
	ave_rating = models.CharField(max_length=3)
	is_certified_tutor = models.NullBooleanField(blank=False, default="Null")
	transcript_photo = models.ImageField(upload_to='transcript_photo/',max_length=100, blank=True, default='Null')
	semester_taken= models.CharField(max_length=10, choices=semester_chices, blank=False, default="")
	year_taken = models.CharField(max_length=4, blank=False, default='') 
	review = models.CharField(max_length=10000)

from django.db import models

# Create your models here.
class District(models.Model):
    name=models.CharField(max_length=250,unique=True,blank=False)
    district_link=models.TextField()


    def __str__(self):
        return self.name

class Banks(models.Model):
    district=models.ForeignKey(District,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    class Meta:
        ordering=("district",)
        verbose_name='Bank'
        verbose_name_plural='Banks'

    def __str__(self):
        return self.name

class Account(models.Model):
    account_type=models.CharField(max_length=25,blank=False)
    class Meta:
        ordering=('account_type',)

    def __str__(self):
        return self.account_type
class Details(models.Model):
    name=models.CharField(max_length=250, blank=False)
    dob=models.DateField(max_length=8)
    age=models.IntegerField()
    gender=models.CharField(max_length=10)
    pnumber=models.CharField(max_length=13)
    mailid=models.EmailField()
    address=models.TextField(max_length=250)
    district=models.ForeignKey(District,on_delete=models.SET_NULL,null=True)
    branch=models.ForeignKey(Banks,on_delete=models.SET_NULL,null=True)
    # banks=models.ForeignKey(Banks,on_delete=models.CASCADE)
    account_type=models.ForeignKey(Account,on_delete=models.CASCADE)
    debit_card=models.BooleanField(default=False)
    credits_card=models.BooleanField(default=False)
    online_banking=models.BooleanField(default=False)

    class Meta:
        ordering=('name',)
        verbose_name='Detail'
        verbose_name_plural='Details'

    def __str__(self):
        return self.name




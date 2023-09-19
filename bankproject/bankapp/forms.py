from django import forms
from django.forms import DateInput

from . models import Details,Banks


class DetailsForm(forms.ModelForm):
    class Meta:
        model= Details
        fields= ('name','dob',
                'age','gender',
                'pnumber','mailid',
                'address','district','branch',
                'account_type','debit_card',
                'credits_card','online_banking')

        labels = {'dob': ('D.O.B'),
                    }
        widgets = {
                    'dob': DateInput(attrs={'type': 'date'})
                    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['branch'].queryset = Banks.objects.none()

        if 'district' in self.data:
            try:
                district_id = int(self.data.get('district'))
                self.fields['branch'].queryset = Banks.objects.filter(district_id=district_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['branch'].queryset = self.instance.district.branch_set.order_by('name')

    # def __int__(self,*args,**kwargs):
    #     super().__init__(*args,**kwargs)
    #     self.fields['branch'].queryset=Banks.objects.none()
    #
    #     if 'district' in self.data:
    #         try:
    #             district_id = int(self.data.get('district'))
    #             self.fields['branch'].queryset = Banks.objects.filter(district_id=district_id).order_by('branch')
    #         except (ValueError, TypeError):
    #             pass  # invalid input from the client; ignore and fallback to empty City queryset
    #     elif self.instance.pk:
    #         self.fields['branch'].queryset = self.instance.district.branch_set.order_by('branch')
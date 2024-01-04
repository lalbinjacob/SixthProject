from django import forms

from storeapp.models import Ordering, Course

Gender_choices=[
    ('Male','Male'),
    ('Female','Female'),
    ('Others','Others')
]

Materials_choices=[
    ('Note book','Note book'),
    ('Pen','Pen'),
    ('Lab products','Lab products'),
    ('Question paper','Question paper'),
    ('Guide book','Guide Book'),
    ('Test book','Test book')
]

class OrderingCreationForm(forms.ModelForm):
    gender=forms.ChoiceField(choices=Gender_choices,widget=forms.RadioSelect)
    materials_provide=forms.MultipleChoiceField(label='Materials',choices=Materials_choices,widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Ordering
        fields = ['name','birthdate','gender','age','phone_number','address','email','department',
                  'course','purpose','materials_provide'
        ]

        labels = {
                'name':'Name',
                'birthdate':'Date of Birth',
                'phone_number':'Mobile No',
                'email':'Email ID',
                'materials_provide':'Materials Provide',
        }
        widgets = {
                 'name':forms.TextInput(attrs={'class':'form-control'}),
                 'birthdate':forms.DateInput(attrs={'class':'form-control','id':'datepicker'}),
                 'phone_number':forms.NumberInput(attrs={'class':'form-control',}),
                 'address':forms.Textarea(attrs={'class':'form-control'}),
                 'email':forms.EmailInput(attrs={'class':'form-control'})

        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['course'].queryset = Course.objects.none()

        if 'department' in self.data:
            try:
                department_id = int(self.data.get('department'))
                self.fields['course'].queryset = Course.objects.filter(department_id=department_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['course'].queryset = self.instance.department.course_set.order_by('name')
from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate
from .models import CustomUser,Student
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Submit, Layout, Field
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit

class userRegistrationForm(UserCreationForm):
   # password = forms.CharField(widget=forms.PasswordInput)
   # confirm_password = forms.CharField(widget=forms.PasswordInput)
   class Meta :
    model = CustomUser
    fields =('registration_no','email','password')
   
   def clean(self):
        cleaned_data = super(userRegistrationForm, self).clean()
        password = cleaned_data.get('password')
        # confirm_password = cleaned_data.get('confirm_password')
        # if password != confirm_password:
        #     raise forms.ValidationError("Passwords do not match")
        return cleaned_data


class userLoginForm(forms.ModelForm):
      class Meta:
        model = CustomUser
        fields = ('registration_no','password')
      def clean(self):
         if self.is_valid():
            registration_no = self.cleaned_data['registration_no']
            password = self.cleaned_data['password']

            if not authenticate(registration_no=registration_no,password=password):
               raise forms.ValidationError('please provide registration no and password')
               
         
# class StepOneForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     department = forms.CharField(max_length=100)
#     session = forms.CharField(max_length=100)
#     reg_no = forms.CharField(max_length=100)
#     hall = forms.CharField(max_length=100)
#     email = forms.EmailField()
#     father_name = forms.CharField(max_length=100)
#     mother_name = forms.CharField(max_length=100)
#     present_address = forms.CharField(widget=forms.Textarea)
#     permanent_address = forms.CharField(widget=forms.Textarea)

#     helper = FormHelper()
#     helper.form_method = 'post'
#     helper.add_input(Submit('next', 'Next', css_class='btn-primary'))


# class StepTwoForm(forms.Form):
#     facebook_link = forms.URLField()
#     linkedin_link = forms.URLField(required=False)
#     ssc_institution = forms.CharField(max_length=100)
#     ssc_board = forms.CharField(max_length=100)
#     ssc_passing_year = forms.IntegerField()
#     hsc_institution = forms.CharField(max_length=100)
#     hsc_board = forms.CharField(max_length=100)
#     hsc_passing_year = forms.IntegerField()
#     photography = forms.BooleanField(required=False)
#     content_writing = forms.BooleanField(required=False)
#     debating = forms.BooleanField(required=False)
#     graphics_designing = forms.BooleanField(required=False)
#     web_development = forms.BooleanField(required=False)
#     hobbies = forms.CharField(max_length=100)

#     helper = FormHelper()
#     helper.form_method = 'post'
#     helper.add_input(Submit('back', 'Back', css_class='btn-secondary'))
#     helper.add_input(Submit('next', 'Next', css_class='btn-primary'))


# class StepThreeForm(forms.Form):
#     duits_reason = forms.CharField(widget=forms.Textarea)
#     it_interest = forms.CharField(widget=forms.Textarea)
#     other_clubs = forms.CharField(widget=forms.Textarea)
#     ms_word = forms.BooleanField(required=False)
#     adobe = forms.BooleanField(required=False)
#     canva = forms.BooleanField(required=False)
#     google_workspace = forms.BooleanField(required=False)
#     compilers = forms.BooleanField(required=False)

#     helper = FormHelper()
#     helper.form_method = 'post'
#     helper.add_input(Submit('back', 'Back', css_class='btn-secondary'))
#     helper.add_input(Submit('submit', 'Submit', css_class='btn-success'))

# class StudentForm(forms.ModelForm):
#     class Meta:
#         model = Student
#         fields = [
#             'name',
#             'department',
#             'session',
#             'registration_number',
#             'hall',
#             'email',
#             'fathers_name',
#             'mothers_name',
#             'present_address',
#             'permanent_address',
#             'social_media_link_1',
#             'social_media_link_2',
#             'ssc_institution',
#             'ssc_board',
#             'ssc_passing_year',
#             'hsc_institution',
#             'hsc_board',
#             'hsc_passing_year',
#             'photography',
#             'content_writing',
#             'debating',
#             'graphics_designing',
#             'web_development',
#             'hobbies_and_interests',
#             'why_join_duits',
#             'information_tech_interest',
#             'other_club_member',
#             'microsoft_word',
#             'microsoft_excel',
#             'adobe_illustrator_or_photoshop',
#             'canva',
#             'google_workspace',
#             'program_compilers',
#         ]

#     def __init__(self, *args, **kwargs):
#         super(StudentForm, self).__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.form_id = 'id-StudentForm'
#         self.helper.form_class = 'blueForms'
#         self.helper.form_method = 'post'
#         self.helper.form_action = 'submit_survey'
#         self.helper.add_input(Submit('submit', 'Submit'))

#         self.helper.layout = Layout(
#             Fieldset(
#                 'Step 1: Personal Information',
#                 'name',
#                 'department',
#                 'session',
#                 'registration_number',
#                 'hall',
#                 'email',
#                 'fathers_name',
#                 'mothers_name',
#                 'present_address',
#                 'permanent_address',
#             ),
#             Fieldset(
#                 'Step 2: Relevant Information',
#                 'social_media_link_1',
#                 'social_media_link_2',
#                 'ssc_institution',
#                 'ssc_board',
#                 'ssc_passing_year',
#                 'hsc_institution',
#                 'hsc_board',
#                 'hsc_passing_year',
#                 'photography',
#                 'content_writing',
#                 'debating',
#                 'graphics_designing',
#                 'web_development',
#                 'hobbies_and_interests',
#             ),
#             Fieldset(
#                 'Step 3: Extra Information',
#                 'why_join_duits',
#                 'information_tech_interest',
#                 'other_clubs',
#                 'microsoft_word',
#                 'microsoft_excel ',
#                 'adobe_illustrator_or_photoshop',
#                 'canva',
#                 'google_workspace',
#                 'program_compilers',
#             ),
#             ButtonHolder(
#                 Submit('submit', 'Submit', css_class='button white')
#             )
#         )
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'name',
            'department',
            'session',
            'registration_number',
            'hall',
            'email',
            'fathers_name',
            'mothers_name',
            'present_address',
            'permanent_address',
            'social_media_link_1',
            'social_media_link_2',
            'ssc_institution',
            'ssc_board',
            'ssc_passing_year',
            'hsc_institution',
            'hsc_board',
            'hsc_passing_year',
            'photography',
            'content_writing',
            'debating',
            'graphics_designing',
            'web_development',
            'hobbies_and_interests',
            'why_join_duits',
            'information_tech_interest',
            'other_club_member',
            'microsoft_word',
            'microsoft_excel',
            'adobe_illustrator_or_photoshop',
            'canva',
            'google_workspace',
            'program_compilers',
        ]
        fieldsets = (
            ('Step 1: Personal Information', {
                'fields': (
                    'name',
                    'department',
                    'session',
                    'registration_number',
                    'hall',
                    'email',
                    'fathers_name',
                    'mothers_name',
                    'present_address',
                    'permanent_address',
                )
            }),
            ('Step 2: Relevant Information', {
                'fields': (
                    'social_media_link_1',
                    'social_media_link_2',
                    'ssc_institution',
                    'ssc_board',
                    'ssc_passing_year',
                    'hsc_institution',
                    'hsc_board',
                    'hsc_passing_year',
                    'photography',
                    'content_writing',
                    'debating',
                    'graphics_designing',
                    'web_development',
                    'hobbies_and_interests',
                )
            }),
            ('Step 3: Extra Information', {
                'fields': (
                    'why_join_duits',
                    'information_tech_interest',
                    'other_club_member',
                    'microsoft_word',
                    'microsoft_excel',
                    'adobe_illustrator_or_photoshop',
                    'canva',
                    'google_workspace',
                    'program_compilers',
                )
            }),
        )

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-StudentForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.add_input(Submit('submit', 'Submit'))

        self.helper.layout = Layout(
            Fieldset(*self.Meta.fieldsets),
            ButtonHolder(
                Submit('submit', 'Submit', css_class='button white')
            )
        )
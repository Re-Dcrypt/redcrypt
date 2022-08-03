from django import forms
from allauth.account.forms import SignupForm, ResetPasswordForm
from accounts.models import Profile
from hcaptcha.fields import hCaptchaField


class MyCustomSignupForm(SignupForm):
    name = forms.CharField(required=False, label="Name [Optional]")
    organization = forms.CharField(
        required=False,
        label='School/Organization [Optional]'
        )
    hcaptcha = hCaptchaField(theme='dark')

    field_order = [
        'name',
        'organization',
        'username',
        'email',
        'password1',
        'password2',
        'hcaptcha']

    def save(self, request):
        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(MyCustomSignupForm, self).save(request)

        profile = Profile.objects.create(
            user=user,
            name=self.cleaned_data['name'],
            organization=self.cleaned_data['organization'],
            avatar_url=f"https://source.boringavatars.com/beam/{user.username}?colors=00D2D2,006D6D,002A2A,055D5D,074848"
            )
        profile.save()

        # Add your own processing here.

        # You must return the original result.
        return user


class CustomForgetPassword(ResetPasswordForm):
    hcaptcha = hCaptchaField(theme='dark')


class ContactForm(forms.Form):
    subject = forms.CharField(
        required=True,
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'text-nblue p-2'}))
    body = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'class': 'text-nblue p-2'}))
    hCaptcha = hCaptchaField(theme='dark')

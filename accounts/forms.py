from django import forms
from allauth.account.forms import SignupForm
from accounts.models import Profile


class MyCustomSignupForm(SignupForm):
    name = forms.CharField(required=False, label="Name [Optional]")
    organization = forms.CharField(
        required=False,
        label='School/Organization [Optional]'
        )

    def save(self, request):
        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(MyCustomSignupForm, self).save(request)

        profile = Profile.objects.create(
            user=user,
            name=self.cleaned_data['name'],
            organization=self.cleaned_data['organization']
            )
        profile.save()

        # Add your own processing here.

        # You must return the original result.
        return user

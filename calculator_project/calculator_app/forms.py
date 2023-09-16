from django import forms

class CalculatorForm(forms.Form):
    num1 = forms.FloatField(label='Enter first number')
    num2 = forms.FloatField(label='Enter second number')
    operator = forms.ChoiceField(
        label='Select operation',
        choices=[('+', 'Add'), ('-', 'Subtract'), ('*', 'Multiply'), ('/', 'Divide')]
    )

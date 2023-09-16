from django.shortcuts import render
from .forms import CalculatorForm

def index(request):
    return render(request , "home.html")

def calculator(request):
    if request.method == 'POST':
        form = CalculatorForm(request.POST)
        if form.is_valid():
            num1 = form.cleaned_data['num1']
            num2 = form.cleaned_data['num2']
            operator = form.cleaned_data['operator']

            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 != 0:
                    result = num1 / num2
                else:
                    result = 'Division by zero is not allowed.'
            else:
                result = 'Invalid operator'
    else:
        form = CalculatorForm()
        result = None

    return render(request, 'calculator.html', {'form': form, 'result': result})


def calculator_get(request):
    num1 = request.GET.get('num1', '')
    num2 = request.GET.get('num2', '')
    operator = request.GET.get('operator', '')
    result = None

    if num1 and num2 and operator:
        try:
            num1 = float(num1)
            num2 = float(num2)
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 != 0:
                    result = num1 / num2
                else:
                    result = 'Division by zero is not allowed.'
            else:
                result = 'Invalid operator'
        except ValueError:
            result = 'Invalid input'

    return render(request, 'calculator_get.html', {'num1': num1, 'num2': num2, 'operator': operator, 'result': result})

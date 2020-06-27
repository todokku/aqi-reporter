from django.shortcuts import render

def home(request):
    import json
    import requests 

    if request.method == "POST":
        zipcode = request.POST['zipcode']
        # get the content from the api
        api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=5&API_KEY=39E0FAAE-8F3D-45D7-8F99-9C8ADBF9E785")

        try:
            # call json and load up the content from api_request
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."

        # api.0.Category.Name is the django version of api[0]['Category']['Name'], but this is python file
        if api[0]['Category']['Name'] == "Good":
            category_description = "(0-50) Air quality is satisfactory, and air pollution poses little or no risk."
            category_color = "good"
        elif api[0]['Category']['Name'] == "Moderate": 
            category_description = "(51-100) Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution."
            category_color = "moderate"
        elif api[0]['Category']['Name'] == "unhealthyforsensitivegroups":
            category_description = "(101-150) Members of sensitive groups may experience health effects. The general public is less likely to be affected."
            category_color = "Unhealthy for Sensitive Groups"
        elif api[0]['Category']['Name'] == "Unhealthy":
            category_description = "(151-200) Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects."
            category_color = "Unhealthy"
        elif api[0]['Category']['Name'] == "veryunhealthy":
            category_description = "(201-300) Health alert: The risk of health effects is increased for everyone."
            category_color = "Very Unhealthy"
        elif api[0]['Category']['Name'] == "hazardous":
            category_description = "(301 and higher) Health warning of emergency conditions: everyone is more likely to be affected."
            category_color = "Hazardous"


        return render(request, 'home.html', {
            'api': api, 
            'category_description': category_description, 
            'category_color': category_color
            })

        

    else:
        # get the content from the api
        api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=60638&distance=5&API_KEY=39E0FAAE-8F3D-45D7-8F99-9C8ADBF9E785")

        try:
            # call json and load up the content from api_request
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."

        # api.0.Category.Name is the django version of api[0]['Category']['Name'], but this is python file
        if api[0]['Category']['Name'] == "Good":
            category_description = "(0-50) Air quality is satisfactory, and air pollution poses little or no risk."
            category_color = "good"
        elif api[0]['Category']['Name'] == "Moderate": 
            category_description = "(51-100) Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution."
            category_color = "moderate"
        elif api[0]['Category']['Name'] == "unhealthyforsensitivegroups":
            category_description = "(101-150) Members of sensitive groups may experience health effects. The general public is less likely to be affected."
            category_color = "Unhealthy for Sensitive Groups"
        elif api[0]['Category']['Name'] == "Unhealthy":
            category_description = "(151-200) Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects."
            category_color = "Unhealthy"
        elif api[0]['Category']['Name'] == "veryunhealthy":
            category_description = "(201-300) Health alert: The risk of health effects is increased for everyone."
            category_color = "Very Unhealthy"
        elif api[0]['Category']['Name'] == "hazardous":
            category_description = "(301 and higher) Health warning of emergency conditions: everyone is more likely to be affected."
            category_color = "Hazardous"


        return render(request, 'home.html', {
            'api': api, 
            'category_description': category_description, 
            'category_color': category_color
            })

def about(request):
    return render(request, 'about.html', {})

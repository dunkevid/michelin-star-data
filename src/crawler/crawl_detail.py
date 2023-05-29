from src.constants import HTML_CLASS_NAME

def get_detail_address(html):
  element = html.find('li', class_=HTML_CLASS_NAME['d_r_detail_address'])
  address = element.text

  return address

def get_detail_phone_number(html):
  phone_number = ''
  element = html.find_all('a', class_=HTML_CLASS_NAME['d_r_detail_information'])
  if (len(element) > 0 and element[0].get('target') is None):
    phone_number = element[0].get('href') \
      .replace('tel:', '') \
      .replace('-', '') \
      .replace('+', '') \
      .replace(' ', '') \

  return phone_number

def get_detail_website(html):
  website = ''
  element = html.find_all('a', class_=HTML_CLASS_NAME['d_r_detail_information'])
  if (len(element) > 0):
    if (len(element) == 1 and element[0].get('target') is not None):
      return element[0].get('href')
    elif(len(element) == 2 and element[1].get('target') is not None):
      return element[1].get('href')
    else:
      return ''

  return website

def get_detail_opening_hours(html):
  opening_hours = []
  elements = html.find_all('div', class_=HTML_CLASS_NAME['d_r_detail_opening_hours'])
  
  for element in elements:
    opening_hours_e = element.find_all('div', class_='open__time')
    for i in range(len(opening_hours_e)):
      if (i == 0):
        continue
      
      text = opening_hours_e[i].text \
        .strip() \
        .replace(' ', '') \
        .replace('\n\n\n', ' ')
      opening_hours.append(text)

  return opening_hours

def get_detail_description(html):
  element = html.find('div', class_=HTML_CLASS_NAME['d_r_detail_description'])
  description = element.text
  description = description.replace('\n', '')

  return description

def get_detail_facilities_and_services(html):
  services = []
  element = html.find('ul', class_=HTML_CLASS_NAME['d_r_detail_facilities_and_services'])

  if element:
    for item in element.find_all('li'):
      service = item.text.strip()
      services.append(service)

  return services
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from behave import when
import time
from hamcrest import assert_that, equal_to
import random
import subprocess
#from features_front import Data
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
# from PIL import Image
# from features_front.Slack import Slack_Report_IMG
# from feature_qa.feature_template.Discord.Discord import *

#=================================
'''          TIME              '''
#=================================

@when('wait "{numbers}" seconds')
def step_impl(context, numbers):
    context.field = 'wait'
    time.sleep(int(numbers))


@when('wait:"{seconds}" seconds until the element with id:"{idname}" contains the message:"{message}"')
def step_impl(context, seconds,idname,message):
    wait = WebDriverWait(context.driver, int(seconds))
    wait.until(EC.text_to_be_present_in_element((By.ID, idname), message))


@when('wait "{seconds}" seconds until the element with id "{idname}" is found')
def step_impl(context, seconds,idname):
    context.driver.implicitly_wait(int(seconds))    # seconds
    context.driver.find_element_by_id(idname)


@when('wait "{seconds}" seconds until the item with ID:"{Idname}" is found')
def step_impl(context, seconds,Idname):
    context.driver.implicitly_wait(int(seconds))    # seconds
    context.driver.find_element_by_id(Idname)

@when('wait:"{seconds}" seconds until all elements of the container with class:"{classname}" load')
def step_impl(context, seconds, classname):
    wait = WebDriverWait(context.driver, int(seconds))
    # wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, classname)))
    wait.until(EC.visibility_of_any_elements_located((By.CLASS_NAME, classname)))

    time.sleep(1)


@when('wait:"seconds" seconds until a element with id:"id" is found')
def step_impl(context, seconds, id):
    # delay = int(seconds) # seconds
    try:
        WebDriverWait(context.driver, int(seconds)).until(EC.presence_of_element_located(context.driver.find_element_by_id(id)))
        print ("Page is ready!")
    except TimeoutException:
        print ("Loading took too much time!")


#==================================
'''            CLICK           '''
#==================================

@when('click "{css_selector}"')
def step_impl(context, css_selector):
    try:
        wait = WebDriverWait(context.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector)))
        element.click()
    except:
        pass

@when('click button with id "{id_button}"')
def step_impl(context, id_button):
    wait = WebDriverWait(context.driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.ID, id_button)))
    element.click()

    # context.driver.implicitly_wait(10)    # seconds
    # context.driver.find_element_by_id(id_button).click()
    # # time.sleep(4)

@when('click button with name "{name_button}"')
def step_impl(context, name_button):
    wait = WebDriverWait(context.driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.NAME, name_button)))
    element.click()

    # context.driver.implicitly_wait(10)    # seconds
    # context.driver.find_element_by_name(NameButton).click()
    # # time.sleep(2)


@when('click button with xpath "{xpath}"')
def step_impl(context, xpath):
    wait = WebDriverWait(context.driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
    element.click()


    # context.driver.implicitly_wait(10)    # seconds
    # context.driver.find_element_by_xpath(XPATH).click()
    # # time.sleep(10)


@when('click button with class name "{class_name}"')
def step_impl(context, class_name):
    wait = WebDriverWait(context.driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, class_name)))
    element.click()

    # context.driver.implicitly_wait(10)    # seconds
    # context.driver.find_element_by_class_name(Class).click()
    # # time.sleep(5)


@when('click button with css "{css_selector}"')
def step_impl(context, css_selector):
    wait = WebDriverWait(context.driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector)))
    element.click()

    # context.driver.find_element_by_css_selector(selector).click()
    # time.sleep(5)


@when('click css "{selector}"')
def step_impl(context, selector):
    context.driver.find_element_by_class_name(selector).click()


#Special Action
@when('click on edit')
def step_impl(context):
    context.driver.find_element_by_css_selector('.items-stretch :nth-child(2) .my-card i').click()
    time.sleep(2)
    context.driver.find_element_by_xpath('/html/body/div[3]/div/div[1]').click()
    time.sleep(2)

#==================================
'''            FILL           '''
#==================================


@when('fill in the field by id "{id_name}" with value "{value}"')
def step_impl(context, id_name, value):
    wait = WebDriverWait(context.driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.ID, id_name)))
    element.send_keys(value)



@when('fill in the field by css "{css_selector}" with value "{value}"')
def step_impl(context, css_selector, value):
    context.driver.implicitly_wait(10)  # seconds
    context.driver.find_element_by_css_selector(css_selector).send_keys(value)


@when('fill in the field by xpath "{field_xpath}" with value "{value}"')
def step_impl(context, field_xpath, value):
    context.driver.implicitly_wait(10)  # seconds
    context.driver.find_element_by_xpath(field_xpath).send_keys(value)
   # time.sleep(2)


@when('fill in the field by class_name "{class_name}" with value "{value}"')
def step_impl(context, class_name, value):
    context.driver.implicitly_wait(10)  # seconds
    context.driver.find_element_by_name(class_name).send_keys(value)
   # time.sleep(2)


@when('fill random in the field by id "{id}" with value "{value}"')
def step_impl(context, id, value):
    context.driver.implicitly_wait(10)  # seconds
    context.driver.find_element_by_id(id).send_keys('New' + str(random.randrange(4000)) + value)
   # time.sleep(2)


@when('fill random in the field by css "{css_selector}" with value "{value}"')
def step_impl(context, css_selector, value):
    context.driver.implicitly_wait(10)  # seconds
    context.driver.find_element_by_css_selector(css_selector).send_keys('New' + str(random.randrange(4000)) + value)



#@when('fill random data in the field with id "{Fieldname}"')
#def step_impl(context, Fieldname):
        #context.driver.find_element_by_id(Fieldname).send_keys(Data.Search())


#@when('click drop-down list with id "{id}" and value css "{css_selector}"')
#def step_impl(context, id, css_selector):
    #context.driver.implicitly_wait(5)  # seconds
    #context.driver.find_element_by_id(id).click()
    #context.driver.implicitly_wait(5)  # seconds
    #context.driver.find_element_by_css_selector(css_selector).click()
    #time.sleep(2)



#==================================
'''        CLEAR FILL           '''
#==================================

@when('clear field by css: "{css_selector}"')
def step_impl(context, css_selector):
    wait = WebDriverWait(context.driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector)))
    element.click()
    time.sleep(1)
    size = element.get_attribute('value')
    for i in size:
        element.send_keys(Keys.BACK_SPACE)
    time.sleep(1)




    # wait = WebDriverWait(context.driver, 10)
    # element = wait.until(EC.(By.CSS_SELECTOR, field))
    # element.clear()
    # time.sleep(1)

    # context.driver.implicitly_wait(10)  # seconds
    # element = context.driver.find_element_by_css_selector(field)
    # element.click()
    # time.sleep(1)
    # size = element.get_attribute('value')
    # for i in size:
    #     element.send_keys(Keys.BACK_SPACE)




# webElement

#==================================
'''        SEE MESSAGE           '''
#==================================


@when('the user will see a message "{text}" in the id "{id}"')
def step_impl(context, text, id):
    elem = context.driver.find_element_by_id(id)
    message = context.Valid = elem.get_attribute('innerHTML')
    if len(message) == 0:
        time.sleep(3)
        context.Valid = elem.get_attribute('innerHTML')
        assert_that(context.Valid.strip(), equal_to(text))
    else:
        pass

@when('the user will see a message "{text}" in the css "{css_selector}"')
def step_impl(context, text, css_selector):
    context.driver.implicitly_wait(10)
    elem = context.driver.find_element_by_css_selector(css_selector)
    message = context.Valid = elem.get_attribute('innerHTML')
    time.sleep(3)
    context.Valid = elem.get_attribute('innerHTML')
    assert_that(context.Valid.strip(), equal_to(text))



@when('the user will see a message "{error}" in this css "{css_selector}" and position "{position}"')
def step_impl(context, error, css_selector, position):
    elem = context.driver.find_elements_by_css_selector(css_selector)
    # print(elem[0].text)
    # print(elem[1].text)
    # print(elem[2].text)
    # print(elem[3].text)
    context.Valid = elem[int(position)].text
    assert_that(context.Valid, equal_to(error))


@when('the user will see a message "{text}" in this class "{class_name}"')
def step_impl(context, text, class_name):
    elem = context.driver.find_element_by_class_name(class_name)
    context.Valid = elem.get_attribute('innerHTML')
    assert_that(context.Valid.strip(), equal_to(text))


@when('the user will see a title "{text}" in this tag "{tag}"')
def step_impl(context, text, tag):
    elem = context.driver.find_element_by_tag_name(tag)
    context.Valid = elem.get_attribute('innerHTML')
    if str(context.Valid) == text:
        pass
    else:
        breakpoint()
    assert_that(context.Valid, equal_to(text))



#==================================
'''     ATTRIBUTE BY CLASS      '''
#==================================

@when('the "{name_btn}" button has the class "{class_name}"')
def step_impl(context, name_btn, class_name):
    IOS = context.driver.find_element_by_id(name_btn)
    active = (IOS.get_attribute('class'))
    if active == class_name:
        pass
    else:
        breakpoint()


#==================================
'''      FIELD AUTOCOMPLETE     '''
#==================================

@when('the field "{field_name}" was autocomplete')
def seen(context, field_name):
 field = context.driver.find_element_by_id(field_name)
 Valuefield = field.get_attribute('value')
 if len(Valuefield) == 0:
     breakpoint()
 else:
     pass


#==================================
'''          GOOGLE TABS        '''
#==================================


@when('the user goes to the tab "{tab_name}"')
def step_impl(context, tab_name):
 context.driver.switch_to.window(context.driver.window_handles[int(tab_name)])


@when('open new tab with the url: {open_url}')
def step_impl(context, open_url):
 func = f"window.open({open_url})"
 # print(func)
 # AssertionError
 context.driver.execute_script(func)


@when('refresh url')
def step_impl(context):
 context.driver.refresh()


@when('close chrome')
def step_impl(context):
 context.driver.close()


#==================================
'''      SET WINDOW SIZE         '''
#==================================


@when("window size width:'{width}',height:'{height}'")
def step_impl(context, width, height):
   context.driver.set_window_size(int(width), int(height))



#==================================
""" Save Screenshot by comparison domains"""
#==================================


@when('take a screenshot by image base. save to this folder:"{folder}" with the name "{name}"')
def step_impl(context, folder, name):
   context.driver.save_screenshot('features_front/Visual_Regression/base_image/' + folder + '/' + name + '.png')



@when('take a screenshot by image compare. save to this folder:"{folder}" with the name "{name}"')
def step_impl(context, folder, name):
   context.driver.save_screenshot('features_front/Visual_Regression/base_compare/' + folder + '/' + name + '.png')


#==================================
'''     TO COMPARE IMAGES       '''
#==================================


@when('to get the image 1 by xpath:"{image_1}", to get the image 2 by xpath:"{image_2}", compare image 1 and 2. add the difference image to this xpath:"{image_difference}"')
def step_impl(context, image_1, image_2, image_difference):
    CompareImg = ("compare " + image_1+' ' + image_2 +' '+ image_difference)
    subprocess.call(CompareImg, shell=True)

    channel = 'screenshot'
    h1 = Image.open(image_1).histogram()
    h2 = Image.open(image_2).histogram()
    if h1 == h2:
        pass
    else:
        Slack_Report_IMG(channel,image_difference)




#==================================
'''         CHECK ITEMS       '''
#==================================


@when('check if the item with class:"{class_name}" exists')
def step_impl(context, class_name):
    context.driver.implicitly_wait(10)    # seconds
    element = context.driver.find_element_by_css_selector(class_name)
    if element is not None:
        pass
    else:
        breakpoint(step_impl)


@when('check if the item with class "{class_name}" does not exist')
def step_impl(context, class_name):
    try:
        context.driver.implicitly_wait(5)  # seconds
        context.driver.find_element_by_css_selector(class_name)
        print('testing')
    except:
        breakpoint(step_impl)



#====================================================================
#spacial test
@when('check if when you add a video it appears in programs')
def step_impl(context):
    time.sleep(3)
    context.driver.find_element_by_id('menu').click()
    time.sleep(2)
    context.driver.find_element_by_id('menu_internet').click()
    time.sleep(4)
    context.driver.find_element_by_id('search').send_keys('diomedes diaz')
    time.sleep(2)
    context.driver.find_element_by_id('search_button').click()
    time.sleep(5)


    #add new video to my programs
    # compare = context.driver.find_element_by_css_selector('.items-stretch > div:nth-child(2) button').click()
    # time.sleep(2)
    compare = context.driver.find_element_by_css_selector('.items-stretch div:nth-child(2) .q-card__section img:nth-child(1)').click()
    time.sleep(2)

    url = context.driver.find_element_by_css_selector('.items-stretch > div:nth-child(2) iframe').get_attribute('src')
    time.sleep(3)
    context.driver.find_element_by_id('menu').click()
    time.sleep(3)
    click = context.driver.find_element_by_css_selector('.q-list a:nth-child(3)').click()
    time.sleep(2)
    time.sleep(3)
    videos = context.driver.find_elements_by_css_selector('.items-stretch >div > div > div > div:nth-child(2) > iframe')

    list = []
    for video in videos:
        if url in video.get_attribute('src'):
            list.append(video.get_attribute('src'))
            pass
            break
        else:
            pass

    if url in list:
        pass
    else:
        breakpoint()


@when('click with random css value')
#Add video in my gallery
def step_impl(context):

    Result = ('.items-stretch div:nth-child('+Data.Add_video_in_my_galery()+') .q-card__section img:nth-child(1)')
    # context.driver.find_element_by_class_name(str(Result)).click()

    wait = WebDriverWait(context.driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, Result)))
    element.click()



@when('add video')
def step_impl(context):
    # context.driver.find_element_by_id('internet_search_btn').click()
    time.sleep(4)
    # context.driver.find_element_by_id('search').send_keys('testing')
    time.sleep(2)
    context.driver.find_element_by_id('search_button').click()
    time.sleep(4)
    #add new video to my programs
    compare = context.driver.find_element_by_css_selector('.items-stretch div:nth-child(2) .q-card__section img:nth-child(1)').click()
    time.sleep(2)
#===================================================================

@when('the user will see a message "{text}" in this css "{css_selector}"')
def step_impl(context, text, css):
    elem = context.driver.find_element_by_css_selector(css)
    context.Valid = elem.get_attribute('innerHTML')
    assert_that(context.Valid.strip(), equal_to(text))
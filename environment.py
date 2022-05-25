from behave import when
from selenium import webdriver
#from feature.feature_template.Discord.Discord import *
from Discord import Discord

BEHAVE_DEBUG_ON_ERROR = False

# def after_step(context, step):
#     if step.status == "failed":
#         file_name = step.filename
#         scenario_name = context.scenario_name
#         step_name = step.name
#         Discord.Report_Discord(file_name,scenario_name,step_name)


def after_step(context, step):
    if step.status == "failed":
        file_name = step.filename
        scenario_name = context.scenario_name
        step_name = step.name
        content = str('**Behave Test**\n'+'```File: '+ file_name +'\nScenario: '+scenario_name+'\nStep FAILE: '+step_name+'```')
        Discord.Report_Discord(content)

# def after_scenario(context, scenario):
    # print(scenario.name)


def before_scenario(context, scenario):
    # print(scenario.name)
    context.scenario_name = scenario.name


def after_feature(context, feature):
    name = feature.name
    if feature.status == "passed":
        content = str('**Behave Test**\n'+'```'+'feature:'+name+'\nAll tests were completed successfully'+'```')
        Discord.Report_Discord(content)
        print(feature.status)
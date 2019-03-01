
from behave import *

from actions.Actions import Action


@given('website "{url}"')
def step(context, url):
    userdata = context.config.userdata
    context.browser = userdata.get("browser")
    context.actions = Action(context.browser)
    context.actions.open_page(url)


@then('search book by keyword')
def step(context):
    userdata = context.config.userdata
    context.book_val = userdata.get("word")
    context.actions.search(context.book_val)


@then('get info from page')
def step(context):
    context.items = context.actions.get_info()


@then('check search value is in names')
def step(context):
    context.actions.is_word_in_arr(context.items, context.book_val)


@then("exit")
def step(context):
    context.actions.exit()

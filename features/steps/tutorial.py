#!/usr/bin/env python
# -*- coding: utf-8 -*-
from behave import *
from actions.Actions import Action


@given('website "{url}"')
def step(context, url):
    context.actions = Action()
    context.actions.open_page(url)


@then('search book "{book_name}"')
def step(context, book_name):
    context.book_val = ''
    if context.book_val == '':
        context.book_val = book_name
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

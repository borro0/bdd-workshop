# This is your steps file, implement all steps in here

from behave import given, when, then, use_step_matcher
from course import Course
from datetime import datetime

use_step_matcher("cfparse")

# GIVEN STEPS

@given(u'there is a course with {count:d} registrations')
def course_with_registrations(context, count):
    context.course = Course()
    context.course.registrations = count
    context.current_date = datetime.now

@given(u'I enter {name}')
def step_impl(context, name):
    context.name = name


@when(u'I register')
def step_impl(context):
    context.course.register(context.name)


@then(u'the course has {count:d} registration')
def step_impl(context, count):
    assert context.course.registrations == count

# WHEN STEPS

# THEN STEPS

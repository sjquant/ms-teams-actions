import json
import os

import pymsteams


WEBHOOK_URI = os.getenv("INPUT_WEBHOOK_URI")
TITLE = os.getenv("INPUT_TITLE")
COLOR = os.getenv("INPUT_COLOR")
SUMMARY = os.getenv("INPUT_SUMMARY")
TEXT = os.getenv("INPUT_TEXT")
LINK_BUTTONS = os.getenv("INPUT_LINK_BUTTONS")
SECTIONS = os.getenv("INPUT_SECTIONS")
ACTIONS = os.getenv("INPUT_ACTIONS")


def addActions(message, actions):
    actions = json.loads(actions)
    for each in actions:
        actions = message.payload.setdefault("potentialAction", [])
        actions.append(each)


def addSections(message, sections):
    sections = json.loads(sections)
    for each in sections:
        sections = message.payload.setdefault("sections", [])
        sections.append(each)


def addButtons(message, buttons):
    buttons = json.loads(buttons)
    for each in buttons:
        message.addLinkButton(each[0], each[1])


def main():
    message = pymsteams.connectorcard(WEBHOOK_URI)
    if TITLE:
        message.title(TITLE)
    if COLOR:
        message.color(COLOR)
    if SUMMARY:
        message.summary(SUMMARY)
    if TEXT:
        message.text(TEXT)
    if SECTIONS:
        addSections(message, SECTIONS)
    if ACTIONS:
        addActions(message, ACTIONS)
    if LINK_BUTTONS:
        addButtons(message, LINK_BUTTONS)
    message.send()


if __name__ == "__main__":
    main()
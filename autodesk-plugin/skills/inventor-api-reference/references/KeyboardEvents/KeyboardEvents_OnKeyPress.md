# KeyboardEvents.OnKeyPress Event

Parent Object: [KeyboardEvents](../KeyboardEvents/KeyboardEvents.md)

## Description

Event that occurs when the user presses and releases an ANSI key on the keyboard. The ANSI value of the key pressed is returned.

## Syntax

KeyboardEvents.**OnKeyPress**( ***KeyASCII*** As Long )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| KeyASCII | Long | Returns a Long that is a standard numeric ANSI keycode. KeyASCII is passed by value. Changing KeyASCII to 0 cancels the keystroke so the object receives no character. |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
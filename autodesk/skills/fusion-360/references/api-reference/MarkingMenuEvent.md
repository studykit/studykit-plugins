# MarkingMenuEvent Object

Derived from: [Event](Event.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/UserInterface/MarkingMenuEvent.h>

## Description

A MarkingMenuEvent is fired when the marking menu and context menu are displayed. For example, in response to the markingMenuDisplaying event.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](MarkingMenuEvent_add.htm) | Add a handler to be notified when the event occurs. |
| [classType](MarkingMenuEvent_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [remove](MarkingMenuEvent_remove.htm) | Removes a handler from the event. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isValid](MarkingMenuEvent_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [name](MarkingMenuEvent_name.htm) | The name of the event - e.g. "DocumentOpening" |
| [objectType](MarkingMenuEvent_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [sender](MarkingMenuEvent_sender.htm) | The object that is firing the event. For example, in the case of a command input event this will return the command. |

## Accessed From

[UserInterface.markingMenuDisplaying](UserInterface_markingMenuDisplaying.htm)

## Version

Introduced in version January 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
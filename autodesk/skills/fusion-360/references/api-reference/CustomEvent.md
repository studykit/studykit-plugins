# CustomEvent Object

Derived from: [Event](Event.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Application/CustomEvent.h>

## Description

A CustomEvent is primarily used to send an event from a worker thread you've created back to your add-in, which is running in the primary thread. It's also possible for add-ins to cooperate and another add-in can trigger this event in your add-in by knowing the custom event id.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](CustomEvent_add.htm) | Add a handler to be notified when the event occurs. |
| [classType](CustomEvent_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [remove](CustomEvent_remove.htm) | Removes a handler from the event. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [eventId](CustomEvent_eventId.htm) | Returns the id that was assigned to this event when it was registered. Each custom event has it's own unique id. |
| [isValid](CustomEvent_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [name](CustomEvent_name.htm) | The name of the event - e.g. "DocumentOpening" |
| [objectType](CustomEvent_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [sender](CustomEvent_sender.htm) | The object that is firing the event. For example, in the case of a command input event this will return the command. |

## Accessed From

[Application.registerCustomEvent](Application_registerCustomEvent.htm)

## Version

Introduced in version January 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
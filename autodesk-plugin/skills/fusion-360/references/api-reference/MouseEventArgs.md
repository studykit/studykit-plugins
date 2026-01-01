# MouseEventArgs Object

Derived from: [EventArgs](EventArgs.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/UserInterface/MouseEventArgs.h>

## Description

Provides a set of arguments from a firing MouseEvent to a MouseEventHandler's notify callback method.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](MouseEventArgs_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [button](MouseEventArgs_button.htm) | Gets which mouse button(s) are pressed. The returned value is bitwise and can indicate that more than one button is pressed. |
| [clicks](MouseEventArgs_clicks.htm) | Gets the number of times the button was pressed and released. |
| [firingEvent](MouseEventArgs_firingEvent.htm) | The event that the firing is in response to. |
| [isValid](MouseEventArgs_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [keyboardModifiers](MouseEventArgs_keyboardModifiers.htm) | Gets which modifier keys are currently pressed. The returned value is bitwise and can indicate that more than one button is pressed. |
| [objectType](MouseEventArgs_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [position](MouseEventArgs_position.htm) | Gets the coordinate of the mouse in screen space. |
| [viewport](MouseEventArgs_viewport.htm) | Returns the viewport where the mouse event occurred, if it was within a viewport. If the mouse is not over a viewport this property will return null. |
| [viewportPosition](MouseEventArgs_viewportPosition.htm) | Gets the coordinate of the mouse in viewport space, if the mouse is within a viewport. If the mouse is not over a viewport this property will return null. |
| [wheelDelta](MouseEventArgs_wheelDelta.htm) | Gets a signed count of the number of detents the mouse wheel has rotated. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# HTMLEventArgs Object

Derived from: [EventArgs](EventArgs.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/UserInterface/HTMLEventArgs.h>

## Description

The HTMLEventArgs provides access to the information sent from the JavaScript that's associated with HTML being displayed within a palette.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](HTMLEventArgs_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [action](HTMLEventArgs_action.htm) | The action string sent from the JavaScript associated with HTML displayed in the palette. The string can represent any type of data in any format but JSON is commonly used to pass more complex data. |
| [browserCommandInput](HTMLEventArgs_browserCommandInput.htm) | When the event is fired from a BrowserCommandInput object, this property returns the specific BrowserCommandInput that caused the event to fire. In all other cases this property returns null. |
| [data](HTMLEventArgs_data.htm) | The data string sent from the JavaScript associated with HTML displayed in the palette. The string can represent any type of data in any format but JSON is commonly used to pass more complex data. |
| [firingEvent](HTMLEventArgs_firingEvent.htm) | The event that the firing is in response to. |
| [isValid](HTMLEventArgs_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](HTMLEventArgs_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [returnData](HTMLEventArgs_returnData.htm) | Set this property to return data back to the JavaScript that's associated with the HTML. |

## Version

Introduced in version March 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
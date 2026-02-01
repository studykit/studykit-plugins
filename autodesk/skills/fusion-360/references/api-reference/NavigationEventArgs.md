# NavigationEventArgs Object

Derived from: [EventArgs](EventArgs.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/UserInterface/NavigationEventArgs.h>

## Description

The NavigationEventArgs provides access to the information sent from the browser within a palette on a navigation event.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](NavigationEventArgs_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [browserCommandInput](NavigationEventArgs_browserCommandInput.htm) | When the event is fired from a BrowserCommandInput object, this property returns the specific BrowserCommandInput that caused the event to fire. In all other cases this property returns null. |
| [firingEvent](NavigationEventArgs_firingEvent.htm) | The event that the firing is in response to. |
| [isValid](NavigationEventArgs_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [launchExternally](NavigationEventArgs_launchExternally.htm) | If True, the URL will be navigated to in an external browser by the operating system. If False, the default value, the URL will be navigated to in the palette's browser. |
| [navigationURL](NavigationEventArgs_navigationURL.htm) | The URL that is being navigated to. |
| [objectType](NavigationEventArgs_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [preventDefault](NavigationEventArgs_preventDefault.htm) | If True, the default handling of this navigation event will not continue. If False, the default value, the default handling of this navigation event will continue. |

## Version

Introduced in version March 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
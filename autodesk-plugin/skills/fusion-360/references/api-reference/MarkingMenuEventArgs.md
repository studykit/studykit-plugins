# MarkingMenuEventArgs Object

Derived from: [EventArgs](EventArgs.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/UserInterface/MarkingMenuEventArgs.h>

## Description

The MarkingMenuEventArgs provides information associated with the marking and context menu being displayed.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](MarkingMenuEventArgs_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [firingEvent](MarkingMenuEventArgs_firingEvent.htm) | The event that the firing is in response to. |
| [isValid](MarkingMenuEventArgs_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [linearMarkingMenu](MarkingMenuEventArgs_linearMarkingMenu.htm) | Provides access to the linear marking menu. |
| [objectType](MarkingMenuEventArgs_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [radialMarkingMenu](MarkingMenuEventArgs_radialMarkingMenu.htm) | Provides access to the radial marking menu. |
| [selectedEntities](MarkingMenuEventArgs_selectedEntities.htm) | Returns the currently selected entities that the user left-clicked over. These provide the "context" of what should be displayed in the menu. This can be an empty array in the case where they clicked in a open area within the graphics window. |

## Version

Introduced in version January 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
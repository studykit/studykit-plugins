# SelectionEventArgs Object

Derived from: [EventArgs](EventArgs.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/UserInterface/SelectionEventArgs.h>

## Description

Provides a set of arguments from a firing SelectionEvent to a SelectionEventHandler's notify callback method.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](SelectionEventArgs_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [activeInput](SelectionEventArgs_activeInput.htm) | Returns the SelectionCommandInput that is currently active in the command dialog and that the user is selecting entities for. This can be used to determine which set of rules you want to apply to determine if the current entity is selectable or not. |
| [additionalEntities](SelectionEventArgs_additionalEntities.htm) | Gets or sets any additional entities that should be pre-highlighted and selected if the entity the mouse is over is selected. If you add an entity that is already selected, it will be unselected. The result of adding additional entities is the same as if they were selected one at a time by the user and the user can unselect each entity one at a time by picking it while it's selected. |
| [firingEvent](SelectionEventArgs_firingEvent.htm) | The event that the firing is in response to. |
| [isSelectable](SelectionEventArgs_isSelectable.htm) | Gets or sets whether this entity should be made available to be selected. The value is initialized to true, so doing nothing will result in the entity being selectable. |
| [isValid](SelectionEventArgs_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](SelectionEventArgs_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |
| [selection](SelectionEventArgs_selection.htm) | Gets the entity that is valid for selection. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# Toolbar Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/UserInterface/Toolbar.h>

## Description

Provides access to a toolbar in the user interface. A toolbar is a collection of toolbar controls.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](Toolbar_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [controls](Toolbar_controls.htm) | Gets the controls in this toolbar. |
| [id](Toolbar_id.htm) | Gets the unique ID of the toolbar that can be used programmatically to find a specific toolbar. |
| [isValid](Toolbar_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](Toolbar_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [parentUserInterface](Toolbar_parentUserInterface.htm) | Gets the owning UserInterface object. |

## Accessed From

[Toolbars.item](Toolbars_item.htm), [Toolbars.itemById](Toolbars_itemById.htm), [UserInterface.activeToolbar](UserInterface_activeToolbar.htm)

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
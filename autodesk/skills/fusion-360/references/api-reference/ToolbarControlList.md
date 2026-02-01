# ToolbarControlList Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ToolbarControlList.h>

## Description

Provides access to a list of toolbar controls.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](ToolbarControlList_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](ToolbarControlList_item.htm) | Returns the ToolbarControl at the specified index. When iterating by index, the controls are returned in the same order as they are shown in the user interface. |
| [itemById](ToolbarControlList_itemById.htm) | Returns the ToolbarControl at the specified ID. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](ToolbarControlList_count.htm) | Gets the number of toolbar controls. |
| [isValid](ToolbarControlList_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](ToolbarControlList_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[ToolbarPanel.promotedControls](ToolbarPanel_promotedControls.htm)

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
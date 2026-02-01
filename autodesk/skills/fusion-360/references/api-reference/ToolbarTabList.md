# ToolbarTabList Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ToolbarTabList.h>

## Description

A ToolbarTabList is a list of ToolbarTab objects.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](ToolbarTabList_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](ToolbarTabList_item.htm) | Returns the specified tab using an index into the collection. |
| [itemById](ToolbarTabList_itemById.htm) | Returns the ToolbarTab of the specified ID. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](ToolbarTabList_count.htm) | Gets the number of toolbar tabs in the collection. |
| [isValid](ToolbarTabList_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](ToolbarTabList_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[UserInterface.allToolbarTabs](UserInterface_allToolbarTabs.htm), [UserInterface.toolbarTabsByProductType](UserInterface_toolbarTabsByProductType.htm)

## Version

Introduced in version August 2019

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
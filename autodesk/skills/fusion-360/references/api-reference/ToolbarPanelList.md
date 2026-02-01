# ToolbarPanelList Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ToolbarPanelList.h>

## Description

A ToolbarPanelList is a list of ToolbarPanel objects.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](ToolbarPanelList_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](ToolbarPanelList_item.htm) | Returns the specified work space using an index into the collection. |
| [itemById](ToolbarPanelList_itemById.htm) | Returns the ToolbarPanel of the specified ID. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](ToolbarPanelList_count.htm) | Gets the number of toolbar panels in the collection. |
| [isValid](ToolbarPanelList_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](ToolbarPanelList_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[UserInterface.allToolbarPanels](UserInterface_allToolbarPanels.htm), [UserInterface.toolbarPanelsByProductType](UserInterface_toolbarPanelsByProductType.htm)

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
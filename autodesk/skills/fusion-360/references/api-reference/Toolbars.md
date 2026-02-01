# Toolbars Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/UserInterface/Toolbars.h>

## Description

Provides access to the toolbars. These are currently the right and left QAT's and the NavBar.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](Toolbars_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](Toolbars_item.htm) | Returns the specified toolbar using an index into the collection. |
| [itemById](Toolbars_itemById.htm) | Returns the Toolbar of the specified ID. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](Toolbars_count.htm) | Gets the number of Toolbar objects in the collection. |
| [isValid](Toolbars_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](Toolbars_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[UserInterface.toolbars](UserInterface_toolbars.htm)

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
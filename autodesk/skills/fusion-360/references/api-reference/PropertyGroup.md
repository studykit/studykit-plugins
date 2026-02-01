# PropertyGroup Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Application/PropertyGroup.h>

## Description

Represents a group of properties and provides access to the properties.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](PropertyGroup_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](PropertyGroup_item.htm) | Returns the specified property from the group using an index into the group. |
| [itemById](PropertyGroup_itemById.htm) | Returns the specified property from the group using the unique ID of the property. The ID is consistent and can't be modified by the user and isn't affected by localization. |
| [itemByName](PropertyGroup_itemByName.htm) | Returns the specified Property using the name of the property. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](PropertyGroup_count.htm) | Returns the number of properties within the group. |
| [id](PropertyGroup_id.htm) | Returns the unique ID of this property. |
| [isValid](PropertyGroup_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [name](PropertyGroup_name.htm) | Returns the name of this group as seen in the user interface. This name is localized and can change based on the current language |
| [objectType](PropertyGroup_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [parent](PropertyGroup_parent.htm) | Returns the parent of this group. Typically this will be a Component. |

## Accessed From

[PropertyGroups.item](PropertyGroups_item.htm), [PropertyGroups.itemById](PropertyGroups_itemById.htm), [PropertyGroups.itemByName](PropertyGroups_itemByName.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Library Item API Sample](LibraryItemSample_Sample.htm) | Demonstrates how to examine library items using the API.  To use the sample, create a new Python or C++ script and copy and paste this code, replacing the existing default code. The script will search for and record all components and library items in the current project. They are displayed in a dialog when the script has finished. |

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
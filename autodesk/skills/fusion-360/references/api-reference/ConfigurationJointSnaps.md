# ConfigurationJointSnaps Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationJointSnaps.h>

## Description

Collection object that provides access to all the joint snaps that have been defined for a ConfigurationJointSnapColumn. You can also use this collection to define new joint snaps that will then be available when specifying which snap to use in a cell.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](ConfigurationJointSnaps_add.htm) | Adds a new snap to the column. The snaps associated with the column can be used in the cells in the column. |
| [classType](ConfigurationJointSnaps_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](ConfigurationJointSnaps_item.htm) | A method that returns the specified snap using an index into the collection. |
| [itemByName](ConfigurationJointSnaps_itemByName.htm) | A method that returns the snap with the specified name. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](ConfigurationJointSnaps_count.htm) | Returns the number of snaps for the column. |
| [isValid](ConfigurationJointSnaps_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](ConfigurationJointSnaps_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[ConfigurationJointSnapColumn.snaps](ConfigurationJointSnapColumn_snaps.htm)

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
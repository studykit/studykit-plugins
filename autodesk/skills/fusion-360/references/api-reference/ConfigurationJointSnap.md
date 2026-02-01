# ConfigurationJointSnap Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationJointSnap.h>

## Description

This object represents an individual joint snap that has been defined for a ConfigurationJointSnapColumn. Multiple joint snaps can be defined for a column and then one of those joint snaps is specified in each cell of the column.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](ConfigurationJointSnap_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [deleteMe](ConfigurationJointSnap_deleteMe.htm) | Deletes this joint snap. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isValid](ConfigurationJointSnap_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [jointGeometry](ConfigurationJointSnap_jointGeometry.htm) | Gets and sets the JointGeometry object for this snap. |
| [name](ConfigurationJointSnap_name.htm) | Gets and sets the name of the snap. |
| [objectType](ConfigurationJointSnap_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[ConfigurationJointSnapCell.snap](ConfigurationJointSnapCell_snap.htm), [ConfigurationJointSnaps.add](ConfigurationJointSnaps_add.htm), [ConfigurationJointSnaps.item](ConfigurationJointSnaps_item.htm), [ConfigurationJointSnaps.itemByName](ConfigurationJointSnaps_itemByName.htm)

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
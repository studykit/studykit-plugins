# Snapshot Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/Snapshot.h>

## Description

Object that represents a Snapshot in the timeline

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](Snapshot_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [deleteMe](Snapshot_deleteMe.htm) | Deletes this snapshot. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isValid](Snapshot_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [name](Snapshot_name.htm) | Gets and sets the name of the snapshot as seen in the timeline. |
| [objectType](Snapshot_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [timelineObject](Snapshot_timelineObject.htm) | Returns the timeline object associated with this snapshot. |

## Accessed From

[Snapshots.add](Snapshots_add.htm), [Snapshots.item](Snapshots_item.htm)

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# Snapshots Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/Snapshots.h>

## Description

Provides access to the Snapshots within a design and provides methods to create new Snapshots.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](Snapshots_add.htm) | Creates a new snapshot. Creating a snapshot is only valid when the HasPendingTransforms property returns true. |
| [classType](Snapshots_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](Snapshots_item.htm) | Function that returns the specified snapshot in the collection using an index into the collection. |
| [revertPendingSnapshot](Snapshots_revertPendingSnapshot.htm) | Reverts and changes that have been made that can be snapshot. This effectively reverts the design back to the last snapshot. This is only valid when the HasPendingSnapshot property returns true. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](Snapshots_count.htm) | The number of items in the collection. |
| [hasPendingSnapshot](Snapshots_hasPendingSnapshot.htm) | Indicates if there are any changes that have been made than can be snapshot. |
| [isValid](Snapshots_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](Snapshots_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[Design.snapshots](Design_snapshots.htm), [FlatPatternProduct.snapshots](FlatPatternProduct_snapshots.htm), [WorkingModel.snapshots](WorkingModel_snapshots.htm)

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
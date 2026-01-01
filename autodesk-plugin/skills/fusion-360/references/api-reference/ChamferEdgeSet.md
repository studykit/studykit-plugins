# ChamferEdgeSet Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ChamferEdgeSet.h>

## Description

The base class for the classes that define the different types of chamfer edge sets.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](ChamferEdgeSet_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [deleteMe](ChamferEdgeSet_deleteMe.htm) | Deletes the chamfer edge set from the chamfer. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isTangentChain](ChamferEdgeSet_isTangentChain.htm) | Gets and sets the Tangent chain for chamfer. This enables tangent chain option for chamfer. |
| [isValid](ChamferEdgeSet_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](ChamferEdgeSet_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |

## Accessed From

[ChamferEdgeSets.item](ChamferEdgeSets_item.htm)

## Derived Classes

[DistanceAndAngleChamferEdgeSet](DistanceAndAngleChamferEdgeSet.htm), [EqualDistanceChamferEdgeSet](EqualDistanceChamferEdgeSet.htm), [TwoDistancesChamferEdgeSet](TwoDistancesChamferEdgeSet.htm)

## Version

Introduced in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
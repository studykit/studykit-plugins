# FilletEdgeSet Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/FilletEdgeSet.h>

## Description

The base class for the classes that define the different types of fillet edge sets.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](FilletEdgeSet_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [deleteMe](FilletEdgeSet_deleteMe.htm) | Deletes the fillet edge set from the fillet. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [continuity](FilletEdgeSet_continuity.htm) | Gets and sets the continuity of the fillet edge set. Valid values are TangentSurfaceContinuityType and CurvatureSurfaceContinuityType. |
| [isTangentChain](FilletEdgeSet_isTangentChain.htm) | Gets and sets the Tangent chain for fillet. This enables tangent chain option for fillet. |
| [isValid](FilletEdgeSet_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](FilletEdgeSet_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |
| [tangencyWeight](FilletEdgeSet_tangencyWeight.htm) | Returns the model parameter that controls the G1 or G2 tangency weight of the fillet. It must be a real value between 0.1 and 2.0 inclusive. You can edit the tangency weight by using the properties on the returned ModelParameter object. |

## Accessed From

[FilletEdgeSets.item](FilletEdgeSets_item.htm)

## Derived Classes

[ChordLengthFilletEdgeSet](ChordLengthFilletEdgeSet.htm), [ConstantRadiusFilletEdgeSet](ConstantRadiusFilletEdgeSet.htm), [VariableRadiusFilletEdgeSet](VariableRadiusFilletEdgeSet.htm)

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# FilletEdgeSetInput Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/FilletEdgeSetInput.h>

## Description

Represents the input to define a fillet edge set.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](FilletEdgeSetInput_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [continuity](FilletEdgeSetInput_continuity.htm) | Gets and sets the continuity of the fillet edge set. Valid values are TangentSurfaceContinuityType and CurvatureSurfaceContinuityType. The default is TangentSurfaceContinuityType. |
| [entities](FilletEdgeSetInput_entities.htm) | Gets and sets the entities associated with this fillet edge set. For constant radius and chord length edge sets, this can be edges, faces, and features. For variable radius edges sets, this must be edges. |
| [isValid](FilletEdgeSetInput_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](FilletEdgeSetInput_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [tangencyWeight](FilletEdgeSetInput_tangencyWeight.htm) | Gets and sets the tangency weight for the given edge set. The tangency weight controls the influence of the continuity (G1 or G2) on the fillet. The ValueInput must be a real value between 0.1 and 2.0 inclusive, with no units. The default value is 1.0. |

## Accessed From

[FilletEdgeSetInputs.item](FilletEdgeSetInputs_item.htm)

## Derived Classes

[ChordLengthFilletEdgeSetInput](ChordLengthFilletEdgeSetInput.htm), [ConstantRadiusFilletEdgeSetInput](ConstantRadiusFilletEdgeSetInput.htm), [VariableRadiusFilletEdgeSetInput](VariableRadiusFilletEdgeSetInput.htm)

## Version

Introduced in version November 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
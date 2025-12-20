# FilletConstantRadiusEdgeSet Object

Derived from: [FilletRadiusEdgeSet](../FilletRadiusEdgeSet/FilletRadiusEdgeSet.md) Object

## Description

The ConstantRadiusEdgeSet object provides access the edges and their associated radii for a constant radius fillet.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AllFillets](../FilletConstantRadiusEdgeSet/FilletConstantRadiusEdgeSet_AllFillets.md) | Property that returns if the edge set defines all concave edges. |
| [AllRounds](../FilletConstantRadiusEdgeSet/FilletConstantRadiusEdgeSet_AllRounds.md) | Property that returns if the edge set defines all convex edges. |
| [Application](../FilletConstantRadiusEdgeSet/FilletConstantRadiusEdgeSet_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [ContinuityType](../FilletConstantRadiusEdgeSet/FilletConstantRadiusEdgeSet_ContinuityType.md) | Read-write property that gets and sets the continuity type for the edge set. Valid values are kTangentContinuity and kCurvatureContinuity. This property can currently only be set in the forward create scenario (it fails if the FilletDefinition is obtained from an existing feature). |
| [Edges](../FilletConstantRadiusEdgeSet/FilletConstantRadiusEdgeSet_Edges.md) | Property that provides access to the in the edge set. This property is only available when a FilletDefinition object is being defined to use as input for creating a fillet. When the parent FilletDefinition object is obtained from an existing Fillet, the end-of-part marker should be placed above this fillet feature to allow access this property. |
| [InvertedFillet](../FilletConstantRadiusEdgeSet/FilletConstantRadiusEdgeSet_InvertedFillet.md) | Gets and sets whether or not to use inverted fillet for the edge set. |
| [Radius](../FilletConstantRadiusEdgeSet/FilletConstantRadiusEdgeSet_Radius.md) | Property that returns the parameter that controls the radius of the fillet. This property will return Nothing if the fillet feature has not been created yet. |
| [Type](../FilletConstantRadiusEdgeSet/FilletConstantRadiusEdgeSet_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[FilletDefinition.AddConstantRadiusEdgeSet](../FilletDefinition/FilletDefinition_AddConstantRadiusEdgeSet.md)

## Version

Introduced in version 5.3

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
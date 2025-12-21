# FilletVariableRadiusEdgeSet Object

Derived from: [FilletRadiusEdgeSet](../FilletRadiusEdgeSet/FilletRadiusEdgeSet.md) Object

## Description

The FilletVariableRadiusEdgeSet object provides methods to specify the radius for variable radius fillet features.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddIntermediateRadius](../FilletVariableRadiusEdgeSet/FilletVariableRadiusEdgeSet_AddIntermediateRadius.md) | Method that creates a new FilletIntermediateRadius. The new FilletIntermediateRadius is returned. This method is used to define radii at intermediate points along an edge. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../FilletVariableRadiusEdgeSet/FilletVariableRadiusEdgeSet_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [ContinuityType](../FilletVariableRadiusEdgeSet/FilletVariableRadiusEdgeSet_ContinuityType.md) | Read-write property that gets and sets the continuity type for the edge set. Valid values are kTangentContinuity and kCurvatureContinuity. This property can currently only be set in the forward create scenario (it fails if the FilletDefinition is obtained from an existing feature). |
| [Edges](../FilletVariableRadiusEdgeSet/FilletVariableRadiusEdgeSet_Edges.md) | Property that provides access to the in the edge set. This property is only available when a FilletDefinition object is being defined to use as input for creating a fillet. When the parent FilletDefinition object is obtained from an existing Fillet, the end-of-part marker should be placed above this fillet feature to allow access this property. |
| [EndRadius](../FilletVariableRadiusEdgeSet/FilletVariableRadiusEdgeSet_EndRadius.md) | Property that returns the parameter that controls the end radius of the fillet. |
| [IntermediateRadiusCount](../FilletVariableRadiusEdgeSet/FilletVariableRadiusEdgeSet_IntermediateRadiusCount.md) | Property that returns the number of intermediate points defined in the edge set. |
| [IntermediateRadiusItem](../FilletVariableRadiusEdgeSet/FilletVariableRadiusEdgeSet_IntermediateRadiusItem.md) | Returns the specified FilletIntermediateRadius object. |
| [StartRadius](../FilletVariableRadiusEdgeSet/FilletVariableRadiusEdgeSet_StartRadius.md) | Property that returns the parameter that controls the start radius of the fillet. |
| [Type](../FilletVariableRadiusEdgeSet/FilletVariableRadiusEdgeSet_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[FilletDefinition.AddVariableRadiusEdgeSet](../FilletDefinition/FilletDefinition_AddVariableRadiusEdgeSet.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Fillet Feature (Complex)](../../sample-programs/FilletFeature2_Sample.md) | This sample demonstrates creating a complex fillet. The result in this case has several different constant radii fillets and two edges that use variable radius, with one of these having a different radius defined along the edge. |

## Version

Introduced in version 5.3

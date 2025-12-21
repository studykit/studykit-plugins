# FilletRadiusEdgeSet Object

## Description

The FilletRadiusEdgeSet object is the base class for FilletConstantRadiusEdgeSet and FilletVariableRadiusEdgeSet objects.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../FilletRadiusEdgeSet/FilletRadiusEdgeSet_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Edges](../FilletRadiusEdgeSet/FilletRadiusEdgeSet_Edges.md) | Property that provides access to the in the edge set. This property is only available when a FilletDefinition object is being defined to use as input for creating a fillet. When the parent FilletDefinition object is obtained from an existing Fillet, the end-of-part marker should be placed above this fillet feature to allow access this property. |
| [Type](../FilletRadiusEdgeSet/FilletRadiusEdgeSet_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[FilletDefinition.EdgeSetItem](../FilletDefinition/FilletDefinition_EdgeSetItem.md)

## Derived Classes

[FilletConstantRadiusEdgeSet](../FilletConstantRadiusEdgeSet/FilletConstantRadiusEdgeSet.md), [FilletVariableRadiusEdgeSet](../FilletVariableRadiusEdgeSet/FilletVariableRadiusEdgeSet.md)

## Version

Introduced in version 5.3

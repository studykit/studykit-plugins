# WorkAxes Object

## Description

The WorkAxes collection object provides access to all of the  objects in the parent document and provides methods to create new work axes.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddByAnalyticEdge](../WorkAxes/WorkAxes_AddByAnalyticEdge.md) | Method that creates a new work axis based on the input analytic edge. This method is not currently supported when creating a work axis within an assembly. |
| [AddByLine](../WorkAxes/WorkAxes_AddByLine.md) | Method that creates a new work axis based on the input line. This method is not currently supported when creating a work axis within an assembly. |
| [AddByLineAndPlane](../WorkAxes/WorkAxes_AddByLineAndPlane.md) | Method that creates a new work axis that is along a line defined by projecting the input line onto the input plane along the plane normal. This method is not currently supported when creating a work axis within an assembly. |
| [AddByLineAndPoint](../WorkAxes/WorkAxes_AddByLineAndPoint.md) | Method that creates a new work axis that is parallel to a line and passes through the input point. This method is not currently supported when creating a work axis within an assembly. |
| [AddByNormalToSurface](../WorkAxes/WorkAxes_AddByNormalToSurface.md) | Method that creates a new work axis that passes through the point and is normal to the input surface. This method is not currently supported when creating a work axis within an assembly. |
| [AddByRevolvedFace](../WorkAxes/WorkAxes_AddByRevolvedFace.md) | Method that creates a new work axis through the axis of a revolved face. This method is not currently supported when creating a work axis within an assembly. |
| [AddByTwoPlanes](../WorkAxes/WorkAxes_AddByTwoPlanes.md) | Method that creates a new work axis at the intersection of the two input planes. This method is not currently supported when creating a work axis within an assembly. |
| [AddByTwoPoints](../WorkAxes/WorkAxes_AddByTwoPoints.md) | Method that creates a new work axis through the two input points. This method is not currently supported when creating a work axis within an assembly. |
| [AddFixed](../WorkAxes/WorkAxes_AddFixed.md) | Method that creates a new work axis that passes through the input point in the direction of the input vector. When used to create a work axis within an assembly the resulting work axis will return an AssemblyWorkAxisDef definition. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../WorkAxes/WorkAxes_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../WorkAxes/WorkAxes_Count.md) | Property that returns the number of items in this collection. |
| [Item](../WorkAxes/WorkAxes_Item.md) | Returns the specified WorkAxis object from the collection. This is the default property of the WorkAxes collection object. |
| [Parent](../WorkAxes/WorkAxes_Parent.md) | Property returning the parent  object. |
| [Type](../WorkAxes/WorkAxes_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[AssemblyComponentDefinition.WorkAxes](../AssemblyComponentDefinition/AssemblyComponentDefinition_WorkAxes.md), [FlatPattern.WorkAxes](../FlatPattern/FlatPattern_WorkAxes.md), [PartComponentDefinition.WorkAxes](../PartComponentDefinition/PartComponentDefinition_WorkAxes.md), [SheetMetalComponentDefinition.WorkAxes](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_WorkAxes.md), [WeldmentComponentDefinition.WorkAxes](../WeldmentComponentDefinition/WeldmentComponentDefinition_WorkAxes.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create sheet metal face and cut features](../../sample-programs/SheetMetalFeatures_Sample.md) | This sample demonstrates the creation of sheet metal face and cut features. |

## Version

Introduced in version 4

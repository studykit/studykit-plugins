# WorkPoints Object

## Description

Provides access to all of the  objects in the parent document and provides methods to create new work points.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddAtCentroid](../WorkPoints/WorkPoints_AddAtCentroid.md) | Method that creates a new work point at the centroid of the input entities. This method is not currently supported when creating a work point within an assembly. |
| [AddByCurveAndEntity](../WorkPoints/WorkPoints_AddByCurveAndEntity.md) | Method that creates a new work point at the intersection of the input curve and entity. This method is not currently supported when creating a work point within an assembly. |
| [AddByMidPoint](../WorkPoints/WorkPoints_AddByMidPoint.md) | Method that creates a new work point at the midpoint of the input edge. This method is not currently supported when creating a work point within an assembly. |
| [AddByPoint](../WorkPoints/WorkPoints_AddByPoint.md) | Method that creates a new work point at the input point. This method is not currently supported when creating a work point within an assembly. |
| [AddBySphereCenterPoint](../WorkPoints/WorkPoints_AddBySphereCenterPoint.md) | Creates a new work point at the center of the sphere specified by the input face. This method is not currently supported when creating a work point within an assembly. |
| [AddByThreePlanes](../WorkPoints/WorkPoints_AddByThreePlanes.md) | Method that creates a new work point at the intersection of the three input planes. If the three input planes don't intersect an error will occur. This method is not currently supported when creating a work point within an assembly. |
| [AddByTorusCenterPoint](../WorkPoints/WorkPoints_AddByTorusCenterPoint.md) | Method that creates a new work point at the center of the torus specified by the input face. This method is not currently supported when creating a work point within an assembly. |
| [AddByTwoLines](../WorkPoints/WorkPoints_AddByTwoLines.md) | Method that creates a new work point at the intersection of the two input lines. If the lines don't intersect an error will occur. This method is not currently supported when creating a work point within an assembly. |
| [AddFixed](../WorkPoints/WorkPoints_AddFixed.md) | Method that creates a new work point at the position specified by the input point. When used to create a work point within an assembly the resulting work point will return an AssemblyWorkPointDef definition. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../WorkPoints/WorkPoints_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../WorkPoints/WorkPoints_Count.md) | Property that returns the number of items in this collection. |
| [Item](../WorkPoints/WorkPoints_Item.md) | Returns the specified WorkPoint object from the collection. This is the default property of the WorkPoints collection object. |
| [Parent](../WorkPoints/WorkPoints_Parent.md) | Property returning the parent  object. |
| [Type](../WorkPoints/WorkPoints_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[AssemblyComponentDefinition.WorkPoints](../AssemblyComponentDefinition/AssemblyComponentDefinition_WorkPoints.md), [FlatPattern.WorkPoints](../FlatPattern/FlatPattern_WorkPoints.md), [PartComponentDefinition.WorkPoints](../PartComponentDefinition/PartComponentDefinition_WorkPoints.md), [SheetMetalComponentDefinition.WorkPoints](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_WorkPoints.md), [WeldmentComponentDefinition.WorkPoints](../WeldmentComponentDefinition/WeldmentComponentDefinition_WorkPoints.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create sheet metal rip feature](../../sample-programs/RipFeatures_Add_Sample.md) | This sample demonstrates the creation of a rip sheet metal feature. |
| [Create sheet metal face and cut features](../../sample-programs/SheetMetalFeatures_Sample.md) | This sample demonstrates the creation of sheet metal face and cut features. |
| [Sweep Feature Add](../../sample-programs/SweepFeature_Sample.md) | This sample demonstrates the creation of a sweep feature. The profile is a circle, but the path is made up of a 3D sketch and a 2D sketch. |
| [UCS by three points](../../sample-programs/UserCoordinateSystems_Add_Sample.md) | This sample demonstrates the creation of a User Coordinate System (UCS) based on 3 points that define the origin, x-direction and y-direction for the UCS. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
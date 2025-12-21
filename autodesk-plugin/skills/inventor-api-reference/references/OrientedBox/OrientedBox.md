# OrientedBox Object

## Description

The OrientedBox object is a mathematical utility object that represents a rectangular box. Not like the Box object, the OrientedBox faces are not necessarily parallel to the model XY/XZ/YZ planes.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Contains](../OrientedBox/OrientedBox_Contains.md) | Determines whether the specified point is contained within this oriented box. |
| [Copy](../OrientedBox/OrientedBox_Copy.md) | Creates a copy of this OrientedBox object. |
| [GetOrientedBoxData](../OrientedBox/OrientedBox_GetOrientedBoxData.md) | Method that returns the corner point and edges data that define this OrientedBox. |
| [IsDisjoint](../OrientedBox/OrientedBox_IsDisjoint.md) | Determines whether this box does not intersect with the specified oriented box. |
| [PutOrientedBoxData](../OrientedBox/OrientedBox_PutOrientedBoxData.md) | Method that sets the corner point and edges data that define this OrientedBox. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [CornerPoint](../OrientedBox/OrientedBox_CornerPoint.md) | Read-write property that gets and sets the corner point for the OrientedBox object. |
| [DirectionOne](../OrientedBox/OrientedBox_DirectionOne.md) | Read-write property that gets and sets the vector that defines the first direction and length of the OrientedBox object. When set this value, the new vector should be parallel to the current vector, otherwise an error will occur. |
| [DirectionThree](../OrientedBox/OrientedBox_DirectionThree.md) | Read-write property that gets and sets the vector that defines the third direction and length of the OrientedBox object. When set this value, the new vector should be parallel to the current vector, otherwise an error will occur. |
| [DirectionTwo](../OrientedBox/OrientedBox_DirectionTwo.md) | Read-write property that gets and sets the vector that defines the second direction and length of the OrientedBox object. When set this value, the new vector should be parallel to the current vector, otherwise an error will occur. |

## Accessed From

[AssemblyComponentDefinition.OrientedMinimumRangeBox](../AssemblyComponentDefinition/AssemblyComponentDefinition_OrientedMinimumRangeBox.md), [ComponentDefinition.OrientedMinimumRangeBox](../ComponentDefinition/ComponentDefinition_OrientedMinimumRangeBox.md), [ComponentOccurrence.OrientedMinimumRangeBox](../ComponentOccurrence/ComponentOccurrence_OrientedMinimumRangeBox.md), [ComponentOccurrenceProxy.OrientedMinimumRangeBox](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_OrientedMinimumRangeBox.md), [FlatPattern.OrientedMinimumRangeBox](../FlatPattern/FlatPattern_OrientedMinimumRangeBox.md), [OrientedBox.Copy](../OrientedBox/OrientedBox_Copy.md), [PartComponentDefinition.OrientedMinimumRangeBox](../PartComponentDefinition/PartComponentDefinition_OrientedMinimumRangeBox.md), [PointCloudCrop.BoundingBox](../PointCloudCrop/PointCloudCrop_BoundingBox.md), [SheetMetalComponentDefinition.OrientedMinimumRangeBox](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_OrientedMinimumRangeBox.md), [SurfaceBody.OrientedMinimumRangeBox](../SurfaceBody/SurfaceBody_OrientedMinimumRangeBox.md), [SurfaceBodyProxy.OrientedMinimumRangeBox](../SurfaceBodyProxy/SurfaceBodyProxy_OrientedMinimumRangeBox.md), [TransientGeometry.CreateOrientedBox](../TransientGeometry/TransientGeometry_CreateOrientedBox.md), [VirtualComponentDefinition.OrientedMinimumRangeBox](../VirtualComponentDefinition/VirtualComponentDefinition_OrientedMinimumRangeBox.md), [WeldmentComponentDefinition.OrientedMinimumRangeBox](../WeldmentComponentDefinition/WeldmentComponentDefinition_OrientedMinimumRangeBox.md), [WeldsComponentDefinition.OrientedMinimumRangeBox](../WeldsComponentDefinition/WeldsComponentDefinition_OrientedMinimumRangeBox.md)

## Version

Introduced in version 2016

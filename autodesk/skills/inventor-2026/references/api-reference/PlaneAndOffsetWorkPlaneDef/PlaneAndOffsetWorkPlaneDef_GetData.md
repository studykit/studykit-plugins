# PlaneAndOffsetWorkPlaneDef.GetData Method

Parent Object: [PlaneAndOffsetWorkPlaneDef](../PlaneAndOffsetWorkPlaneDef/PlaneAndOffsetWorkPlaneDef.md)

## Description

Method that gets all of the data defining a work planed defined by a plane, direction and offset. The work plane is parallel to the plane and is offset the specified distance in the specified direction. The sign of the value controls which side of the plane the offset is in. A positive value will be in the positive normal side of the plane.

## Syntax

PlaneAndOffsetWorkPlaneDef.**GetData**( ***Plane*** As Object, ***Offset*** As [Parameter](../Parameter/Parameter.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Plane | Object | Output object that represents a plane. This object can be a planar Face, WorkPlane, or Sketch object. The work plane is parallel to this plane. |
| Offset | [Parameter](../Parameter/Parameter.md) | Output Parameter that defines the offset of the work plane to the plane. The sign of the value controls which side of the plane the offset is in. A positive value will be in the positive normal side of the plane. |

## Version

Introduced in version 4

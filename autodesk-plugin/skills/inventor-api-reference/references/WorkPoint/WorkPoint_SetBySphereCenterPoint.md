# WorkPoint.SetBySphereCenterPoint Method

Parent Object: [WorkPoint](../WorkPoint/WorkPoint.md)

## Description

Redefines the work point to be at the center of the Sphere specified by the input face.

## Remarks

This method is not valid when the work point exists in an Assembly component definition.

## Syntax

WorkPoint.**SetBySphereCenterPoint**( ***Face*** As [Face](../Face/Face.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Face | [Face](../Face/Face.md) | Input Face object whose geometry is a spherical surface. An error occurs if the geometry of the input face is not a spherical surface |

## Version

Introduced in version 2014

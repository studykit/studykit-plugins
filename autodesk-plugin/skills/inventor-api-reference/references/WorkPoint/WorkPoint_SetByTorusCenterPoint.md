# WorkPoint.SetByTorusCenterPoint Method

Parent Object: [WorkPoint](../WorkPoint/WorkPoint.md)

## Description

Method that redefines the work point to be at the center of the torus specified by the input face.

## Remarks

This method is not valid when the work point exists in an Assembly component definition.

## Syntax

WorkPoint.**SetByTorusCenterPoint**( ***Face*** As [Face](../Face/Face.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Face | [Face](../Face/Face.md) | Input Face object whose geometry is a torus surface. An error occurs if the geometry of the input face is not a torus surface. |

## Version

Introduced in version 2008

# WorkPlanes.AddByTorusMidPlane Method

Parent Object: [WorkPlanes](../WorkPlanes/WorkPlanes.md)

## Description

Method that creates a new work plane at the mid-plane of the torus specified by the input face. This method is not currently supported when creating a work plane within an assembly.

## Syntax

WorkPlanes.**AddByTorusMidPlane**( ***Face*** As [Face](../Face/Face.md), [***Construction***] As Boolean ) As [WorkPlane](../WorkPlane/WorkPlane.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Face | [Face](../Face/Face.md) | Input Face object that represents a torus surface. |
| Construction | Boolean | Optional Input Boolean that specifies whether to create the work plane as a construction plane or not. The default is False, which indicates to create a standard work plane, not a construction work plane. A construction work plane is hidden from the user and is not displayed graphically or listed in the browser. |

## Version

Introduced in version 2008

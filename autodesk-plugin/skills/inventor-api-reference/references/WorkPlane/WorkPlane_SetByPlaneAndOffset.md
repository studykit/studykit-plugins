# WorkPlane.SetByPlaneAndOffset Method

Parent Object: [WorkPlane](../WorkPlane/WorkPlane.md)

## Description

Method that redefines the work plane to be parallel to the input plane at a specified distance in the specified direction.

## Remarks

This method is not valid when the work plane exists in an Assembly component definition.

## Syntax

WorkPlane.**SetByPlaneAndOffset**( ***Plane*** As Object, ***Offset*** As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Plane | Object | Input object that represents a Plane. This object can be a planar Face, WorkPlane, or Sketch object.. |
| Offset | Variant | Input Variant that defines the offset distance of the Plane. This can be a numeric value or a string. The offset distance of a work plane is always defined by a parameter. When a new work plane is created that requires a parameter, that parameter is automatically created when the work plane is created. If a numeric value is supplied the new parameter is set to the value specified. The input value is in centimeters. If a string is supplied this will be used as the expression for the newly created parameter and will be interpreted the same as if the user entered it in a dialog. This means if a value is specified without a unit qualifier it will default to the current document length unit. The following is a valid entry for the offset, assuming the parameter d2 already exists and defines a length, 'd2 + 3 in'. The sign of the value controls which side of the plane the offset is in. A positive value will be in the positive normal side of the plane. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
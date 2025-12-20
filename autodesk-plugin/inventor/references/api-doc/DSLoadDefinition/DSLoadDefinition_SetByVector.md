# DSLoadDefinition.SetByVector Method

Parent Object: [DSLoadDefinition](../DSLoadDefinition/DSLoadDefinition.md)

## Description

Specifies the direction and magnitude of this load to be defined by the x, y, z components of a vector.

## Syntax

DSLoadDefinition.**SetByVector**( ***XComponent*** As Variant, ***YComponent*** As Variant, ***ZComponent*** As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| XComponent | Variant | Input Variant value that specifies the X component value of the vector. This can be either a Double indicating the load in database units, a String containing a valid expression that results in either force or torque units, or a DSValueGraph object. |
| YComponent | Variant | Input Variant value that specifies the Y component value of the vector. This can be either a Double indicating the load in database units, a String containing a valid expression that results in either force or torque units, or a DSValueGraph object. |
| ZComponent | Variant | Input Variant value that specifies the Z component value of the vector. This can be either a Double indicating the load in database units, a String containing a valid expression that results in either force or torque units, or a DSValueGraph object. |

## Version

Introduced in version 2013

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
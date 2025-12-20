# DSLoadDefinition.SetByMagnitudeAndDirection Method

Parent Object: [DSLoadDefinition](../DSLoadDefinition/DSLoadDefinition.md)

## Description

Specifies the direction and magnitude of this load to be defined by a magnitude value and a direction defined by an entity.

## Syntax

DSLoadDefinition.**SetByMagnitudeAndDirection**( ***Magnitude*** As Variant, ***DirectionEntity*** As Object, ***NaturalEntityDirection*** As Boolean )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Magnitude | Variant | Input Variant value that specifies the magnitude of the load. This can be either a Double indicating the load in database units, a String containing a valid expression that results in either force or torque units, or a DSGraph object. |
| DirectionEntity | Object | Input entity that defines the direction of the load. Valid geometry includes planar and cylindrical faces, and linear edges. |
| NaturalEntityDirection | Boolean | Input Boolean value that specifies if the direction is the same as the natural direction of the direction entity or reversed. |

## Version

Introduced in version 2013

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
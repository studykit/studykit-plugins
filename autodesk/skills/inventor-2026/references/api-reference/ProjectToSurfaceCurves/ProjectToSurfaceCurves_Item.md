# ProjectToSurfaceCurves.Item Property

Parent Object: [ProjectToSurfaceCurves](../ProjectToSurfaceCurves/ProjectToSurfaceCurves.md)

## Description

Allows integer-indexed access to items in the collection.

## Syntax

ProjectToSurfaceCurves.**Item**( ***Index*** As Variant ) As [ProjectToSurfaceCurve](../ProjectToSurfaceCurve/ProjectToSurfaceCurve.md)

## Property Value

This is a read only property whose value is a [ProjectToSurfaceCurve](../ProjectToSurfaceCurve/ProjectToSurfaceCurve.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the intersection curve to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the project to surface curve name. If an out of range index or a name of a non-existent project to surface curve is provided, an error occurs. |

## Version

Introduced in version 2021

# SilhouetteCurves.Item Property

Parent Object: [SilhouetteCurves](../SilhouetteCurves/SilhouetteCurves.md)

## Description

Allows integer-indexed access to items in the collection.

## Syntax

SilhouetteCurves.**Item**( ***Index*** As Variant ) As [SilhouetteCurve](../SilhouetteCurve/SilhouetteCurve.md)

## Property Value

This is a read only property whose value is a [SilhouetteCurve](../SilhouetteCurve/SilhouetteCurve.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the silhouette curve to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the silhouette curve name. If an out of range index or a name of a non-existent silhouette curve is provided, an error occurs. |

## Version

Introduced in version 2012

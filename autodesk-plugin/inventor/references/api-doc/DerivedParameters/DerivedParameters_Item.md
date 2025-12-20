# DerivedParameters.Item Property

Parent Object: [DerivedParameters](../DerivedParameters/DerivedParameters.md)

## Description

Method that returns the specified DerivedParameter object from the collection. This is the default method of the DerivedParameters collection object.

## Syntax

DerivedParameters.**Item**( ***Value*** As Variant ) As [DerivedParameter](../DerivedParameter/DerivedParameter.md)

## Property Value

This is a read only property whose value is a [DerivedParameter](../DerivedParameter/DerivedParameter.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Value | Variant | Value that specifies the DerivedParameter to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the parameter name. If an out of range index or a name of a non-existent parameter is provided, an error occurs. |

## Version

Introduced in version 11

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
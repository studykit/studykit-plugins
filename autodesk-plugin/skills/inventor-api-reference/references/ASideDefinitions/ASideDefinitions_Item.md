# ASideDefinitions.Item Property

Parent Object: [ASideDefinitions](../ASideDefinitions/ASideDefinitions.md)

## Description

Allows VARIANT-indexed access to items in the collection. You can use names as indexes as well.

## Syntax

ASideDefinitions.**Item**( ***Index*** As Variant ) As [ASideDefinition](../ASideDefinition/ASideDefinition.md)

## Property Value

This is a read only property whose value is an [ASideDefinition](../ASideDefinition/ASideDefinition.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the ASideDefinition to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the ASideDefinition name. If an out of range index or a name of a non-existent ASideDefinition is provided, an error occurs. |

## Version

Introduced in version 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
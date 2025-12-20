# DynamicSimulations.Item Property

Parent Object: [DynamicSimulations](../DynamicSimulations/DynamicSimulations.md)

## Description

Allows integer-indexed access to items in the collection.

## Syntax

DynamicSimulations.**Item**( ***Index*** As Long ) As [DynamicSimulation](../DynamicSimulation/DynamicSimulation.md)

## Property Value

This is a read only property whose value is a [DynamicSimulation](../DynamicSimulation/DynamicSimulation.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Long | Input Variant value that specifies the DynamicSimulation to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the DynamicSimulation name. If an out of range index or a name of a non-existent DynamicSimulation is provided, an error will occur. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Play back a simulation](../../sample-programs/DesignSimulation_PlaySimulation_Sample.md) | This sample plays back an existing dynamic simulation. |

## Version

Introduced in version 2013

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
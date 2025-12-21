# Environments.Item Property

Parent Object: [Environments](../Environments/Environments.md)

## Description

Returns the specified Environment object from the collection.

## Syntax

Environments.**Item**( ***Index*** As Variant ) As [Environment](../Environment/Environment.md)

## Property Value

This is a read only property whose value is an [Environment](../Environment/Environment.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant that specifies the environment within the collection to return. This can be either a Long to indicate the index of the item within the collection or a String indicating the name of the environment. If the specified name does not exist for a control, a failure occurs. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Play back a simulation](../../sample-programs/DesignSimulation_PlaySimulation_Sample.md) | This sample plays back an existing dynamic simulation. |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
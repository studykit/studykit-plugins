# ComponentOccurrences.AddByComponentDefinition Method

Parent Object: [ComponentOccurrences](../ComponentOccurrences/ComponentOccurrences.md)

## Description

Method that creates a new for a new part or subassembly. This method is the equivalent of the 'Create Component' command.

## Syntax

ComponentOccurrences.**AddByComponentDefinition**( ***CompDef*** As [ComponentDefinition](../ComponentDefinition/ComponentDefinition.md), ***Position*** As [Matrix](../Matrix/Matrix.md) ) As [ComponentOccurrence](../ComponentOccurrence/ComponentOccurrence.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| CompDef | [ComponentDefinition](../ComponentDefinition/ComponentDefinition.md) | Input object that will be referenced when creating the new occurrence. |
| Position | [Matrix](../Matrix/Matrix.md) | Input object that defines the location and orientation to position the occurrence. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Demote occurence](../../sample-programs/BrowserPaneObject_Reorder_Demote_Sample.md) | This sample demonstrates how to demote a top level occurrence in an assembly into a new sub-assembly occurrence. |
| [SurfaceBody Copy](../../sample-programs/CopyBodyFeature_Sample.md) | This sample demonstrates copying a surface body from one part to another. This is equivalent to the Promote command, but the API is much more flexible. In order for the sample to be self-contained, it creates two parts on the fly that will be used to demonstrate copying a body from one part to another. When copying a body into a part, you provide the surface body and a matrix to define its position in the new part. This sample creates a matrix based on the position of these parts within an assembly. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
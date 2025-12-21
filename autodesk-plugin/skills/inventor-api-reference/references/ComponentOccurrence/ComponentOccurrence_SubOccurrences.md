# ComponentOccurrence.SubOccurrences Property

Parent Object: [ComponentOccurrence](../ComponentOccurrence/ComponentOccurrence.md)

## Description

Property that returns the collection of occurrences for an occurrence. This property applies to occurrences that represent a subassembly. The collection returned provides access to the occurrences contained within the subassembly. If this collection is obtained from an occurrence that represents a part, it will not contain any occurrences.

## Syntax

ComponentOccurrence.**SubOccurrences**() As [ComponentOccurrencesEnumerator](../ComponentOccurrencesEnumerator/ComponentOccurrencesEnumerator.md)

## Property Value

This is a read only property whose value is a [ComponentOccurrencesEnumerator](../ComponentOccurrencesEnumerator/ComponentOccurrencesEnumerator.md).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Traverse an Assembly](../../sample-programs/AssemblyTraverse_Sample.md) | This sample shows how to recursively traverse an assembly and get the count of leaf node components and subassemblies. |
| [Promote occurence](../../sample-programs/BrowserPaneObject_Reorder_Promote_Sample.md) | This sample demonstrates how to promote an occurrence. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
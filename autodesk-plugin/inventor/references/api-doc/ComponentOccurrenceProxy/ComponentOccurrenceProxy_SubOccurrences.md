# ComponentOccurrenceProxy.SubOccurrences Property

Parent Object: [ComponentOccurrenceProxy](../ComponentOccurrenceProxy/ComponentOccurrenceProxy.md)

## Description

Property that returns the collection of occurrences for an occurrence. This property applies to occurrences that represent a subassembly. The collection returned provides access to the occurrences contained within the subassembly. If this collection is obtained from an occurrence that represents a part, it will not contain any occurrences.

## Syntax

ComponentOccurrenceProxy.**SubOccurrences**() As [ComponentOccurrencesEnumerator](../ComponentOccurrencesEnumerator/ComponentOccurrencesEnumerator.md)

## Property Value

This is a read only property whose value is a [ComponentOccurrencesEnumerator](../ComponentOccurrencesEnumerator/ComponentOccurrencesEnumerator.md).

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
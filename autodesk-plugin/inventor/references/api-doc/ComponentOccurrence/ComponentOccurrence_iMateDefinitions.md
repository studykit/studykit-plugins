# ComponentOccurrence.iMateDefinitions Property

Parent Object: [ComponentOccurrence](../ComponentOccurrence/ComponentOccurrence.md)

## Description

Property that returns the iMateDefinitions that are available from this occurrence. The iMateDefinition objects returned are actually proxies for the various iMateDefinition objects. These can be used as input to the Add and ValidResult methods of the iMateResults object.

## Syntax

ComponentOccurrence.**iMateDefinitions**() As [iMateDefinitionsEnumerator](../iMateDefinitionsEnumerator/iMateDefinitionsEnumerator.md)

## Property Value

This is a read only property whose value is an [iMateDefinitionsEnumerator](../iMateDefinitionsEnumerator/iMateDefinitionsEnumerator.md).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [iMate Result Creation](../../sample-programs/iMateResult_Sample.md) | This sample demonstrates creating an iMate result using two existin iMate definitions. |

## Version

Introduced in version 6

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# ComponentOccurrence.Replace Method

Parent Object: [ComponentOccurrence](../ComponentOccurrence/ComponentOccurrence.md)

## Description

Method that replaces the occurrence or all instances of an occurrence with another file.

## Remarks

If a replace fails, it may be due to the ownership control available since R12. For example, the hidden DocumentDescriptor.OwnershipType property using the kExclusiveOwnership enum will block replacement of the instance. Autodesk may find it necessary to mark parts or assemblies as exclusively owned. Exclusive ownership is specifically for an application to indicate that the components are not usable in other assemblies and have application controlled semantics in this assembly (in other words, the relationship between this parent and this child is very strong and application controlled).

## Syntax

ComponentOccurrence.**Replace**( ***FileName*** As String, ***ReplaceAll*** As Boolean )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FileName | String | Input filename of the new file to be used to replace the existing occurrence. |
| ReplaceAll | Boolean | Input Boolean that indicates whether the current occurrence should be replaced for all instances of this occurrence. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Replace content center part](../../sample-programs/ContentCenterPartReplace_Sample.md) | This sample demonstrates how to replace the content part referenced by an assembly occurrence. |

## Version

Introduced in version 5

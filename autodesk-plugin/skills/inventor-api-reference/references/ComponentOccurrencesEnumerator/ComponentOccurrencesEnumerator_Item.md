# ComponentOccurrencesEnumerator.Item Property

Parent Object: [ComponentOccurrencesEnumerator](../ComponentOccurrencesEnumerator/ComponentOccurrencesEnumerator.md)

## Description

Allows integer-indexed access to objects in the collection.

## Syntax

ComponentOccurrencesEnumerator.**Item**( ***Index*** As Long ) As [ComponentOccurrence](../ComponentOccurrence/ComponentOccurrence.md)

## Property Value

This is a read only property whose value is a [ComponentOccurrence](../ComponentOccurrence/ComponentOccurrence.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Long | Input Long value that specifies the index of the to return. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [iMate Creation During Occurrence Placement](../../sample-programs/AddUsingiMates_Sample.md) | This sample demonstrates creating multiple iMate results when adding an occurrence into an assembly. This uses the AddUsingiMate method which is the equivalent of using the Place Component command and checking the Use iMate check box on the dialog. |
| [Promote occurence](../../sample-programs/BrowserPaneObject_Reorder_Promote_Sample.md) | This sample demonstrates how to promote an occurrence. |

## Version

Introduced in version 4

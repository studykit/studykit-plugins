# ComponentOccurrenceProxy.Replace2 Method

Parent Object: [ComponentOccurrenceProxy](../ComponentOccurrenceProxy/ComponentOccurrenceProxy.md)

## Description

Replaces this component occurrence with another component. Can save replaced component and unset adaptivity.

## Syntax

ComponentOccurrenceProxy.**Replace2**( ***FileName*** As String, ***ReplaceAll*** As Boolean, [***SaveEdits***] As Variant, [***KeepAdaptivity***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FileName | String | Input String value indicates the full document name of another document to be used to replace the existing occurrence. |
| ReplaceAll | Boolean | Input Boolean that indicates whether the current occurrence should be replaced or all instances of this occurrence should be replaced. |
| SaveEdits | Variant | Optional input Boolean that specifies whether to save the edits in the component(s) that is being replaced. This defaults to False indicating the edits won’t be saved. |
| KeepAdaptivity | Variant | Optional input Boolean that specifies whether to keep the adaptivity after replacing the component(s). This defaults to False indicating the adaptivity is removed after replacement.   This is an optional argument whose default value is null. |

## Version

Introduced in version 2021

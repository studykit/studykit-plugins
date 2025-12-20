# AttributeSets.ParentAvailable Method

Parent Object: [AttributeSets](../AttributeSets/AttributeSets.md)

## Description

Method that returns whether the parent can be found.

## Syntax

AttributeSets.**ParentAvailable**( ***Parent*** As Object, [***Context***] As Variant ) As Boolean

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Parent | Object | Object that returns the parent. Returns Nothing if the method returns False. |
| Context | Variant | Optional output NameValueMap object. Possible values: \* ParentSuppressed As Boolean. Indicates whether the parent is in a suppressed occurrence. \* ParentMissing As Boolean. Indicates whether the parent is in a missing (unresolved) occurrence. \* ParentDeleted As Boolean. Indicates whether the parent is in a deleted occurrence. \* KnownOccurrencePath As ComponentOccurrence. Contains the known occurrence path in which the parent lives. |

## Version

Introduced in version 11

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
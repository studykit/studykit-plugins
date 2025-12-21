# ReferenceKeyManager.BindKeyToObject Method

Parent Object: [ReferenceKeyManager](../ReferenceKeyManager/ReferenceKeyManager.md)

## Description

Method to bind a reference key to the persistent object within the document. Returns a specific object, if there is a unique solution.

## Remarks

In case of multiple matches, it returns an ObjectCollection containing all the candidate matches. The primary match is always the first member of this collection. Except for the first element, the order is not significant. For more detailed information about primary and multiple matches and how they are determined, please see [More Ref Key Info...](MoreRefKeyInfo_Overview.md).
If you call this method in C# language and provide a variable to get the out argument MatchType remember to initialize the variable firstly before passing it as argument.

## Syntax

ReferenceKeyManager.**BindKeyToObject**( ***ReferenceKey***() As Byte, [***KeyContext***] As Long, [***MatchType***] As Variant ) As Object

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ReferenceKey | Byte | Input array of Bytes that contains the reference key to bind back. |
| KeyContext | Long | Input Long that specifies the key context to use. This must reference the same context data that was used when the key was originally generated. The key context must be supplied when working with any B-Rep entities (SurfaceBody, Face, Edge, etc.). For other entity types it is ignored. |
| MatchType | Variant | Output SolutionNatureEnum that returns the nature of the solution that was found.   This is an optional argument whose default value is null. |

## Version

Introduced in version 5

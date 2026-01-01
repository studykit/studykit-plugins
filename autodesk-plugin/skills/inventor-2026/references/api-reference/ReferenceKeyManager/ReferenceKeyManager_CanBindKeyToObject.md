# ReferenceKeyManager.CanBindKeyToObject Method

Parent Object: [ReferenceKeyManager](../ReferenceKeyManager/ReferenceKeyManager.md)

## Description

Method that returns whether the key can be bound to an entity or not.

## Syntax

ReferenceKeyManager.**CanBindKeyToObject**( ***ReferenceKey***() As Byte, [***KeyContext***] As Long, [***Object***] As Variant, [***Context***] As Variant ) As Boolean

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ReferenceKey | Byte | Array of bytes that contains a reference key. |
| KeyContext | Long | Input Long that specifies the key context to use. This must reference the same context data that was used when the key was originally generated. The key context must be supplied when working with any B-Rep entities (SurfaceBody, Face, Edge, etc.). For other entity types it is ignored. |
| Object | Variant | Optional output object that returns the object if the bind was successful. An ObjectCollection is returned if multiple matches are found. Returns Nothing if the method returns False.   This is an optional argument whose default value is null. |
| Context | Variant | Optional output NameValueMap object that returns information about the binding process.  Possible values:   * ObjectSuppressed As Boolean. Indicates whether the bind failed because the object is in a suppressed occurrence. * ObjectMissing As Boolean. Indicates whether the bind failed because the object is in a missing (unresolved) occurrence. * ObjectDeleted As Boolean. Indicates whether the bind failed because the object is in a deleted occurrence. * KnownOccurrencePath As ComponentOccurrence. Contains the known occurrence path in which the object lives. * MatchType As SolutionNatureEnum. Contains the nature of the solution if found.    This is an optional argument whose default value is null. |

## Version

Introduced in version 11

# TransitionSymbol.GetReferenceKey Method

Parent Object: [TransitionSymbol](../TransitionSymbol/TransitionSymbol.md)

## Description

Generate the sequence of bytes, called this object's reference key, which can be held onto beyond document edits and which will allow the caller to be bound back to the live object.

## Syntax

TransitionSymbol.**GetReferenceKey**( ***ReferenceKey***() As Byte, [***KeyContext***] As Long )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ReferenceKey | Byte | Output array of Bytes that contains the reference key. |
| KeyContext | Long | Input Long that specifies the key context. A key context is created using the CreateKeyContext method of the ReferenceKeyManager object. The key context must be supplied when working with any B-Rep entities (SurfaceBody, FaceShell, Face, Edge, EdgeUse and Vertex objects). For all other object types, the key context argument is not used and is ignored if provided. |

## Version

Introduced in version 2025.1

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
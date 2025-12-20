# Face.GetReferenceKey Method

Parent Object: [Face](../Face/Face.md)

## Description

Method that generates and returns the reference key for this entity.

## Remarks

The reference key is an array of bytes that can be used as a persistent reference for this entity. To obtain the entity at a later time using the reference key you use the BindKeyToObject method of the object. The ReferenceKeyManager object is obtained using the ReferenceKeyManager property of the Document object.

## Syntax

Face.**GetReferenceKey**( ***ReferenceKey***() As Byte, [***KeyContext***] As Long )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ReferenceKey | Byte | Input/output array of Bytes that contains the reference key. |
| KeyContext | Long | Input Long that specifies the key context. The key context must be supplied when working with any B-Rep entities (and SurfaceBody, FaceShell, Face, Edge, EdgeUse and Vertex objects). A key context is created using the CreateKeyContext method of the ReferenceKeyManager object. For all other object types, the key context argument is not used and is ignored if provided. |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
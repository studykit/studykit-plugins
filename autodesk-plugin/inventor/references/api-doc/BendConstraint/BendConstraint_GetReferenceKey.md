# BendConstraint.GetReferenceKey Method

Parent Object: [BendConstraint](../BendConstraint/BendConstraint.md)

## Description

Method that generates and returns the reference key for this entity.

## Syntax

BendConstraint.**GetReferenceKey**( ***ReferenceKey***() As Byte, [***KeyContext***] As Long )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ReferenceKey | Byte | Input/output array of Bytes that contains the reference key. |
| KeyContext | Long | Input Long that specifies the key context. The key context must be supplied when working with any B-Rep entities (and SurfaceBody, FaceShell, Face, Edge, EdgeUse and Vertex objects). A key context is created using the CreateKeyContext method of the ReferenceKeyManager object. For all other object types, the key context argument is not used and is ignored if provided. |

## Version

Introduced in version 6

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
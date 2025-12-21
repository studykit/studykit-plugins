# ProjectToSurfaceCurveProxy.GetReferenceKey Method

Parent Object: [ProjectToSurfaceCurveProxy](../ProjectToSurfaceCurveProxy/ProjectToSurfaceCurveProxy.md)

## Description

Generate the sequence of bytes, called this object's reference key, which can be held onto beyond document edits and which will allow the caller to be bound back to the live object.

## Syntax

ProjectToSurfaceCurveProxy.**GetReferenceKey**( ***ReferenceKey***() As Byte, [***KeyContext***] As Long )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ReferenceKey | Byte | Output array of Bytes that contains the reference key. |
| KeyContext | Long | Optional input Long that specifies the key context to use when creating the reference key. Although this argument is optional, you must currently always provide a valid key context. A key context is created using the CreateKeyContext method of the ReferenceKeyManager object. |

## Version

Introduced in version 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# TransientBRep.GetIdenticalBodies Method

Parent Object: [TransientBRep](../TransientBRep/TransientBRep.md)

## Description

Method that find the identical SurfaceBody objects in a SurfaceBody objects collection. In the return value, all the identical surface bodies will be placed in the same ObjectCollection.

## Syntax

TransientBRep.**GetIdenticalBodies**( ***InputSurfaceBodies*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md), [***Options***] As Variant ) As [ObjectCollection](../ObjectCollection/ObjectCollection.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| InputSurfaceBodies | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | Input ObjectCollection that includes the SurfaceBody objects to compute the identity ones in it. |
| Options | Variant | Optional input NameValueMap that specifies the options when compute the comparison. Valid options includes: Name = Tolerance. Value = Double that specifies the tolerance when compare the surface bodies. If this is not specified, the default tolerance value 0.000001 will be used. |

## Version

Introduced in version 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
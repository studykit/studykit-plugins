# SurfaceBodyProxy.AlternateBody Property

Parent Object: [SurfaceBodyProxy](../SurfaceBodyProxy/SurfaceBodyProxy.md)

## Description

Property that returns a new SurfaceBody that was derived from the existing body using the specified form input. The primary purpose of this property is to obtain a body that consists entirely of NURBS surfaces.

## Syntax

SurfaceBodyProxy.**AlternateBody**( ***AlternateForm*** As Long ) As [SurfaceBody](../SurfaceBody/SurfaceBody.md)

## Property Value

This is a read only property whose value is a [SurfaceBody](../SurfaceBody/SurfaceBody.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| AlternateForm | Long | AlternateForm \- Input Long that is the sum of values describing the desired form. |

## Version

Introduced in version 4

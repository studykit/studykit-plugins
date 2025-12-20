# SweepFeature.EndFaces Property

Parent Object: [SweepFeature](../SweepFeature/SweepFeature.md)

## Description

Property that returns the set of that cap one end of the sweep that are coincident with the sketch plane. The end faces are those not coincident to the sketch plane of the feature's profile. In the case of a symmetric revolution these faces are the ones on the negative normal side of the sketch plane. In the cases where there aren't any end faces this property will return Nothing.

## Syntax

SweepFeature.**EndFaces**() As [Faces](../Faces/Faces.md)

## Property Value

This is a read only property whose value is a [Faces](../Faces/Faces.md).

## Version

Introduced in version 6

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
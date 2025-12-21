# IntersectionCurveProxy.SketchEntities Property

Parent Object: [IntersectionCurveProxy](../IntersectionCurveProxy/IntersectionCurveProxy.md)

## Description

Read-only property that returns a collection of sketch entities that belong to the intersection curve. The sketch entities returned by this property cannot be edited or deleted because they are associated with the intersection curve in the model. The BreakLink method can be used to break this association so they are individually editable.

## Syntax

IntersectionCurveProxy.**SketchEntities**() As [SketchEntities3DEnumerator](../SketchEntities3DEnumerator/SketchEntities3DEnumerator.md)

## Property Value

This is a read only property whose value is a [SketchEntities3DEnumerator](../SketchEntities3DEnumerator/SketchEntities3DEnumerator.md).

## Version

Introduced in version 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
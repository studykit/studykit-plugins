# WorkPoint.ReferencedEntity Property

Parent Object: [WorkPoint](../WorkPoint/WorkPoint.md)

## Description

Property that returns the referenced WorkPoint in the case where this work point was created using a referenced component. An example of this is when a work point is selected as part of a derived part. The HasReferenceComponent property indicates if this work point is based on a referenced component or not. This property returns Nothing in the case where it is not based on a referenced component.

## Syntax

WorkPoint.**ReferencedEntity**() As [WorkPoint](../WorkPoint/WorkPoint.md)

## Property Value

This is a read only property whose value is a [WorkPoint](../WorkPoint/WorkPoint.md).

## Version

Introduced in version 5.3

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
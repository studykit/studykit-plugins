# SectionDrawingView.SliceAllParts Property

Parent Object: [SectionDrawingView](../SectionDrawingView/SectionDrawingView.md)

## Description

Property that gets and sets whether to override all individual settings and slice all components in the view according to the Section Line geometry. Components that are not crossed by the Section Line will not participate in the resulting view. Setting this property to True automatically toggles the IncludeSlice property to True. This property does not apply (and setting it returns an error) for drawing views of a part.

## Syntax

SectionDrawingView.**SliceAllParts**() As Boolean

## Property Value

This is a read/write property whose value is a Boolean.

## Version

Introduced in version 2009

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
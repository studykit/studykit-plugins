# SketchDrivenPatternDefinition.ParentFeatures Property

Parent Object: [SketchDrivenPatternDefinition](../SketchDrivenPatternDefinition/SketchDrivenPatternDefinition.md)

## Description

Read-write property that gets and sets the parent features of the pattern. The ObjectCollection returned by this property is a “tear off” and does not affect the pattern if its contents are modified. To change the which features are the parents of the pattern you need to use this property to set the parent features by providing an ObjectCollection that contains the desired set of parent features.

## Syntax

SketchDrivenPatternDefinition.**ParentFeatures**() As [ObjectCollection](../ObjectCollection/ObjectCollection.md)

## Property Value

This is a read/write property whose value is an [ObjectCollection](../ObjectCollection/ObjectCollection.md).

## Version

Introduced in version 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
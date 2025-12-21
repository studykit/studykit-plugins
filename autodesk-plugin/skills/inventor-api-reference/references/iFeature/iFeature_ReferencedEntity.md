# iFeature.ReferencedEntity Property

Parent Object: [iFeature](../iFeature/iFeature.md)

## Description

Property that returns the entity in the base part or assembly document. In the case of a derived assembly, the ReferencedEntity property returns the component occurrence in the base assembly that this ReferenceFeature represents. In the case of a derived part, the ReferencedEntity property can return a solid or surface body of the source part or a surface in the source part.. In cases where the component occurrence, solid or surface body entity is referencing a model entity, but the model entity no longer exists because it has been consumed by a subsequent modeling operation, this property will return Nothing.

## Syntax

iFeature.**ReferencedEntity**() As Object

## Property Value

This is a read only property whose value is an Object.

## Version

Introduced in version 2009

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
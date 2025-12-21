# SketchCircle3D.ReferencedEntity Property

Parent Object: [SketchCircle3D](../SketchCircle3D/SketchCircle3D.md)

## Description

Property that returns the object this entity is dependent on. When sketch entities are created by projecting model edges or intersecting the model, the resulting entities are driven by the original model entities and cannot be modified. This property returns the model entity the sketch entity is dependent on. The Reference property indicates whether the sketch entity is driven by a model entity or not. If the sketch entity is not referencing a model entity, this property will return Nothing. This property can also return nothing even when the sketch entity is referencing a model entity in the case where the model entity has been consumed by some subsequent modeling operation.

## Syntax

SketchCircle3D.**ReferencedEntity**() As Object

## Property Value

This is a read only property whose value is an Object.

## Version

Introduced in version 7

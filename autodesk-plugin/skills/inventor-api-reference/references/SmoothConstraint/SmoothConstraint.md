# SmoothConstraint Object

Derived from: [GeometricConstraint](../GeometricConstraint/GeometricConstraint.md) Object

## Description

The SmoothConstraint object represents a smooth (G2-continuous) constraint within a sketch.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../SmoothConstraint/SmoothConstraint_Delete.md) | Method that deletes the constraint. |
| [GetReferenceKey](../SmoothConstraint/SmoothConstraint_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SmoothConstraint/SmoothConstraint_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../SmoothConstraint/SmoothConstraint_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Deletable](../SmoothConstraint/SmoothConstraint_Deletable.md) | Indicates whether this object is deletable. |
| [EntityOne](../SmoothConstraint/SmoothConstraint_EntityOne.md) | Property that returns the sketch entity that is constrained to be smooth (G2-continuous) to entity two. |
| [EntityTwo](../SmoothConstraint/SmoothConstraint_EntityTwo.md) | Property that returns the sketch entity that is constrained to be smooth (G2-continuous) to entity one. |
| [Parent](../SmoothConstraint/SmoothConstraint_Parent.md) | Property that returns the parent sketch of the object. |
| [Type](../SmoothConstraint/SmoothConstraint_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[GeometricConstraints.AddSmooth](../GeometricConstraints/GeometricConstraints_AddSmooth.md), [SmoothConstraintProxy.NativeObject](../SmoothConstraintProxy/SmoothConstraintProxy_NativeObject.md)

## Derived Classes

[SmoothConstraintProxy](../SmoothConstraintProxy/SmoothConstraintProxy.md)

## Version

Introduced in version 11

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
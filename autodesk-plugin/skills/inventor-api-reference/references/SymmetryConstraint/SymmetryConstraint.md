# SymmetryConstraint Object

Derived from: [GeometricConstraint](../GeometricConstraint/GeometricConstraint.md) Object

## Description

The SymmetryConstraint object represents a symmetry constraint within a sketch.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../SymmetryConstraint/SymmetryConstraint_Delete.md) | Method that deletes the constraint. |
| [GetReferenceKey](../SymmetryConstraint/SymmetryConstraint_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SymmetryConstraint/SymmetryConstraint_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../SymmetryConstraint/SymmetryConstraint_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Deletable](../SymmetryConstraint/SymmetryConstraint_Deletable.md) | Indicates whether this object is deletable. |
| [EntityOne](../SymmetryConstraint/SymmetryConstraint_EntityOne.md) | Property that returns the sketch entity that is constrained to be symmetric to the entity returned by the EntityTwo property. |
| [EntityTwo](../SymmetryConstraint/SymmetryConstraint_EntityTwo.md) | Property that returns the sketch entity that is constrained to be symmetric to the entity returned by the EntityOne property. |
| [Parent](../SymmetryConstraint/SymmetryConstraint_Parent.md) | Property that returns the parent sketch of the object. |
| [SymmetryLine](../SymmetryConstraint/SymmetryConstraint_SymmetryLine.md) | Property that returns the sketch entity that defines the axis of symmetry. |
| [Type](../SymmetryConstraint/SymmetryConstraint_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[GeometricConstraints.AddSymmetry](../GeometricConstraints/GeometricConstraints_AddSymmetry.md), [SymmetryConstraintProxy.NativeObject](../SymmetryConstraintProxy/SymmetryConstraintProxy_NativeObject.md)

## Derived Classes

[SymmetryConstraintProxy](../SymmetryConstraintProxy/SymmetryConstraintProxy.md)

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
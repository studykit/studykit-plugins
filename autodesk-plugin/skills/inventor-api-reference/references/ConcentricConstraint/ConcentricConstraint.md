# ConcentricConstraint Object

Derived from: [GeometricConstraint](../GeometricConstraint/GeometricConstraint.md) Object

## Description

The Sketch ConcentricConstraint object represents a concentric constraint within a sketch. Makes a circle, arc, ellipse, or elliptical arc concentric to another circle, arc, ellipse, or elliptical arc.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../ConcentricConstraint/ConcentricConstraint_Delete.md) | Method that deletes the constraint. |
| [GetReferenceKey](../ConcentricConstraint/ConcentricConstraint_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ConcentricConstraint/ConcentricConstraint_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../ConcentricConstraint/ConcentricConstraint_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [CenterPointConstraint](../ConcentricConstraint/ConcentricConstraint_CenterPointConstraint.md) | Gets a Boolean indicating if the constraint is between the arc and its centerpoint or not. |
| [Deletable](../ConcentricConstraint/ConcentricConstraint_Deletable.md) | Indicates whether this object is deletable. |
| [EntityOne](../ConcentricConstraint/ConcentricConstraint_EntityOne.md) | Gets the sketch entity being constrained. |
| [EntityTwo](../ConcentricConstraint/ConcentricConstraint_EntityTwo.md) | Gets the sketch entity being constrained. |
| [Parent](../ConcentricConstraint/ConcentricConstraint_Parent.md) | Property that returns the parent sketch of the object. |
| [Type](../ConcentricConstraint/ConcentricConstraint_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[ConcentricConstraintProxy.NativeObject](../ConcentricConstraintProxy/ConcentricConstraintProxy_NativeObject.md), [GeometricConstraints.AddConcentric](../GeometricConstraints/GeometricConstraints_AddConcentric.md)

## Derived Classes

[ConcentricConstraintProxy](../ConcentricConstraintProxy/ConcentricConstraintProxy.md)

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# TangentSketchConstraint Object

Derived from: [GeometricConstraint](../GeometricConstraint/GeometricConstraint.md) Object

## Description

The TangentSketchConstraint object represents a tangent constraint within a sketch.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../TangentSketchConstraint/TangentSketchConstraint_Delete.md) | Method that deletes the constraint. |
| [GetReferenceKey](../TangentSketchConstraint/TangentSketchConstraint_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../TangentSketchConstraint/TangentSketchConstraint_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../TangentSketchConstraint/TangentSketchConstraint_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Deletable](../TangentSketchConstraint/TangentSketchConstraint_Deletable.md) | Indicates whether this object is deletable. |
| [EntityOne](../TangentSketchConstraint/TangentSketchConstraint_EntityOne.md) | Property that returns the sketch entity that is constrained to be tangent to entity two. |
| [EntityTwo](../TangentSketchConstraint/TangentSketchConstraint_EntityTwo.md) | Property that returns the sketch entity that is constrained to be tangent to entity one. |
| [Parent](../TangentSketchConstraint/TangentSketchConstraint_Parent.md) | Property that returns the parent sketch of the object. |
| [Type](../TangentSketchConstraint/TangentSketchConstraint_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[GeometricConstraints.AddTangent](../GeometricConstraints/GeometricConstraints_AddTangent.md), [TangentSketchConstraintProxy.NativeObject](../TangentSketchConstraintProxy/TangentSketchConstraintProxy_NativeObject.md)

## Derived Classes

[TangentSketchConstraintProxy](../TangentSketchConstraintProxy/TangentSketchConstraintProxy.md)

## Version

Introduced in version 5

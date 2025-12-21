# BendConstraint Object

Derived from: [GeometricConstraint3D](../GeometricConstraint3D/GeometricConstraint3D.md) Object

## Description

The BendConstraint object represents a bend constraint within a 3D sketch.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../BendConstraint/BendConstraint_Delete.md) | Method that deletes the constraint. In the case of coincident constraint, all the connected lines are disconnected and the constraint is deleted. |
| [GetReferenceKey](../BendConstraint/BendConstraint_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../BendConstraint/BendConstraint_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Arc](../BendConstraint/BendConstraint_Arc.md) | Property that returns the SketchArc3D object associated with the bend. |
| [AttributeSets](../BendConstraint/BendConstraint_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Deletable](../BendConstraint/BendConstraint_Deletable.md) | Indicates whether this object can be deleted. |
| [LineOne](../BendConstraint/BendConstraint_LineOne.md) | Property that returns the Sketch Line used to construct the bend feature. |
| [LineTwo](../BendConstraint/BendConstraint_LineTwo.md) | Property that returns the Sketch Line used to construct the bend feature. |
| [Parent](../BendConstraint/BendConstraint_Parent.md) | Property that returns the parent sketch of the object. |
| [Radius](../BendConstraint/BendConstraint_Radius.md) | Property that returns the parameter controlling the radius of the bend. |
| [Type](../BendConstraint/BendConstraint_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[BendConstraintProxy.NativeObject](../BendConstraintProxy/BendConstraintProxy_NativeObject.md)

## Derived Classes

[BendConstraintProxy](../BendConstraintProxy/BendConstraintProxy.md)

## Version

Introduced in version 6

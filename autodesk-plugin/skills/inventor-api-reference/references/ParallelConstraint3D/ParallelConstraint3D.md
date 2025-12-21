# ParallelConstraint3D Object

Derived from: [GeometricConstraint3D](../GeometricConstraint3D/GeometricConstraint3D.md) Object

## Description

The ParallelConstraint3D object represents a parallel constraint within a 3D sketch.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../ParallelConstraint3D/ParallelConstraint3D_Delete.md) | Method that deletes the constraint. In the case of coincident constraint, all the connected lines are disconnected and the constraint is deleted. |
| [GetReferenceKey](../ParallelConstraint3D/ParallelConstraint3D_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ParallelConstraint3D/ParallelConstraint3D_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../ParallelConstraint3D/ParallelConstraint3D_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Deletable](../ParallelConstraint3D/ParallelConstraint3D_Deletable.md) | Indicates whether this object can be deleted. |
| [EntityOne](../ParallelConstraint3D/ParallelConstraint3D_EntityOne.md) | Property that returns the first entity being constrained. |
| [EntityTwo](../ParallelConstraint3D/ParallelConstraint3D_EntityTwo.md) | Property that returns the second entity being constrained. |
| [Parent](../ParallelConstraint3D/ParallelConstraint3D_Parent.md) | Property that returns the parent sketch of the object. |
| [Type](../ParallelConstraint3D/ParallelConstraint3D_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[GeometricConstraints3D.AddParallel](../GeometricConstraints3D/GeometricConstraints3D_AddParallel.md), [ParallelConstraint3DProxy.NativeObject](../ParallelConstraint3DProxy/ParallelConstraint3DProxy_NativeObject.md)

## Derived Classes

[ParallelConstraint3DProxy](../ParallelConstraint3DProxy/ParallelConstraint3DProxy.md)

## Version

Introduced in version 10

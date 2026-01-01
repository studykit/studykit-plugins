# SymmetryConstraintProxy Object

Derived from: [SymmetryConstraint](../SymmetryConstraint/SymmetryConstraint.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../SymmetryConstraintProxy/SymmetryConstraintProxy_Delete.md) | Method that deletes the constraint. |
| [GetReferenceKey](../SymmetryConstraintProxy/SymmetryConstraintProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SymmetryConstraintProxy/SymmetryConstraintProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../SymmetryConstraintProxy/SymmetryConstraintProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ContainingOccurrence](../SymmetryConstraintProxy/SymmetryConstraintProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [Deletable](../SymmetryConstraintProxy/SymmetryConstraintProxy_Deletable.md) | Indicates whether this object is deletable. |
| [EntityOne](../SymmetryConstraintProxy/SymmetryConstraintProxy_EntityOne.md) | Property that returns the sketch entity that is constrained to be symmetric to the entity returned by the EntityTwo property. |
| [EntityTwo](../SymmetryConstraintProxy/SymmetryConstraintProxy_EntityTwo.md) | Property that returns the sketch entity that is constrained to be symmetric to the entity returned by the EntityOne property. |
| [NativeObject](../SymmetryConstraintProxy/SymmetryConstraintProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [Parent](../SymmetryConstraintProxy/SymmetryConstraintProxy_Parent.md) | Property that returns the parent sketch of the object. |
| [SymmetryLine](../SymmetryConstraintProxy/SymmetryConstraintProxy_SymmetryLine.md) | Property that returns the sketch entity that defines the axis of symmetry. |
| [Type](../SymmetryConstraintProxy/SymmetryConstraintProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 6

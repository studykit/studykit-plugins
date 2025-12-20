# RadiusDimConstraint Object

Derived from: [DimensionConstraint](../DimensionConstraint/DimensionConstraint.md) Object

## Description

The RadiusDimConstraint object represents a constraint that controls the radius of a circle or arc.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../RadiusDimConstraint/RadiusDimConstraint_Delete.md) | Method that deletes the constraint. |
| [GetReferenceKey](../RadiusDimConstraint/RadiusDimConstraint_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AnchorPoints](../RadiusDimConstraint/RadiusDimConstraint_AnchorPoints.md) | Gets the anchor points of dimension. |
| [Application](../RadiusDimConstraint/RadiusDimConstraint_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../RadiusDimConstraint/RadiusDimConstraint_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [DimensionCenterPoint](../RadiusDimConstraint/RadiusDimConstraint_DimensionCenterPoint.md) | Gets the center of the dimension line. |
| [Driven](../RadiusDimConstraint/RadiusDimConstraint_Driven.md) | Gets and sets whether this dimension constraint is driving the geometry or the geometry is defining the value associated with the constraint. |
| [Entity](../RadiusDimConstraint/RadiusDimConstraint_Entity.md) | Property that returns the entity being constrained to. |
| [Parameter](../RadiusDimConstraint/RadiusDimConstraint_Parameter.md) | Property that returns the parameter associated with this dimension constraint. If the Driven property of the constraint is True, this will return a ReferenceParameter object. Otherwise it will return a ModelParameter object. |
| [Parent](../RadiusDimConstraint/RadiusDimConstraint_Parent.md) | Property that returns the parent sketch of the object. |
| [TextPoint](../RadiusDimConstraint/RadiusDimConstraint_TextPoint.md) | Gets and sets the position of the dimension text. |
| [Type](../RadiusDimConstraint/RadiusDimConstraint_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[DimensionConstraints.AddRadius](../DimensionConstraints/DimensionConstraints_AddRadius.md), [RadiusDimConstraintProxy.NativeObject](../RadiusDimConstraintProxy/RadiusDimConstraintProxy_NativeObject.md)

## Derived Classes

[RadiusDimConstraintProxy](../RadiusDimConstraintProxy/RadiusDimConstraintProxy.md)

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
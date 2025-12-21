# DiameterDimConstraintProxy Object

Derived from: [DiameterDimConstraint](../DiameterDimConstraint/DiameterDimConstraint.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../DiameterDimConstraintProxy/DiameterDimConstraintProxy_Delete.md) | Method that deletes the constraint. |
| [GetReferenceKey](../DiameterDimConstraintProxy/DiameterDimConstraintProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AnchorPoints](../DiameterDimConstraintProxy/DiameterDimConstraintProxy_AnchorPoints.md) | Gets the anchor points of dimension. |
| [Application](../DiameterDimConstraintProxy/DiameterDimConstraintProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../DiameterDimConstraintProxy/DiameterDimConstraintProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ContainingOccurrence](../DiameterDimConstraintProxy/DiameterDimConstraintProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [DimensionCenterPoint](../DiameterDimConstraintProxy/DiameterDimConstraintProxy_DimensionCenterPoint.md) | Gets the center of the dimension line. |
| [Driven](../DiameterDimConstraintProxy/DiameterDimConstraintProxy_Driven.md) | Gets and sets whether this dimension constraint is driving the geometry or the geometry is defining the value associated with the constraint. |
| [Entity](../DiameterDimConstraintProxy/DiameterDimConstraintProxy_Entity.md) | Property that returns the circle or arc being constrained. |
| [NativeObject](../DiameterDimConstraintProxy/DiameterDimConstraintProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [Parameter](../DiameterDimConstraintProxy/DiameterDimConstraintProxy_Parameter.md) | Property that returns the parameter associated with this dimension constraint. If the Driven property of the constraint is True, this will return a ReferenceParameter object. Otherwise it will return a ModelParameter object. |
| [Parent](../DiameterDimConstraintProxy/DiameterDimConstraintProxy_Parent.md) | Property that returns the parent sketch of the object. |
| [TextPoint](../DiameterDimConstraintProxy/DiameterDimConstraintProxy_TextPoint.md) | Gets and sets the position of the dimension text. |
| [Type](../DiameterDimConstraintProxy/DiameterDimConstraintProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 6

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# RadiusDimConstraintProxy Object

Derived from: [RadiusDimConstraint](../RadiusDimConstraint/RadiusDimConstraint.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../RadiusDimConstraintProxy/RadiusDimConstraintProxy_Delete.md) | Method that deletes the constraint. |
| [GetReferenceKey](../RadiusDimConstraintProxy/RadiusDimConstraintProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AnchorPoints](../RadiusDimConstraintProxy/RadiusDimConstraintProxy_AnchorPoints.md) | Gets the anchor points of dimension. |
| [Application](../RadiusDimConstraintProxy/RadiusDimConstraintProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../RadiusDimConstraintProxy/RadiusDimConstraintProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ContainingOccurrence](../RadiusDimConstraintProxy/RadiusDimConstraintProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [DimensionCenterPoint](../RadiusDimConstraintProxy/RadiusDimConstraintProxy_DimensionCenterPoint.md) | Gets the center of the dimension line. |
| [Driven](../RadiusDimConstraintProxy/RadiusDimConstraintProxy_Driven.md) | Gets and sets whether this dimension constraint is driving the geometry or the geometry is defining the value associated with the constraint. |
| [Entity](../RadiusDimConstraintProxy/RadiusDimConstraintProxy_Entity.md) | Property that returns the entity being constrained to. |
| [NativeObject](../RadiusDimConstraintProxy/RadiusDimConstraintProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [Parameter](../RadiusDimConstraintProxy/RadiusDimConstraintProxy_Parameter.md) | Property that returns the parameter associated with this dimension constraint. If the Driven property of the constraint is True, this will return a ReferenceParameter object. Otherwise it will return a ModelParameter object. |
| [Parent](../RadiusDimConstraintProxy/RadiusDimConstraintProxy_Parent.md) | Property that returns the parent sketch of the object. |
| [TextPoint](../RadiusDimConstraintProxy/RadiusDimConstraintProxy_TextPoint.md) | Gets and sets the position of the dimension text. |
| [Type](../RadiusDimConstraintProxy/RadiusDimConstraintProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 6
